import random
from team import matchups
from team import ana
from team import ari
from team import bos
from team import buf
from team import car
from team import cgy
from team import chi
from team import col
from team import cbj
from team import dal
from team import det
from team import fla
from team import edm
from team import la
from team import min
from team import mtl
from team import nsh
from team import nj
from team import nyi
from team import nyr
from team import ott
from team import phi
from team import pit
from team import sj
from team import sea
from team import stl
from team import tb
from team import tor
from team import van
from team import vgk
from team import wsh
from team import wpg

class Sim(object):
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

def get_sog1(team1, team2):
    team1_sog = 0
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

    # 30-21 Defense Team 2
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

    # 40-31 Defense Team 2
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

    # 50-41 Defense Team 2
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

    # 60-51 Defense Team 2
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

    # 70-61 Defense Team 2
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

    # 80-71 Defense
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
    return team1_sog

def get_sog2(team1, team2):
    team2_sog = 0
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
    return team2_sog

def get_goals1(team1, team2, team1_sog):
    team1_goals = 0
    team2_saves = 0
    for i in range(team1_sog):
        if team2.goalie <= 20:
            if random.random() <= 0.125:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 30 & team2.goalie > 20:
            if random.random() <= 0.120:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 40 & team2.goalie > 30:
            if random.random() <= 0.110:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 50 & team2.goalie > 40:
            if random.random() <= 0.100:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 60 & team2.goalie > 50:
            if random.random() <= 0.098:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 70 & team2.goalie > 60:
            if random.random() <= 0.092:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 80 & team2.goalie > 70:
            if random.random() <= 0.085:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
    return team1_goals, team2_saves

def get_goals2(team1,team2, team2_sog):
    team2_goals = 0
    team1_saves = 0
    for i in range(team2_sog):
        if team1.goalie <= 20:
            if random.random() <= 0.125:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 30 & team1.goalie > 20:
            if random.random() <= 0.120:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 40 & team1.goalie > 30:
            if random.random() <= 0.110:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 50 & team1.goalie > 40:
            if random.random() <= 0.100:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 60 & team1.goalie > 50:
            if random.random() <= 0.098:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 70 & team1.goalie > 60:
            if random.random() <= 0.092:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 80 & team1.goalie > 70:
            if random.random() <= 0.085:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
    return team2_goals, team1_saves

def get_winner(team1, team2, team1_goals, team2_goals, team1_sog, team2_sog):
    if team1_goals > team2_goals:
        team1.points += 2
        team1.wins += 1
        team2.losses += 1
    elif team2_goals > team1_goals:
        team2.points += 2
        team2.wins += 1
        team1.losses += 1
    else:  # If it's a tie
        team1.points += 1
        team2.points += 1

        # Simulate overtime until a winner is determined
        while team1_goals == team2_goals:
            # Simulate additional goals
            goal1 = random.random()
            goal2 = random.random()
            if goal1 > goal2:
                team1_goals += 1
                team1_sog += 1
            elif goal2 > goal1:
                team2_goals += 1
                team2_sog += 1

        # Determine the winner after overtime
        if team1_goals > team2_goals:
            team1.points += 1
            team2.otl += 1
            team1.wins += 1
        elif team2_goals > team1_goals:
            team2.points += 1
            team1.otl += 1
            team2.wins += 1

for (team1_name, team2_name), num_games in matchups.items():
    team1 = globals()[team1_name]
    team2 = globals()[team2_name]
    for _ in range(num_games):
        team1_sog = get_sog1(team1, team2)
        team2_sog = get_sog2(team1, team2)
        team1_goals, team2_saves = get_goals1(team1, team2, team1_sog)
        team2_goals, team1_saves = get_goals2(team1, team2, team2_sog)
        get_winner(team1, team2, team1_goals, team2_goals, team1_sog, team2_sog)

