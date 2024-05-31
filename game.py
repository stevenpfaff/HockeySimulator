import random

class Game(object):
    def __init__(self, home, visitor):
        self.home = home
        self.visitor = visitor
        self.home_sog = self.__get_sog(home, visitor)
        self.visitor_sog = self.__get_sog(visitor, home)
        self.home_goals = self.__get_goals(visitor, self.home_sog)
        self.visitor_goals = self.__get_goals(home, self.visitor_sog)
        self.winner, self.regulation = self.__get_winner(self.home_goals, self.visitor_goals, self.home_sog, self.visitor_sog)

    @classmethod
    def __get_sog(self, offense, defense):
        if offense.offense <= 20 and defense.defense <= 20:
            return random.randint(18, 35)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 20:
            return random.randint(20, 35)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 20:
            return random.randint(22, 38)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 20:
            return random.randint(25, 40)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 20:
            return random.randint(28, 42)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 20:
            return random.randint(28, 45)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 20:
            return random.randint(30, 50)

        # 30-21 Defense Team 2
        elif offense.offense <= 20 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(15, 32)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(18, 32)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(18, 35)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(20, 35)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(25, 38)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(28, 42)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 30 & defense.defense > 20:
            return random.randint(30, 50)

        # 40-31 Defense Team 2
        elif offense.offense <= 20 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(13, 28)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(15, 30)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(15, 32)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(18, 35)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(22, 38)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(25, 40)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 40 & defense.defense > 30:
            return random.randint(28, 48)


        # 50-41 Defense Team 2
        elif offense.offense <= 20 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(13, 25)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(13, 28)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(15, 30)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(18, 32)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(22, 35)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(25, 40)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 50 & defense.defense > 40:
            return random.randint(25, 40)


        # 60-51 Defense Team 2
        elif offense.offense <= 20 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(13, 22)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(13, 25)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(15, 28)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(18, 30)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(22, 32)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(25, 35)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 60 & defense.defense > 50:
            return random.randint(25, 45)


        # 70-61 Defense Team 2
        elif offense.offense <= 20 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(13, 20)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(13, 22)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(15, 25)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(17, 30)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(20, 32)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(22, 35)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 70 & defense.defense > 60:
            return random.randint(25, 40)


        # 80-71 Defense
        elif offense.offense <= 20 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(10, 20)

        elif offense.offense <= 30 & offense.offense > 20 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(13, 22)

        elif offense.offense <= 40 & offense.offense > 30 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(15, 22)

        elif offense.offense <= 50 & offense.offense > 40 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(17, 25)

        elif offense.offense <= 60 & offense.offense > 50 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(20, 28)

        elif offense.offense <= 70 & offense.offense > 60 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(22, 30)

        elif offense.offense <= 80 & offense.offense > 70 and defense.defense <= 80 & defense.defense > 70:
            return random.randint(22, 30)

        return 0

    @classmethod
    def __get_goals(self, defense, sog):
        goals = 0
        for i in range(sog):
            if defense.goalie <= 20:
                if random.random() <= 0.115:
                    goals += 1

            elif defense.goalie <= 30 & defense.goalie > 20:
                if random.random() <= 0.110:
                    goals += 1

            elif defense.goalie <= 40 & defense.goalie > 30:
                if random.random() <= 0.105:
                    goals += 1

            elif defense.goalie <= 50 & defense.goalie > 40:
                if random.random() <= 0.102:
                    goals += 1

            elif defense.goalie <= 60 & defense.goalie > 50:
                if random.random() <= 0.100:
                    goals += 1

            elif defense.goalie <= 70 & defense.goalie > 60:
                if random.random() <= 0.090:
                    goals += 1

            elif defense.goalie <= 80 & defense.goalie > 70:
                if random.random() <= 0.085:
                    goals += 1

        return goals

    @classmethod
    def __get_winner(self, team1_goals, team2_goals, team1_sog, team2_sog):
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
            return "team1", regulation
        else:
            return "team2", regulation