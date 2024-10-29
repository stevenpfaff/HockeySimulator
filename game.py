import random
from skater import Skater
import csv

class Game:
    def __init__(self, home_team, away_team, home_goalie, away_goalie):
        self.home = home_team
        self.visitor = away_team
        self.home_goalie = home_goalie
        self.visitor_goalie = away_goalie
        self.home_sog = self.__get_sog(self.home.offense, self.visitor.defense)
        self.visitor_sog = self.__get_sog(self.visitor.offense, self.home.defense)
        self.home_goals = self.__get_goals(self.home_sog, self.visitor_goalie.rating, self.home)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.home_goalie.rating, self.visitor)
        self.winner, self.regulation = self.__get_winner()

    @staticmethod
    def find_closest_value(value, keys):
        return min(keys, key=lambda k: abs(k - value))

    @classmethod
    def __get_sog(cls, offense, defense, home_team=False):
        # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
        ranges = [
            (80, [(80, (15, 38)), (85, (15, 35)), (90, (15, 32)), (95, (15, 30)), (100, (15, 28)), (105, (15, 25)),
                  (110, (14, 25))]),
            (85, [(80, (16, 40)), (85, (16, 38)), (90, (16, 35)), (95, (16, 32)), (100, (16, 30)), (105, (16, 28)),
                  (110, (15, 28))]),
            (90, [(80, (17, 40)), (85, (17, 38)), (90, (17, 35)), (95, (17, 32)), (100, (17, 30)), (105, (17, 28)),
                  (110, (16, 28))]),
            (95, [(80, (18, 40)), (85, (18, 38)), (90, (18, 36)), (95, (18, 35)), (100, (18, 32)), (105, (18, 30)),
                  (110, (17, 30))]),
            (100, [(80, (19, 40)), (85, (19, 38)), (90, (19, 36)), (95, (19, 35)), (100, (19, 34)), (105, (19, 32)),
                   (110, (18, 31))]),
            (102, [(80, (20, 40)), (85, (20, 38)), (90, (20, 36)), (95, (20, 36)), (100, (20, 34)), (105, (20, 32)),
                   (110, (18, 32))]),
            (105, [(80, (21, 42)), (85, (21, 40)), (90, (21, 38)), (95, (21, 36)), (100, (20, 35)), (105, (20, 32)),
                   (110, (19, 32))]),
            (107, [(80, (22, 45)), (85, (22, 42)), (90, (22, 40)), (95, (22, 38)), (100, (22, 35)), (105, (22, 32)),
                   (110, (20, 32))]),
            (110, [(80, (23, 46)), (85, (23, 45)), (90, (23, 42)), (95, (23, 40)), (100, (23, 38)), (105, (23, 35)),
                   (110, (22, 34))]),
            (115, [(80, (24, 48)), (85, (24, 46)), (90, (24, 45)), (95, (24, 42)), (100, (24, 40)), (105, (24, 38)),
                   (110, (23, 35))])
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

        # Generate the random SOG value within the adjusted range
        sog = random.randint(sog_min, sog_max)

        return sog

        def get_random_value(offense_val, defense_val):
            for o_max, defense_ranges in ranges:
                if offense_val <= o_max:
                    for d_threshold, value_range in defense_ranges:
                        if defense_val <= d_threshold:
                            return random.randint(*value_range)
            return 0

        return get_random_value(offense, defense)

    def __get_goals(self, sog, goalie_rating, team):
        goals = 0
        for _ in range(sog):
            probability = self.get_goal_probability(goalie_rating)
            if random.random() <= probability:
                # self.assign_goal(team)
                goals += 1
        return goals

    # def assign_goal(self, team):
    #     # Create a weighted list based on shooting and offense for the goal scorer
    #     shooters = [player for player in team.players]
    #
    #     # Define separate role weights for goals and assists
    #     goal_role_weights = {
    #         "1st Line": 2.0,
    #         "2nd Line": 1.5,
    #         "3rd Line": 1.0,
    #         "4th Line": 0.8,
    #         "Number 1": 1.0,
    #         "Top Pair": 0.6,
    #         "2nd Pair": 0.4,
    #         "3rd Pair": 0.2,
    #         "bench": 0.1
    #     }
    #
    #     assist_role_weights = {
    #         "1st Line": 2.5,
    #         "2nd Line": 2.0,
    #         "3rd Line": 1.5,
    #         "4th Line": 1.0,
    #         "Number 1": 2,
    #         "Top Pair": 1.5,
    #         "2nd Pair": 1.2,
    #         "3rd Pair": 0.8,
    #         "bench": 0.2
    #     }
    #
    #     # Shooter weights for goal scoring
    #     shooter_weights = [(player.shooting * 10 + player.offense * 0.3) * 10 * goal_role_weights.get(player.role, 1.0)
    #                        for player in shooters]
    #
    #     # Randomly select the goal scorer based on weighted shooting and offense
    #     scorer = random.choices(shooters, weights=shooter_weights, k=1)[0]
    #
    #     # Determine how many assists (0, 1, or 2)
    #     assist_count = random.choices([0, 1, 2], weights=[0.05, 0.25, 0.7], k=1)[
    #         0]  # Adjusted weights for more realistic distribution
    #
    #     if assist_count == 0:
    #         # Unassisted goal
    #         scorer.update_stats(goals=1)  # Increment only the scorer's goals
    #     elif assist_count == 1:
    #         # Single-assist goal
    #         passers = [player for player in team.players if player != scorer]
    #         passer_weights = [(player.passing * 10 + player.offense * 1.5) * assist_role_weights.get(player.role, 1.0)
    #                           for player in passers]
    #         assist1 = random.choices(passers, weights=passer_weights, k=1)[0]
    #
    #         # Update stats
    #         scorer.update_stats(goals=1)
    #         assist1.update_stats(assists=1)
    #     else:
    #         # Two-assist goal
    #         passers = [player for player in team.players if player != scorer]
    #         passer_weights = [(player.passing * 10 + player.offense * 1.5) * assist_role_weights.get(player.role, 1.0)
    #                           for player in passers]
    #
    #         assist1 = random.choices(passers, weights=passer_weights, k=1)[0]
    #         passers.remove(assist1)  # Remove assist1 to avoid duplication
    #         passer_weights = [(player.passing * 10 + player.offense * 1.5) * assist_role_weights.get(player.role, 1.0)
    #                           for player in passers]
    #
    #         assist2 = random.choices(passers, weights=passer_weights, k=1)[0]
    #
    #         # Update stats
    #         scorer.update_stats(goals=1)
    #         assist1.update_stats(assists=1)
    #         assist2.update_stats(assists=1)

    @staticmethod
    def get_goal_probability(goalie_rating):
        threshold = 20  # Example threshold, adjust as needed
        if goalie_rating <= threshold:
            return 0.140
        elif goalie_rating > threshold and goalie_rating <= 30:
            return 0.130
        elif goalie_rating > 30 and goalie_rating <= 40:
            return 0.120
        elif goalie_rating > 40 and goalie_rating <= 45:
            return 0.110
        elif goalie_rating > 45 and goalie_rating <= 50:
            return 0.105
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