print(ana.name, "W:", ana.wins, "L:", ana.losses, "OTL:", ana.otl, "PTS:", ana.points, "G:", ana.goals, "GA:", ana.goals_against)
print(ari.name, "W:", ari.wins, "L:", ari.losses, "OTL:", ari.otl, "PTS:", ari.points, "G:", ari.goals, "GA:", ari.goals_against)
print(bos.name, "W:", bos.wins,"L:", bos.losses,"OTL:", bos.otl, "PTS:", bos.points, "G:", bos.goals, "GA:", bos.goals_against)
print(buf.name, "W:", buf.wins,"L:", buf.losses,"OTL:", buf.otl, "PTS:", buf.points, "G:", buf.goals, "GA:", buf.goals_against)
print(cgy.name, "W:", cgy.wins,"L:", cgy.losses,"OTL:", cgy.otl, "PTS:", cgy.points, "G:", cgy.goals, "GA:", cgy.goals_against)
print(car.name, "W:", car.wins, "L:", car.losses, "OTL:", car.otl, "PTS:", car.points, "G:", car.goals, "GA:", car.goals_against)
print(chi.name, "W:", chi.wins, "L:", chi.losses, "OTL:", chi.otl, "PTS:", chi.points, "G:", chi.goals, "GA:", chi.goals_against)
print(col.name, "W:", col.wins, "L:", col.losses, "OTL:", col.otl, "PTS:", col.points, "G:", col.goals, "GA:", col.goals_against)
print(cbj.name, "W:", cbj.wins, "L:", cbj.losses, "OTL:", cbj.otl, "PTS:", cbj.points, "G:", cbj.goals, "GA:", cbj.goals_against)
print(dal.name, "W:", dal.wins, "L:", dal.losses, "OTL:", dal.otl, "PTS:", dal.points, "G:", dal.goals, "GA:", dal.goals_against)
print(det.name, "W:", det.wins, "L:", det.losses, "OTL:", det.otl, "PTS:", det.points, "G:", det.goals, "GA:", det.goals_against)
print(edm.name, "W:", edm.wins, "L:", edm.losses, "OTL:", edm.otl, "PTS:", edm.points, "G:", edm.goals, "GA:", edm.goals_against)
print(fla.name, "W:", fla.wins, "L:", fla.losses, "OTL:", fla.otl, "PTS:", fla.points, "G:", fla.goals, "GA:", fla.goals_against)
print(la.name, "W:", la.wins, "L:", la.losses, "OTL:", la.otl, "PTS:", la.points, "G:", la.goals, "GA:", la.goals_against)
print(min.name, "W:", min.wins, "L:", min.losses, "OTL:", min.otl, "PTS:", min.points, "G:", min.goals, "GA:", min.goals_against)
print(mtl.name, "W:", mtl.wins, "L:", mtl.losses, "OTL:", mtl.otl, "PTS:", mtl.points, "G:", mtl.goals, "GA:", mtl.goals_against)
print(nsh.name, "W:", nsh.wins, "L:", nsh.losses, "OTL:", nsh.otl, "PTS:", nsh.points, "G:", nsh.goals, "GA:", nsh.goals_against)
print(nj.name, "W:", nj.wins, "L:", nj.losses, "OTL:", nj.otl, "PTS:", nj.points, "G:", nj.goals, "GA:", nj.goals_against)
print(nyi.name, "W:", nyi.wins, "L:", nyi.losses, "OTL:", nyi.otl, "PTS:", nyi.points, "G:", nyi.goals, "GA:", nyi.goals_against)
print(nyr.name, "W:", nyr.wins, "L:", nyr.losses, "OTL:", nyr.otl, "PTS:", nyr.points, "G:", nyr.goals, "GA:", nyr.goals_against)
print(ott.name, "W:", ott.wins, "L:", ott.losses, "OTL:", ott.otl, "PTS:", ott.points, "G:", ott.goals, "GA:", ott.goals_against)
print(phi.name, "W:", phi.wins, "L:", phi.losses, "OTL:", phi.otl, "PTS:", phi.points, "G:", phi.goals, "GA:", phi.goals_against)
print(pit.name, "W:", pit.wins, "L:", pit.losses, "OTL:", pit.otl, "PTS:", pit.points, "G:", pit.goals, "GA:", pit.goals_against)
print(sj.name, "W:", sj.wins, "L:", sj.losses, "OTL:", sj.otl, "PTS:", sj.points, "G:", sj.goals, "GA:", sj.goals_against)
print(sea.name, "W:", sea.wins, "L:", sea.losses, "OTL:", sea.otl, "PTS:", sea.points, "G:", sea.goals, "GA:", sea.goals_against)
print(stl.name, "W:", stl.wins, "L:", stl.losses, "OTL:", stl.otl, "PTS:", stl.points, "G:", stl.goals, "GA:", stl.goals_against)
print(tb.name, "W:", tb.wins, "L:", tb.losses, "OTL:", tb.otl, "PTS:", tb.points, "G:", tb.goals, "GA:", tb.goals_against)
print(tor.name, "W:", tor.wins, "L:", tor.losses, "OTL:", tor.otl, "PTS:", tor.points, "G:", tor.goals, "GA:", tor.goals_against)
print(van.name, "W:", van.wins, "L:", van.losses, "OTL:", van.otl, "PTS:", van.points, "G:", van.goals, "GA:", van.goals_against)
print(vgk.name, "W:", vgk.wins, "L:", vgk.losses, "OTL:", vgk.otl, "PTS:", vgk.points, "G:", vgk.goals, "GA:", vgk.goals_against)
print(wsh.name, "W:", wsh.wins, "L:", wsh.losses, "OTL:", wsh.otl, "PTS:", wsh.points, "G:", wsh.goals, "GA:", wsh.goals_against)
print(wpg.name, "W:", wpg.wins, "L:", wpg.losses, "OTL:", wpg.otl, "PTS:", wpg.points, "G:", wpg.goals, "GA:", wpg.goals_against)
