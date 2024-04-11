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

for i in range (82):
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

    # Shooting% set to 8.6% here (NHL League Average)
    for i in range(HomeShots):
        Goals = random.randrange(1,1000)
        if Goals <= 86:
            HomeGoals +=1
            TotalHomeGoals +=1
        else:
            HomeSaves +=1
    for i in range(AwayShots):
        Goals = random.randrange(1,1000)
        if Goals <= 86:
            AwayGoals +=1
            TotalAwayGoals+=1
        else:
            AwaySaves +=1

    #Wins and Losses tracked here
    if AwayGoals > HomeGoals:
        AwayWins += 1
        HomeLosses += 1
        AwayPoints +=2
    elif HomeGoals > AwayGoals:
        HomeWins += 1
        AwayLosses += 1
        HomePoints +=2
    else:
        Ties +=1
        HomePoints +=1
        AwayPoints +=1
        
print("Home Wins:", HomeWins, "Home Losses:", HomeLosses, "Ties:", Ties, "Home Points:", HomePoints)
print("Away Wins:", AwayWins, "Away Losses:", AwayLosses, "Ties:", Ties, "Away Points:", AwayPoints)
print("Home Total Goals:", TotalHomeGoals)
print("Away Total Goals:", TotalAwayGoals)
