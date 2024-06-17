import random

class Game(object):
    def __init__(self, home, visitor, home_goalie=None, visitor_goalie=None):
        self.home = home
        self.visitor = visitor
        self.home_goalie = home_goalie if home_goalie else home.starting_goalie
        self.visitor_goalie = visitor_goalie if visitor_goalie else visitor.starting_goalie
        self.home_sog = self.__get_sog(home, visitor)
        self.visitor_sog = self.__get_sog(visitor, home)
        self.home_goals = self.__get_goals(self.home_sog, self.home_goalie)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.visitor_goalie)
        self.winner, self.regulation = self.__get_winner(self.home, self.visitor, self.home_goals, self.visitor_goals,
                                                         self.home_sog, self.visitor_sog)

    @classmethod
    def __get_sog(cls, offense, defense):
        ranges = [
            (20, 20, [(15, 35), (15, 32), (15, 30), (15, 28), (15, 25), (15, 22), (12, 20)]),
            (30, 20, [(16, 38), (16, 35), (16, 33), (16, 31), (16, 28), (16, 25), (13, 23)]),
            (40, 20, [(17, 41), (17, 38), (17, 36), (17, 34), (17, 31), (17, 28), (14, 26)]),
            (50, 20, [(18, 44), (18, 41), (18, 39), (18, 37), (18, 34), (18, 31), (15, 29)]),
            (60, 20, [(20, 47), (20, 44), (20, 42), (20, 40), (19, 37), (19, 34), (16, 32)]),
            (70, 20, [(22, 50), (22, 47), (22, 45), (22, 43), (20, 40), (20, 37), (18, 35)]),
            (80, 20, [(25, 53), (25, 50), (25, 48), (25, 46), (22, 43), (22, 40), (20, 38)]),
        ]

        def get_random_value(offense_val, defense_val):
            for o_max, d_max, value_ranges in ranges:
                if offense_val <= o_max:
                    for d_threshold, value_range in zip(range(20, 81, 10), value_ranges):
                        if defense_val <= d_threshold:
                            return random.randint(*value_range)
            return 0

        return get_random_value(offense.offense, defense.defense)

    @classmethod
    def __get_goals(cls, sog, starting_goalie):
        goalie_probs = {
            20: 0.075,
            30: 0.085,
            40: 0.095,
            50: 0.100,
            60: 0.110,
            70: 0.120,
            80: 0.125
        }

        def get_goal_probability(goalie_rating):
            for threshold, prob in goalie_probs.items():
                if goalie_rating <= threshold:
                    return prob
            return 0

        probability = get_goal_probability(starting_goalie)
        # print(f"Starting goalie rating: {starting_goalie}, Probability: {probability}")

        goals = sum(1 for _ in range(sog) if random.random() <= probability)
        # print(f"Number of goals scored: {goals}")

        return goals

    @classmethod
    def __get_winner(self, team1, team2, team1_goals, team2_goals, team1_sog, team2_sog):
        regulation = True

        # Simulate overtime until a winner is determined
        while team1_goals == team2_goals:
            regulation = False
            # Simulate additional goals
            goal1 = random.random()
            goal2 = random.random()
            if goal1 > goal2:
                team1_goals += 1
                team1_sog += 1
            elif goal2 > goal1:
                team2_goals += 1
                team2_sog += 1

        if team1_goals > team2_goals:
            return team1, regulation
        else:
            return team2, regulation
