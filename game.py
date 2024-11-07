import random


class Game:
    def __init__(self, home_team, away_team, home_goalie, away_goalie):
        self.home = home_team
        self.visitor = away_team
        self.home_goalie = home_goalie
        self.visitor_goalie = away_goalie
        self.home_sog = self.__get_sog(self.home.offense, self.visitor.defense, home_team=True)
        self.visitor_sog = self.__get_sog(self.visitor.offense, self.home.defense, home_team=False)
        self.home_goals = self.__get_goals(self.home_sog, self.visitor_goalie.rating, self.home)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.home_goalie.rating, self.visitor)

        # Simulate penalties during the game
        self.home_penalties = self.__get_penalties(self.home)
        self.visitor_penalties = self.__get_penalties(self.visitor)

        # Adjust goals scored based on powerplay efficiency
        self.home_goals += self.__get_powerplay_goals(self.home, self.visitor)
        self.visitor_goals += self.__get_powerplay_goals(self.visitor, self.home)

        self.winner, self.regulation = self.__get_winner()

    @staticmethod
    def find_closest_value(value, keys):
        return min(keys, key=lambda k: abs(k - value))

    def __get_penalties(self, team):
        """Determine if a team gets penalized, based on its penalty stat."""
        # You want a team with a penalty rating of 50 to get ~3 penalties per game.
        target_penalties_per_game = 3
        # Penalty probability is inversely proportional to the penalty rating (lower rating -> more penalties)
        penalty_rate = 100 - team.penalty  # Lower penalty rating = more likely to take penalties
        # Scale penalty chance to get an average of 3 penalties for a penalty rating of 50
        expected_penalties = (penalty_rate / 100) * target_penalties_per_game

        penalties = 0
        for _ in range(int(expected_penalties)):  # Simulate expected penalties
            penalty_chance = random.random()
            if penalty_chance <= expected_penalties / target_penalties_per_game:
                penalties += 1

        return penalties

    def __get_powerplay_goals(self, team, opponent):
        """Calculate powerplay goals based on powerplay stat and opponent penaltykill."""
        powerplay_effectiveness = team.powerplay / 100
        penaltykill_effectiveness = opponent.penaltykill / 100

        base_chance = 0.20

        effectiveness_ratio = (powerplay_effectiveness - penaltykill_effectiveness)

        adjusted_chance = base_chance + (effectiveness_ratio * 0.15)

        adjusted_chance = max(0, min(1, adjusted_chance))

        powerplay_chance = random.random()

        if powerplay_chance <= adjusted_chance:
            return 1
        return 0

    @classmethod
    def __get_sog(cls, offense, defense, home_team=False):
        # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
        ranges = [
            (40, [(40, (15, 38)), (42.5, (15, 35)), (45, (15, 32)), (47.5, (15, 30)), (50, (15, 28)), (52.5, (15, 25)),
                  (55, (14, 25)), (57.5, (13, 25))]),
            (42.5, [(40, (16, 40)), (42.5, (16, 38)), (45, (16, 35)), (47.5, (16, 32)), (50, (16, 30)), (52.5, (16, 28)),
                  (55, (15, 28)), (57.5, (14, 28))]),
            (45, [(40, (17, 40)), (42.5, (17, 38)), (45, (17, 35)), (47.5, (17, 32)), (50, (17, 30)), (52.5, (17, 28)),
                  (110, (16, 28)), (115, (15, 28))]),
            (47.5, [(40, (18, 40)), (42.5, (18, 38)), (45, (18, 36)), (47.5, (18, 35)), (50, (18, 32)), (52.5, (18, 30)),
                  (55, (17, 30)), (57.5, (16, 30))]),
            (50, [(40, (19, 40)), (42.5, (19, 38)), (45, (19, 36)), (47.5, (19, 35)), (50, (19, 34)), (52.5, (19, 32)),
                   (55, (18, 31)), (57.5, (17, 31))]),
            (52.5, [(40, (20, 40)), (42.5, (20, 38)), (45, (20, 36)), (47.5, (20, 36)), (50, (20, 34)), (52.5, (20, 32)),
                   (55, (18, 32)), (57.5, (17, 32))]),
            (55, [(40, (21, 42)), (42.5, (21, 40)), (45, (21, 38)), (47.5, (21, 36)), (50, (20, 35)), (52.5, (20, 32)),
                   (55, (19, 32)), (57.5, (18, 32))]),
            (57.5, [(40, (22, 45)), (42.5, (22, 42)), (45, (22, 40)), (47.5, (22, 38)), (50, (22, 35)), (52.5, (22, 32)),
                   (55, (20, 32)), (57.5, (19, 32))]),
            (60, [(40, (23, 46)), (42.5, (23, 45)), (45, (23, 42)), (47.5, (23, 40)), (50, (23, 38)), (52.5, (23, 35)),
                   (55, (22, 34)), (57.5, (21, 34))])
        ]

        # Find the closest offense and defense ranges
        closest_offense = min(ranges, key=lambda x: abs(x[0] - offense))
        closest_defense = min(closest_offense[1], key=lambda x: abs(x[0] - defense))

        # Extract the min and max SOG values
        sog_min, sog_max = closest_defense[1]

        # Apply home-ice advantage: If home team, increase SOG range slightly
        if home_team:
            sog_min += 2  # Slight boost for the home team
            sog_max += 2  # Slight boost for the home team

        jitter_min = sog_min + random.randint(-2, 2)  # Adjust these jitter ranges as needed
        jitter_max = sog_max + random.randint(-2, 2)

        # Make sure jitter doesn't push values outside reasonable limits
        jitter_min = max(10, jitter_min)
        jitter_max = max(jitter_min, jitter_max)

        # Generate the SOG with the adjusted random range
        sog = random.randint(jitter_min, jitter_max)

        return sog

    def __get_goals(self, sog, goalie_rating, team):
        goals = 0
        for _ in range(sog):
            probability = self.get_goal_probability(goalie_rating)
            if random.random() <= probability:
                # self.assign_goal(team)
                goals += 1
        return goals

    @staticmethod
    def get_goal_probability(goalie_rating):
        threshold = 20  # Example threshold, adjust as needed
        if goalie_rating <= threshold:
            return 0.130
        elif goalie_rating > threshold and goalie_rating <= 30:
            return 0.120
        elif goalie_rating > 30 and goalie_rating <= 40:
            return 0.110
        elif goalie_rating > 40 and goalie_rating <= 45:
            return 0.105
        elif goalie_rating > 45 and goalie_rating <= 50:
            return 0.102
        elif goalie_rating > 50 and goalie_rating <= 55:
            return 0.100
        elif goalie_rating > 55 and goalie_rating <= 60:
            return 0.095
        elif goalie_rating > 60 and goalie_rating <= 70:
            return 0.090
        elif goalie_rating > 70 and goalie_rating <= 80:
            return 0.085

    def __get_winner(self):
        team1_goals = self.home_goals
        team2_goals = self.visitor_goals
        regulation = True  # By default, assume regulation unless overtime is triggered

        # Check for a tie to enter overtime
        if team1_goals == team2_goals:
            regulation = False  # Game went to overtime
            # Simulate overtime/shootout until a winner is determined
            while team1_goals == team2_goals:
                # Simulate overtime shot on goal for both teams
                home_sog = 1  # Assuming 1 shot per team in each OT loop
                visitor_sog = 1

                # Home team attempt in OT
                home_goals = self.__get_goals(home_sog, self.visitor_goalie.rating,
                                              self.home)  # Updated goalie rating access
                if home_goals > 0:
                    team1_goals += home_goals
                    # Assigning the goal and assists properly
                    # self.assign_goal(self.home)
                    break  # Home team wins, end OT

                # Away team attempt in OT
                visitor_goals = self.__get_goals(visitor_sog, self.home_goalie.rating,
                                                 self.visitor)  # Updated goalie rating access
                if visitor_goals > 0:
                    team2_goals += visitor_goals
                    # Assigning the goal and assists properly
                    # self.assign_goal(self.visitor)
                    break  # Away team wins, end OT

        # Determine winner based on final goals
        if team1_goals > team2_goals:
            self.home_goals = team1_goals  # Update final home team goals
            self.visitor_goals = team2_goals  # Update final away team goals
            return self.home, regulation  # Home team wins, return regulation status
        else:
            self.home_goals = team1_goals  # Update final home team goals
            self.visitor_goals = team2_goals  # Update final away team goals
            return self.visitor, regulation  # Away team wins, return regulation status