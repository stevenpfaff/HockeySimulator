import random
from team import league
for x in range(len(league)):
        print(league[x].name)

Team1Wins = 0
Team1Losses = 0
Team1OTL = 0
Team1Pts = 0
Team1TotalGoals = 0
Team1TotalSaves = 0
Team1TotalShots = 0
Team2Wins = 0
Team2Losses = 0
Team2OTL = 0
Team2Pts = 0
Team2TotalGoals = 0
Team2TotalSaves = 0
Team2TotalShots = 0
Team1 = input("Enter The Home Team")
Team2 = input("Enter The Away Team")
Team1Off = int(input("Enter Home Offense Rating on 20-80 scale"))
Team1Def = int(input("Enter Home Defense Rating on 20-80 scale"))
Team1Goal = int(input("Enter Home Goalie Rating on 20-80 scale"))
Team2Off = int(input("Enter Away Offense Rating on 20-80 scale"))
Team2Def = int(input("Enter Away Defense Rating on 20-80 scale"))
Team2Goal = int(input("Enter Away Goalie Rating on 20-80 scale"))
Games = int(input("Enter Amount of Games You'd Like to Simulate"))

for i in range(Games):
    Team1Shots = 0
    Team1Goals = 0
    Team1Saves = 0
    Team2Shots = 0
    Team2Goals = 0
    Team2Saves = 0

    #Shots on goal logic here
    #30-20 Defense
    if Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(15, 32)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(18, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(20, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(22, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(25, 38)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(28, 42)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 30 & Team2Def >= 20:
        aSog = random.randint(30, 50)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    #40-31 Defense
    elif Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(13, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(15, 32)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(18, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(22, 38)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(25, 40)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 40 & Team2Def > 30:
        aSog = random.randint(28, 48)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    #50-41 Defense
    elif Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(13, 28)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(15, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(18, 32)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(22, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(25, 40)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 50 & Team2Def > 40:
        aSog = random.randint(28, 45)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    #60-51 Defense
    elif Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(13, 25)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(15, 28)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(18, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(22, 32)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(25, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 60 & Team2Def > 50:
        aSog = random.randint(25, 45)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    #70-61 Defense
    elif Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(13, 22)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(15, 25)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(17, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(20, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(22, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 70 & Team2Def > 60:
        aSog = random.randint(25, 42)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    #80-71 Defense
    elif Team1Off <= 30 & Team1Off >= 20 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(13, 20)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 40 & Team1Off > 30 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(15, 22)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 50 & Team1Off > 40 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(17, 25)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 60 & Team1Off > 50 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(20, 28)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 70 & Team1Off > 60 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(22, 30)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
    elif Team1Off <= 80 & Team1Off > 70 and Team2Def <= 80 & Team2Def > 70:
        aSog = random.randint(25, 35)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots

    #Team2 Logic Here
    if Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(15, 32)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(18, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(20, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(22, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(25, 38)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(28, 42)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 30 & Team1Def >= 20:
        aSog = random.randint(30, 50)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    # 40-31 Defense
    elif Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(13, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(15, 32)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(18, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(22, 38)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(25, 40)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 40 & Team1Def > 30:
        aSog = random.randint(28, 48)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    # 50-41 Defense
    elif Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(13, 28)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(15, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(18, 32)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(22, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(25, 40)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 50 & Team1Def > 40:
        aSog = random.randint(28, 45)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    # 60-51 Defense
    elif Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(13, 25)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(15, 28)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(18, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(22, 32)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(25, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 60 & Team1Def > 50:
        aSog = random.randint(25, 45)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    # 70-61 Defense
    elif Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(13, 22)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(15, 25)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(17, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(20, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(22, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 70 & Team1Def > 60:
        aSog = random.randint(25, 42)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    # 80-71 Defense
    elif Team2Off <= 30 & Team2Off >= 20 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(13, 20)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 40 & Team2Off > 30 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(15, 22)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 50 & Team2Off > 40 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(17, 25)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 60 & Team2Off > 50 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(20, 28)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 70 & Team2Off > 60 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(22, 30)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
    elif Team2Off <= 80 & Team2Off > 70 and Team1Def <= 80 & Team1Def > 70:
        aSog = random.randint(25, 35)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots

    #Scoring Logic Here
    if Team2Goal <= 30 & Team2Goal >= 20:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 120:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves +=1
    elif Team2Goal <= 40 & Team2Goal > 30:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 110:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves += 1
    elif Team2Goal <= 50 & Team2Goal > 40:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 100:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves += 1
    elif Team2Goal <= 60 & Team2Goal > 50:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 98:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves += 1
    elif Team2Goal <= 70 & Team2Goal > 60:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 92:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves += 1
    elif Team2Goal <= 80 & Team2Goal > 70:
        for i in range(Team1Shots):
            Goals = random.randrange(1,1000)
            if Goals <= 85:
                Team1Goals +=1
                Team1TotalGoals +=1
            else:
                Team2Saves +=1
                Team2TotalSaves += 1
    if Team1Goal <= 30 & Team1Goal >= 20:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1
    elif Team1Goal <= 40 & Team1Goal > 30:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 110:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1
    elif Team1Goal <= 50 & Team1Goal > 40:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 100:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1
    elif Team1Goal <= 60 & Team1Goal > 50:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 98:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1
    elif Team1Goal <= 70 & Team1Goal > 60:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 90:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1
    elif Team1Goal <= 80 & Team1Goal > 70:
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 85:
                Team2Goals +=1
                Team2TotalGoals +=1
            else:
                Team1Saves +=1
                Team1TotalSaves += 1

    #Wins and Losses calculated here
    if Team2Goals > Team1Goals:
        Team2Wins += 1
        Team1Losses += 1
        Team2Pts += 2
    elif Team1Goals > Team2Goals:
        Team1Wins += 1
        Team2Losses += 1
        Team1Pts += 2
    while Team2Goals == Team1Goals:
        print("Overtime!")
        Team1Pts += 1
        Team2Pts += 1
        aSog = random.randint(1, 7)
        Team2Shots += aSog
        Team2TotalShots += Team2Shots
        for i in range(Team2Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                Team2Goals += 1
                Team2TotalGoals += 1
            else:
                Team1Saves += 1
                Team1TotalSaves += 1

        aSog = random.randint(1, 7)
        Team1Shots += aSog
        Team1TotalShots += Team1Shots
        for i in range(Team1Shots):
            Goals = random.randrange(1, 1000)
            if Goals <= 120:
                Team1Goals += 1
                Team1TotalGoals += 1
            else:
                Team2Saves += 1
                Team2TotalSaves += 1

        if Team1Goals > Team2Goals:
            Team1Pts += 1
            Team2OTL += 1
            Team1Wins +=1

        elif Team2Goals > Team1Goals:
            Team2Pts += 1
            Team1OTL += 1
            Team2Wins += 1


    print(Team1, "Shots:", Team1Shots, "Goals:", Team1Goals, Team2, "Shots:", Team2Shots, "Goals:", Team2Goals)

print(Team1TotalShots, Team2TotalShots)
print(Team1TotalSaves, Team2TotalSaves)
print(Team1, "Wins:", Team1Wins, "Losses:", Team1Losses, "OTL:", Team1OTL, "Points:", Team1Pts)
print(Team1, "Total Goals:", Team1TotalGoals, "Shooting Percentage:", Team1TotalGoals / Team1TotalShots, "Save Percentage:", Team1TotalSaves / Team2TotalShots)
print(Team2, "Wins:", Team2Wins, "Losses:", Team2Losses, "OTL:", Team2OTL, "Points:", Team2Pts)
print(Team2, "Total Goals:", Team2TotalGoals, "Shooting Percentage:", Team2TotalGoals / Team2TotalShots, "Save Percentage:", Team2TotalSaves / Team1TotalShots)
