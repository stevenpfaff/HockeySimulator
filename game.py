import random
from skater import forwards

class Game:
    def __init__(self, home_team, away_team, home_goalie, away_goalie):
        self.home = home_team
        self.visitor = away_team
        self.home_goalie = home_goalie
        self.visitor_goalie = away_goalie
        self.home_sog = self.__get_sog(self.home.offense, self.visitor.defense)
        self.visitor_sog = self.__get_sog(self.visitor.offense, self.home.defense)
        self.home_goals = self.__get_goals(self.home_sog, self.visitor_goalie.rating)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.home_goalie.rating)
        self.winner, self.regulation = self.__get_winner()

    @staticmethod
    def find_closest_value(value, keys):
        return min(keys, key=lambda k: abs(k - value))
    @classmethod
    def __get_sog(cls, offense, defense):
        # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
        ranges = [
            (80, [(80, (15, 38)), (85, (15, 35)), (90, (15, 32)), (95, (15, 30)), (100, (15, 28)), (105, (15, 25)), (110, (15, 22))]),
            (85, [(80, (16, 40)), (85, (16, 38)), (90, (16, 35)), (95, (16, 32)), (100, (16, 30)), (105, (16, 28)), (110, (16, 25))]),
            (90, [(80, (17, 40)), (85, (17, 38)), (90, (17, 35)), (95, (17, 32)), (100, (17, 30)), (105, (17, 28)), (110, (17, 25))]),
            (95, [(80, (18, 40)), (85, (18, 38)), (90, (18, 36)), (95, (18, 35)), (100, (18, 32)), (105, (18, 30)), (110, (18, 28))]),
            (100, [(80, (19, 40)), (85, (19, 38)), (90, (19, 36)), (95, (19, 35)), (100, (19, 34)), (105, (19, 32)), (110, (19, 30))]),
            (105, [(80, (20, 42)), (85, (20, 40)), (90, (20, 38)), (95, (20, 36)), (100, (20, 35)), (105, (20, 32)), (110, (20, 30))]),
            (110, [(80, (22, 45)), (85, (22, 42)), (90, (22, 40)), (95, (22, 38)), (100, (22, 35)), (105, (22, 32)), (110, (22, 30))]),
            (115, [(80, (25, 48)), (85, (25, 45)), (90, (25, 42)), (95, (25, 40)), (100, (25, 38)), (105, (25, 35)),(110, (25, 32))]),
        # , (115, (20, 28)), (115, (19, 28)), (115, (18, 28)), (115, (17, 25)), (115, (16, 23)), (115, (15, 23)),  (115, (13, 20)), (115, (21, 30))
        ]

        closest_offense = min(ranges, key=lambda x: abs(x[0] - offense))
        closest_defense = min(closest_offense[1], key=lambda x: abs(x[0] - defense))

        sog_min, sog_max = closest_defense[1]
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

    def __get_goals(self, sog, goalie_rating):
        goals = 0
        for _ in range(sog):
            probability = self.get_goal_probability(goalie_rating)
            if random.random() <= probability:
                goals += 1
        return goals


    @staticmethod
    def get_goal_probability(goalie_rating):
        threshold = 20  # Example threshold, adjust as needed
        if goalie_rating <= threshold:
            return 0.115
        elif goalie_rating > threshold and goalie_rating <= 30:
            return 0.110
        elif goalie_rating > 30 and goalie_rating <= 40:
            return 0.105
        elif goalie_rating > 40 and goalie_rating <= 45:
            return 0.100
        elif goalie_rating > 45 and goalie_rating <= 50:
            return 0.097
        elif goalie_rating > 50 and goalie_rating <= 55:
            return 0.095
        elif goalie_rating > 55 and goalie_rating <= 60:
            return 0.092
        elif goalie_rating > 60 and goalie_rating <= 70:
            return 0.090
        elif goalie_rating > 70 and goalie_rating <= 80:
            return 0.085

    def __get_winner(self):
        team1_goals = self.home_goals
        team2_goals = self.visitor_goals
        regulation = True

        if team1_goals == team2_goals:
            regulation = False
            # Simulate overtime until a winner is determined
            while team1_goals == team2_goals:
                goal1 = random.random()
                goal2 = random.random()
                if goal1 > goal2:
                    team1_goals += 1
                elif goal2 > goal1:
                    team2_goals += 1

        if team1_goals > team2_goals:
            return self.home, regulation
        else:
            return self.visitor, regulation
