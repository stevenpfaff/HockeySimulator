import random

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

    @classmethod
    def __get_sog(cls, offense, defense):
        # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
        ranges = [
            (80, [(80, (15, 35)), (90, (15, 32)), (95, (15, 30)), (100, (15, 28)), (105, (15, 25)), (115, (15, 22))]),
            (90, [(80, (16, 38)), (90, (16, 35)), (95, (16, 33)), (100, (16, 31)), (105, (16, 28)), (115, (16, 25))]),
            (95, [(80, (17, 41)), (90, (17, 38)), (95, (17, 36)), (100, (17, 34)), (105, (17, 31)), (115, (17, 28))]),
            (100, [(80, (18, 44)), (90, (18, 41)), (95, (18, 39)), (100, (18, 37)), (105, (18, 34)), (115, (18, 31))]),
            (105, [(80, (20, 47)), (90, (20, 44)), (95, (20, 42)), (100, (20, 40)), (105, (19, 37)), (115, (19, 34))]),
            (115, [(80, (22, 50)), (90, (22, 47)), (95, (22, 45)), (100, (22, 43)), (105, (20, 40)), (115, (20, 37))]),
        ]
    # @classmethod
    # def __get_sog(cls, offense, defense):
    #     # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
    #     ranges = [
    #         (40, [(40, (15, 35)), (45, (15, 32)), (50, (15, 30)), (55, (15, 28)), (60, (15, 25)), (65, (15, 22))]),
    #         (45, [(40, (16, 38)), (45, (16, 35)), (50, (16, 33)), (55, (16, 31)), (60, (16, 28)), (65, (16, 25))]),
    #         (50, [(40, (17, 41)), (45, (17, 38)), (50, (17, 36)), (55, (17, 34)), (60, (17, 31)), (65, (17, 28))]),
    #         (55, [(40, (18, 44)), (45, (18, 41)), (50, (18, 39)), (55, (18, 37)), (60, (18, 34)), (65, (18, 31))]),
    #         (60, [(40, (20, 47)), (45, (20, 44)), (50, (20, 42)), (55, (20, 40)), (60, (19, 37)), (65, (19, 34))]),
    #         (65, [(40, (22, 50)), (45, (22, 47)), (50, (22, 45)), (55, (22, 43)), (60, (20, 40)), (65, (20, 37))]),
    #     ]

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
        elif goalie_rating > 40 and goalie_rating <= 50:
            return 0.100
        elif goalie_rating > 50 and goalie_rating <= 60:
            return 0.095
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
