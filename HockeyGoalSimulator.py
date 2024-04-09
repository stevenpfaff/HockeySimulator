import random

ShotsOnGoal = 0
TotalGoals = 0
Saves = 0

#Shots on goal generated randomly
Sog = random.randint(15, 50)
ShotsOnGoal += Sog

for i in range(ShotsOnGoal):
    #Shooting% set to 8.6% here (NHL League Average)
    Goals = random.randrange(1,1000)
    if Goals <= 86:
        TotalGoals +=1
    else:
        Saves +=1

print("Total Goals:", TotalGoals)
print("Shots on goal:",ShotsOnGoal)









