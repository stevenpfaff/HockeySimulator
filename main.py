import random
from team import league

HomeWins = 0
HomeLosses = 0
HomeOtLosses = 0
HomePoints = 0
AwayWins = 0
AwayLosses = 0
AwayOtLosses = 0
AwayPoints = 0
TotalHomeGoals = 0
TotalAwayGoals = 0
HomeTeam = input("Enter The Home Team")
AwayTeam = input("Enter The Away Team")
HomeOffense = int(input("Enter Home Offense Rating on 20-80 scale"))
HomeDefense = int(input("Enter Home Defense Rating on 20-80 scale"))
HomeGoalie = int(input("Enter Home Goalie Rating on 20-80 scale"))
AwayOffense = int(input("Enter Away Offense Rating on 20-80 scale"))
AwayDefense = int(input("Enter Away Defense Rating on 20-80 scale"))
AwayGoalie = int(input("Enter Away Goalie Rating on 20-80 scale"))
Games = int(input("Enter Amount of Games You'd Like to Simulate"))

for i in range(Games):
    HomeShots = 0
    HomeGoals = 0
    HomeSaves = 0
    AwayShots = 0
    AwayGoals = 0
    AwaySaves = 0

    #Shots on goal logic here
    #30-20 Defense
    if HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(15, 32)
        HomeShots += aSog

    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(18, 35)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(20, 35)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(22, 35)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(25, 38)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(28, 42)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 30 & AwayDefense >= 20:
        aSog = random.randint(30, 50)
        HomeShots += aSog
    #40-31 Defense
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(13, 30)
        HomeShots += aSog
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(15, 32)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(18, 35)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(22, 38)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(25, 40)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 40 & AwayDefense > 30:
        aSog = random.randint(28, 48)
        HomeShots += aSog
    #50-41 Defense
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(13, 28)
        HomeShots += aSog
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(15, 30)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(18, 32)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(22, 35)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(25, 40)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 50 & AwayDefense > 40:
        aSog = random.randint(28, 45)
        HomeShots += aSog
    #60-51 Defense
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(13, 25)
        HomeShots += aSog
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(15, 28)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(18, 30)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(22, 32)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(25, 35)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 60 & AwayDefense > 50:
        aSog = random.randint(25, 45)
        HomeShots += aSog
    #70-61 Defense
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(13, 22)
        HomeShots += aSog
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(15, 25)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(17, 30)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(20, 30)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(22, 35)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 70 & AwayDefense > 60:
        aSog = random.randint(25, 42)
        HomeShots += aSog
    #80-71 Defense
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(13, 20)
        HomeShots += aSog
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(15, 22)
        HomeShots += aSog
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(17, 25)
        HomeShots += aSog
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(20, 28)
        HomeShots += aSog
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(22, 30)
        HomeShots += aSog
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayDefense <= 80 & AwayDefense > 70:
        aSog = random.randint(25, 35)
        HomeShots += aSog

    #Scoring Logic Here
    #30-20 Goalie
    if HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 75:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 87:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 90:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 95:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 105:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 30 & AwayGoalie >= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 120:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    # 40-31 Goalie
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 72:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 80:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 85:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 93:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 100:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 40 & AwayGoalie > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 115:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    #50-41 Goalie
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 70:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 78:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 85:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 90:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 98:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 50 & AwayGoalie > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 110:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    #60-51 Goalie
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 65:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 70:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 80:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 85:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 90:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 60 & AwayGoalie > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 95:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    #70-61 Goalie
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 60:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 68:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 75:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 82:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 88:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 70 & AwayGoalie > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 95:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    #80-71 Goalie
    elif HomeOffense <= 30 & HomeOffense >= 20 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 55:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 65:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 70:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 78:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 82:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70 and AwayGoalie <= 80 & AwayGoalie > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1,1000)
            if Goals <= 87:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                AwaySaves += 1

    #Away Logic Here
    if AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(15, 32)
        AwayShots += aSog

    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(18, 35)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(20, 35)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(22, 35)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(25, 38)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(28, 42)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 30 & HomeDefense >= 20:
        aSog = random.randint(30, 50)
        AwayShots += aSog
    # 40-31 Defense
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(13, 30)
        AwayShots += aSog
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(15, 32)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(18, 35)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(22, 38)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(25, 40)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 40 & HomeDefense > 30:
        aSog = random.randint(28, 48)
        AwayShots += aSog
    # 50-41 Defense
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(13, 28)
        AwayShots += aSog
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(15, 30)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(18, 32)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(22, 35)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(25, 40)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 50 & HomeDefense > 40:
        aSog = random.randint(28, 45)
        AwayShots += aSog
    # 60-51 Defense
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(13, 25)
        AwayShots += aSog
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(15, 28)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(18, 30)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(22, 32)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(25, 35)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 60 & HomeDefense > 50:
        aSog = random.randint(25, 45)
        AwayShots += aSog
    # 70-61 Defense
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(13, 22)
        AwayShots += aSog
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(15, 25)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(17, 30)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(20, 30)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(22, 35)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 70 & HomeDefense > 60:
        aSog = random.randint(25, 42)
        AwayShots += aSog
    # 80-71 Defense
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(13, 20)
        AwayShots += aSog
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(15, 22)
        AwayShots += aSog
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(17, 25)
        AwayShots += aSog
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(20, 28)
        AwayShots += aSog
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(22, 30)
        AwayShots += aSog
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeDefense <= 80 & HomeDefense > 70:
        aSog = random.randint(25, 35)
        AwayShots += aSog

    # Away Scoring Logic Here
    # 30-20 Goalie
    if AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 75:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 87:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 90:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 95:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 105:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 30 & HomeGoalie >= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    # 40-31 Goalie
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 72:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 80:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 85:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 93:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 100:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 40 & HomeGoalie > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 115:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    # 50-41 Goalie
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 70:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 78:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 85:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 90:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 98:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 50 & HomeGoalie > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 110:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    # 60-51 Goalie
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 65:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 70:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 80:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 85:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 90:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 60 & HomeGoalie > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 95:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    # 70-61 Goalie
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 60:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 68:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 75:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 82:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 88:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 70 & HomeGoalie > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 95:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    # 80-71 Goalie
    elif AwayOffense <= 30 & AwayOffense >= 20 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 55:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 65:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 70:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 78:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 82:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70 and HomeGoalie <= 80 & HomeGoalie > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 87:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                HomeSaves += 1

    #Wins and Losses calculated here
    if AwayGoals > HomeGoals:
        AwayWins += 1
        HomeLosses += 1
        AwayPoints += 2
    elif HomeGoals > AwayGoals:
        HomeWins += 1
        AwayLosses += 1
        HomePoints += 2
    while AwayGoals == HomeGoals:
        print("Overtime!")
        HomePoints += 1
        AwayPoints += 1
        aSog = random.randint(1, 7)
        AwayShots += aSog
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1

        aSog = random.randint(1, 7)
        HomeShots += aSog
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1

        if HomeGoals > AwayGoals:
            HomePoints += 1
            AwayOtLosses += 1
            HomeWins +=1

        elif AwayGoals > HomeGoals:
            AwayPoints += 1
            HomeOtLosses += 1
            AwayWins += 1


    print(HomeTeam, "Shots:", HomeShots, "Goals:", HomeGoals, AwayTeam, "Shots:", AwayShots, "Goals:", AwayGoals)


print(HomeTeam, "Wins:", HomeWins, "Losses:", HomeLosses, "OTL:", HomeOtLosses, "Points:", HomePoints)
print(HomeTeam,"Total Goals:", TotalHomeGoals)
print(AwayTeam, "Wins:", AwayWins, "Losses:", AwayLosses, "OTL:", AwayOtLosses, "Points:", AwayPoints)
print(AwayTeam, "Total Goals:", TotalAwayGoals)
