import random


class Team(object):
    def __init__(self, name, offense, defense, goalie, sog, goals, goals_against, wins, losses, otl, points):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.goalie = goalie
        self.sog = sog
        self.goals = goals
        self.goals_against = goals_against
        self.wins = wins
        self.losses = losses
        self.otl = otl
        self.points = points
    def game(self):
        for i in range(5):
            team1 = tor[0]
            team2 = det[0]
            team1_sog = 0
            team2_sog = 0
            team1_goals = 0
            team2_goals = 0
            team1_saves = 0
            team2_saves = 0
            # Minimum Defense Team 2
            if team1.offense <= 20 and team2.defense <= 20:
                sog = random.randint(18, 35)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 20:
                sog = random.randint(20, 35)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 20:
                sog = random.randint(22, 38)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 20:
                sog = random.randint(25, 40)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 20:
                sog = random.randint(28, 42)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 20:
                sog = random.randint(28, 45)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 20:
                sog = random.randint(30, 50)
                team1_sog += sog

            #30-21 Defense Team 2
            elif team1.offense <= 20 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(15, 32)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(18, 32)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(18, 35)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(20, 35)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(25, 38)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(28, 42)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 30 & team2.defense > 20:
                sog = random.randint(30, 50)
                team1_sog += sog

            #40-31 Defense Team 2
            elif team1.offense <= 20 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(13, 28)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(15, 30)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(15, 32)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(18, 35)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(22, 38)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(25, 40)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 40 & team2.defense > 30:
                sog = random.randint(28, 48)
                team1_sog += sog

            #50-41 Defense Team 2
            elif team1.offense <= 20 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(13, 25)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(13, 28)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(15, 30)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(18, 32)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(22, 35)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(25, 40)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 50 & team2.defense > 40:
                sog = random.randint(25, 40)
                team1_sog += sog

            #60-51 Defense Team 2
            elif team1.offense <= 20 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(13, 22)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(13, 25)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(15, 28)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(18, 30)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(22, 32)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(25, 35)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 60 & team2.defense > 50:
                sog = random.randint(25, 45)
                team1_sog += sog

            #70-61 Defense Team 2
            elif team1.offense <= 20 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(13, 20)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(13, 22)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(15, 25)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(17, 30)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(20, 32)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(22, 35)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 70 & team2.defense > 60:
                sog = random.randint(25, 40)
                team1_sog += sog

            #80-71 Defense
            elif team1.offense <= 20 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(10, 20)
                team1_sog += sog
            elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(13, 22)
                team1_sog += sog
            elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(15, 22)
                team1_sog += sog
            elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(17, 25)
                team1_sog += sog
            elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(20, 28)
                team1_sog += sog
            elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(22, 30)
                team1_sog += sog
            elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 80 & team2.defense > 70:
                sog = random.randint(22, 30)
                team1_sog += sog

            # Minimum Defense Team 1
            if team2.offense <= 20 and team1.defense <= 20:
                sog = random.randint(18, 35)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 20:
                sog = random.randint(20, 35)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 20:
                sog = random.randint(22, 38)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 20:
                sog = random.randint(25, 40)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 20:
                sog = random.randint(28, 42)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 20:
                sog = random.randint(28, 45)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 20:
                sog = random.randint(30, 50)
                team2_sog += sog

            # 30-21 Defense Team 2
            elif team2.offense <= 20 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(15, 32)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(18, 32)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(18, 35)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(20, 35)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(25, 38)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(28, 42)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 30 & team1.defense > 20:
                sog = random.randint(30, 50)
                team2_sog += sog

            # 40-31 Defense Team 2
            elif team2.offense <= 20 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(13, 28)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(15, 30)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(15, 32)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(18, 35)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(22, 38)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(25, 40)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 40 & team1.defense > 30:
                sog = random.randint(28, 48)
                team2_sog += sog

            # 50-41 Defense Team 2
            elif team2.offense <= 20 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(13, 25)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(13, 28)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(15, 30)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(18, 32)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(22, 35)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(25, 40)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 50 & team1.defense > 40:
                sog = random.randint(25, 40)
                team2_sog += sog

            # 60-51 Defense Team 2
            elif team2.offense <= 20 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(13, 22)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(13, 25)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(15, 28)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(18, 30)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(22, 32)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(25, 35)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 60 & team1.defense > 50:
                sog = random.randint(25, 45)
                team2_sog += sog

            # 70-61 Defense Team 2
            elif team2.offense <= 20 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(13, 20)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(13, 22)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(15, 25)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(17, 30)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(20, 32)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(22, 35)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 70 & team1.defense > 60:
                sog = random.randint(25, 40)
                team2_sog += sog

            # 80-71 Defense
            elif team2.offense <= 20 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(10, 20)
                team2_sog += sog
            elif team2.offense <= 30 & team2.offense > 20 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(13, 22)
                team2_sog += sog
            elif team2.offense <= 40 & team2.offense > 30 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(15, 22)
                team2_sog += sog
            elif team2.offense <= 50 & team2.offense > 40 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(17, 25)
                team2_sog += sog
            elif team2.offense <= 60 & team2.offense > 50 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(20, 28)
                team2_sog += sog
            elif team2.offense <= 70 & team2.offense > 60 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(22, 30)
                team2_sog += sog
            elif team2.offense <= 80 & team2.offense > 70 and team1.defense <= 80 & team1.defense > 70:
                sog = random.randint(22, 30)
                team2_sog += sog

            # Minimum Goalie Team 2
            if team2.goalie <= 20:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 125:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            # 30-21 Goalie Team 2
            elif team2.goalie <= 30 & team2.goalie > 20:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 120:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            #40-31 Goalie Team 2
            elif team2.goalie <= 40 & team2.goalie > 30:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 110:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            #50-41 Goalie Team 2
            elif team2.goalie <= 50 & team2.goalie > 40:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 100:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            #60-51 Goalie Team 2
            elif team2.goalie <= 60 & team2.goalie > 50:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 98:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            #70-61 Goalie Team 2
            elif team2.goalie <= 70 & team2.goalie > 60:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 92:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1
            #80-71 Goalie Team 2
            elif team2.goalie <= 80 & team2.goalie > 70:
                for i in range(team1_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 85:
                        team1_goals += 1
                        team1.goals += 1
                        team2.goals_against += 1
                    else:
                        team2_saves += 1

            # Minimum Goalie Team 1
            if team1.goalie <= 20:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 125:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 30-21 Goalie Team 1
            elif team1.goalie <= 30 & team1.goalie > 20:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 120:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 40-31 Goalie Team 1
            elif team1.goalie <= 40 & team1.goalie > 30:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 110:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 50-41 Goalie Team 1
            elif team1.goalie <= 50 & team1.goalie > 40:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 100:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 60-51 Goalie Team 1
            elif team1.goalie <= 60 & team1.goalie > 50:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 98:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 70-61 Goalie Team 1
            elif team1.goalie <= 70 & team1.goalie > 60:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 92:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            # 80-71 Goalie Team 1
            elif team1.goalie <= 80 & team1.goalie > 70:
                for i in range(team2_sog):
                    goals = random.randrange(1, 1000)
                    if goals <= 85:
                        team2_goals += 1
                        team2.goals += 1
                        team1.goals_against += 1
                    else:
                        team1_saves += 1
            print(f"{team1.name}", "Goals:",team1_goals, "Shots:",team1_sog, f"{team2.name}", "Goals:",team2_goals, "Shots:",team2_sog)
            # Wins and Losses Tracked Here
            if team1_goals > team2_goals:
                team1.points += 2
                team1.wins += 1
                team2.losses += 1
            elif team2_goals > team1_goals:
                team2.points += 2
                team2.wins += 1
                team1.losses += 1
            while team1_goals == team2_goals:
                team1.points += 1
                team2.points += 1
                goal = random.randint(1, 2)
                if goal == 1:
                    team1_goals += 1
                    team1.goals += 1
                    team1_sog += 1
                    team2.goals_against += 1
                elif goal == 2:
                    team2_goals += 1
                    team2.goals += 1
                    team2_sog += 1
                    team1.goals_against += 1
                if team1_goals > team2_goals:
                    team1.points += 1
                    team2.otl += 1
                    team1.wins += 1
                elif team2_goals > team1_goals:
                    team2.points += 1
                    team1.otl += 1
                    team2.wins += 1
        print(team1.name,"W:", team1.wins, "L:", team1.losses, "OTL:",team1.otl, "PTS:",team1.points,"G:", team1.goals,"GA:", team1.goals_against)
        print(team2.name,"W:", team2.wins, "L:",team2.losses, "OTL:",team2.otl, "PTS:",team2.points, "G:",team2.goals,"GA:", team2.goals_against)
ana = Team("Anaheim Ducks", 30, 30, 30,0,0,0,0,0,0,0)
ari = Team("Arizona Coyotes", 40, 30, 40,0,0,0,0,0,0,0)
bos = Team("Boston Bruins", 50, 50, 80,0,0,0,0,0,0,0)
buf = Team("Buffalo Sabres", 50, 40, 50,0,0,0,0,0,0, 0),
cgy = Team("Calgary Flames", 40, 50, 40,0,0,0,0,0,0,0),
car = Team("Carolina Hurricanes", 70, 80, 50,0,0,0,0,0,0,0),
chi = Team("Chicago Blackhawks", 20, 30, 40,0,0,0,0,0,0,0),
col = Team("Colorado Avalanche", 70, 40, 40,0,0,0,0,0,0,0),
cbj = Team("Columbus Blue Jackets", 30, 20, 40,0,0,0,0,0,0,0),
dal = Team("Dallas Stars", 60, 70, 60,0,0,0,0,0,0,0),
det = Team("Detroit Red Wings", 40, 40, 50,0,0,0,0,0,0,0),
edm = Team("Edmonton Oilers", 80, 70, 50,0,0,0,0,0,0,0),
fla = Team("Florida Panthers", 80, 70, 80,0,0,0,0,0,0,0),
la = Team("Los Angeles Kings", 60, 70, 70,0,0,0,0,0,0,0),
min = Team("Minnesota Wild", 50, 60, 40,0,0,0,0,0,0,0),
mtl = Team("Montreal Canadiens", 30, 30, 40,0,0,0,0,0,0,0),
nsh = Team("Nashville Predators", 50, 60, 60,0,0,0,0,0,0,0),
nj = Team("New Jersey Devils", 50, 40, 20,0,0,0,0,0,0,0),
nyi = Team("New York Islanders", 40, 50, 60,0,0,0,0,0,0,0),
nyr = Team("New York Rangers", 60, 60, 70,0,0,0,0,0,0,0),
ott = Team("Ottawa Senators", 40, 60, 20,0,0,0,0,0,0,0),
phi = Team("Philadelphia Flyers", 40, 70, 20,0,0,0,0,0,0,0),
pit = Team("Pittsburgh Penguins", 50, 50, 50,0,0,0,0,0,0,0),
sj = Team("San Jose Sharks", 20, 20, 20,0,0,0,0,0,0,0),
sea = Team("Seattle Kraken", 30, 70, 60,0,0,0,0,0,0,0),
stl = Team("St. Louis Blues", 40, 40, 60,0,0,0,0,0,0,0),
tb = Team("Tampa Bay Lightning", 50, 50, 50,0,0,0,0,0,0,0),
tor = Team("Toronto Maple Leafs", 70, 50, 40,0,0,0,0,0,0,0),
van = Team("Vancouver Canucks", 60, 60, 60,0,0,0,0,0,0,0),
vgk = Team("Vegas Golden Knights", 50, 60, 60,0,0,0,0,0,0,0),
wsh = Team("Washington Capitals", 40, 50, 50,0,0,0,0,0,0,0),
wpg = Team("Winnipeg Jets", 50, 60, 80,0,0,0,0,0,0,0)
ana.game()
