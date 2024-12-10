import random
import math

class Game:
    def __init__(self, home_team, away_team, home_goalie, visitor_goalie):
        self.home = home_team
        self.visitor = away_team
        self.home_goalie = home_goalie
        self.visitor_goalie = visitor_goalie

        # Initialize SOG, goals, penalties, etc.
        self.home_sog = self.__get_sog(self.home.offense, self.visitor.defense,
                                       home_team=True)
        self.visitor_sog = self.__get_sog(self.visitor.offense, self.home.defense,
                                          home_team=False)

        self.home_goals = self.__get_goals(self.home_sog, self.visitor_goalie.rating, self.home)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.home_goalie.rating, self.visitor)

        # Simulate penalties and adjust powerplay goals
        self.home_penalties = self.__get_penalties(self.home.penalty)
        self.visitor_penalties = self.__get_penalties(self.visitor.penalty)

        self.home_goals += self.__get_powerplay_goals(self.home.powerplay, self.visitor.penaltykill,
                                                      self.visitor_penalties)
        self.visitor_goals += self.__get_powerplay_goals(self.visitor.powerplay, self.home.penaltykill,
                                                         self.home_penalties)

        self.winner, self.regulation = self.__get_winner()

    @classmethod
    def __lookup_scoring_chance(cls, powerplay, penaltykill):
        """Lookup scoring chance from the powerplay and penaltykill rating ranges."""
        # Dictionary mapping powerplay ratings to penalty kill ratings with corresponding scoring chances
        ranges = [
            (41,
             [(40, 0.20), (44, 0.18), (48, 0.16),  (52, 0.14), (60, 0.12)]),
            (46,
             [(40, 0.22), (44, 0.20), (48, 0.18), (52, 0.16), (60, 0.14)]),
            (51,
             [(40, 0.24), (44, 0.22), (48, 0.20), (52, 0.18), (60, 0.16)]),
            (56,
             [(40, 0.26), (44, 0.24), (48, 0.22), (52, 0.20), (60, 0.18)]),
            (61,
             [(40, 0.28), (44, 0.26), (48, 0.24), (52, 0.22), (60, 0.20)]),
        ]

        # Find closest powerplay and penaltykill scoring chance
        closest_powerplay = min(ranges, key=lambda x: abs(x[0] - powerplay))
        closest_penaltykill = min(closest_powerplay[1], key=lambda x: abs(x[0] - penaltykill))

        return closest_penaltykill[1]

    def __get_sog(self, offense_rating, defense_rating, home_team=False):
        """Calculate SOG using offense and defense ratings with home-ice boost and added randomness."""
        base_sog = 30  # Base SOG, close to league average

        # Calculate offense factor
        offense_factor = (offense_rating - 50) * 0.4

        # Calculate defense factor
        if defense_rating > 50:
            defense_factor = (50 - defense_rating) * 0.4
            defense_factor *= math.sqrt(defense_rating / 50)
            if defense_rating > 55:
                defense_factor *= 0.45
        else:
            defense_factor = (50 - defense_rating) * 0.5
            defense_factor = min(defense_factor, 5)

        sog = base_sog + offense_factor + defense_factor

        # Apply a 2% boost for home team
        if home_team:
            sog *= 1.02

        # Add random variation using a normal distribution
        # Mean is 0, standard deviation is 3 (tweak as needed)
        random_variation = random.gauss(0, 8)
        sog += random_variation

        # Clamp within a reasonable range (e.g., 18-50)
        sog = max(18, min(int(sog), 50))

        return sog

    def __get_goals(self, sog, goalie_rating, team):
        goals = 0
        for _ in range(sog):
            probability = self.get_goal_probability(goalie_rating)
            if random.random() <= probability:
                goals += 1
        return goals

    def __get_penalties(self, penalty_rating):
        """ Determine penalties based on team’s penalty rating. """
        target_penalties_per_game = 3
        expected_penalties = (100 - penalty_rating) / 100 * target_penalties_per_game
        penalties = 0

        for _ in range(int(expected_penalties)):
            if random.random() <= expected_penalties / target_penalties_per_game:
                penalties += 1
        return penalties

    def __get_powerplay_goals(self, powerplay_rating, penaltykill_rating, num_powerplays):
        """ Simulate powerplay goals based on powerplay and penalty kill ratings. """
        scoring_chance = self.__lookup_scoring_chance(powerplay_rating, penaltykill_rating)
        goals = 0
        for _ in range(num_powerplays):
            if random.random() <= scoring_chance:
                goals += 1
        return goals

    @staticmethod
    def get_goal_probability(goalie_rating):
        """ Probability of scoring based on goalie rating """
        return max(0.0825, 0.1333 - 0.00078 * goalie_rating)

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