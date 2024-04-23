import random

HomeWins = 0
HomeLosses = 0
HomePoints = 0
AwayWins = 0
AwayLosses = 0
AwayPoints = 0
Ties = 0
TotalHomeGoals = 0
TotalAwayGoals = 0
HomeTeam = input("Enter The Home Team")
AwayTeam = input("Enter The Away Team")
HomeOffense = int(input("Enter Home Offense Rating on 20-80 scale"))
AwayOffense = int(input("Enter Away Offense Rating on 20-80 scale"))
Games = int(input("Enter Amount of Games You'd Like to Simulate"))

for i in range(Games):
    HomeShots = 0
    HomeGoals = 0
    HomeSaves = 0
    AwayShots = 0
    AwayGoals = 0
    AwaySaves = 0

    # Shots on goal generated randomly
    hSog = random.randint(15, 50)
    HomeShots += hSog

    aSog = random.randint(15, 50)
    AwayShots += aSog

    # Home Shooting% logic set here
    if HomeOffense <= 20:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 68:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 30 & HomeOffense > 20:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 76:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 40 & HomeOffense > 30:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 83:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 50 & HomeOffense > 40:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 86:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 60 & HomeOffense > 50:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 89:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 70 & HomeOffense > 60:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 93:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1
    elif HomeOffense <= 80 & HomeOffense > 70:
        for i in range(HomeShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 105:
                HomeGoals += 1
                TotalHomeGoals += 1
            else:
                HomeSaves += 1

    # Away Shooting% logic set here
    if AwayOffense <= 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 68:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 30 & AwayOffense > 20:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 76:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 40 & AwayOffense > 30:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 83:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 50 & AwayOffense > 40:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 86:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 60 & AwayOffense > 50:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 89:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 70 & AwayOffense > 60:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 93:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    elif AwayOffense <= 80 & AwayOffense > 70:
        for i in range(AwayShots):
            Goals = random.randrange(1, 1000)
            if Goals <= 105:
                AwayGoals += 1
                TotalAwayGoals += 1
            else:
                AwaySaves += 1
    print(HomeTeam, "Shots:", HomeShots, "Goals:", HomeGoals, AwayTeam, "Shots:", AwayShots, "Goals:", AwayGoals)
    # Wins and Losses tracked here
    if AwayGoals > HomeGoals:
        AwayWins += 1
        HomeLosses += 1
        AwayPoints += 2
    elif HomeGoals > AwayGoals:
        HomeWins += 1
        AwayLosses += 1
        HomePoints += 2
    else:
        Ties += 1
        HomePoints += 1
        AwayPoints += 1

print(HomeTeam, "Wins:", HomeWins, "Losses:", HomeLosses, "Ties:", Ties, "Points:", HomePoints)
print(HomeTeam,"Total Goals:", TotalHomeGoals)
print(AwayTeam, "Wins:", AwayWins, "Losses:", AwayLosses, "Ties:", Ties, "Points:", AwayPoints)
print(AwayTeam, "Total Goals:", TotalAwayGoals)
