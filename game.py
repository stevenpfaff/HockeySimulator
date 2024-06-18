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
            (20, [(20, (15, 35)), (30, (15, 32)), (40, (15, 30)), (50, (15, 28)), (60, (15, 25)), (70, (15, 22)),
                  (80, (12, 20))]),
            (30, [(20, (16, 38)), (30, (16, 35)), (40, (16, 33)), (50, (16, 31)), (60, (16, 28)), (70, (16, 25)),
                  (80, (13, 23))]),
            (40, [(20, (17, 41)), (30, (17, 38)), (40, (17, 36)), (50, (17, 34)), (60, (17, 31)), (70, (17, 28)),
                  (80, (14, 26))]),
            (50, [(20, (18, 44)), (30, (18, 41)), (40, (18, 39)), (50, (18, 37)), (60, (18, 34)), (70, (18, 31)),
                  (80, (15, 29))]),
            (60, [(20, (20, 47)), (30, (20, 44)), (40, (20, 42)), (50, (20, 40)), (60, (19, 37)), (70, (19, 34)),
                  (80, (16, 32))]),
            (70, [(20, (22, 50)), (30, (22, 47)), (40, (22, 45)), (50, (22, 43)), (60, (20, 40)), (70, (20, 37)),
                  (80, (18, 35))]),
            (80, [(20, (25, 53)), (30, (25, 50)), (40, (25, 48)), (50, (25, 46)), (60, (22, 43)), (70, (22, 40)),
                  (80, (20, 38))]),
        ]

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
            return 0.120
        elif goalie_rating > threshold and goalie_rating <= 30:
            return 0.110
        elif goalie_rating > 30 and goalie_rating <= 40:
            return 0.105
        elif goalie_rating > 40 and goalie_rating <= 50:
            return 0.102
        elif goalie_rating > 50 and goalie_rating <= 60:
            return 0.100
        elif goalie_rating > 60 and goalie_rating <= 70:
            return 0.09
        elif goalie_rating > 70 and goalie_rating <= 80:
            return 0.08

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
