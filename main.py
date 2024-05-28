import random
from team import matchups
from team import ana, ari, bos, buf, car, cgy, chi, col, cbj, dal, det, fla, edm, la, min, mtl, nsh, nj, nyi, nyr, ott, phi, pit, sj, sea, stl, tb, tor, van, vgk, wsh, wpg
import csv

league = [ana, ari, bos, buf, car, cgy, chi, col, cbj, dal, det, fla, edm, la, min, mtl, nsh, nj, nyi, nyr, ott, phi, pit, sj, sea, stl, tb, tor, van, vgk, wsh, wpg]
eastern_conference = [bos, buf, det, fla, mtl, ott, tb, tor, nj, nyi, nyr, phi, pit, car, cbj, wsh]
western_conference = [ari, chi, col, dal, min, nsh, stl,  wpg, ana, cgy, edm, la, sj, sea, van, vgk,]
metropolitan_division = [nj, nyi, nyr, phi, pit, car, cbj, wsh]
atlantic_division = [bos, buf, det, fla, mtl, ott, tb, tor]
central_division = [ari, chi, col, dal, min, nsh, stl,  wpg]
pacific_division = [ana, cgy, edm, la, sj, sea, van, vgk,]
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
            if random.random() <= 0.115:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 30 & team2.goalie > 20:
            if random.random() <= 0.110:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 40 & team2.goalie > 30:
            if random.random() <= 0.105:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 50 & team2.goalie > 40:
            if random.random() <= 0.102:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 60 & team2.goalie > 50:
            if random.random() <= 0.100:
                team1_goals += 1
                team1.goals += 1
                team2.goals_against += 1
            else:
                team2_saves += 1
        elif team2.goalie <= 70 & team2.goalie > 60:
            if random.random() <= 0.090:
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
            if random.random() <= 0.115:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 30 & team1.goalie > 20:
            if random.random() <= 0.110:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 40 & team1.goalie > 30:
            if random.random() <= 0.105:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 50 & team1.goalie > 40:
            if random.random() <= 0.102:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 60 & team1.goalie > 50:
            if random.random() <= 0.100:
                team2_goals += 1
                team2.goals += 1
                team1.goals_against += 1
            else:
                team1_saves += 1
        elif team1.goalie <= 70 & team1.goalie > 60:
            if random.random() <= 0.090:
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


import csv

def sort_and_print(division_name, division_teams, filename):
    sorted_standings = sorted(division_teams, key=lambda x: x.points, reverse=True)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"{division_name} Standings:"])
        writer.writerow(["Rank", "Team", "Wins", "Losses", "OTL", "Points", "Goals For", "Goals Against"])
        for i, team in enumerate(sorted_standings, start=1):
            writer.writerow([i, team.name, team.wins, team.losses, team.otl, team.points, team.goals, team.goals_against])

def sort_division_standings(metropolitan_division, atlantic_division, central_division, pacific_division, eastern_conference, western_conference, league):
    with open("standings.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["NHL Standings:"])

    sort_and_print("Metropolitan", metropolitan_division, "standings.csv")
    sort_and_print("Atlantic", atlantic_division, "standings.csv")
    sort_and_print("Central", central_division, "standings.csv")
    sort_and_print("Pacific", pacific_division, "standings.csv")
    sort_and_print("Eastern Conference", eastern_conference, "standings.csv")
    sort_and_print("Western Conference", western_conference, "standings.csv")
    sort_and_print("NHL", league, "standings.csv")



# Season Sim occurs here:
for (team1_name, team2_name), num_games in matchups.items():
    team1 = globals()[team1_name]
    team2 = globals()[team2_name]
    for _ in range(num_games):
        team1_sog = get_sog1(team1, team2)
        team2_sog = get_sog2(team1, team2)
        team1_goals, team2_saves = get_goals1(team1, team2, team1_sog)
        team2_goals, team1_saves = get_goals2(team1, team2, team2_sog)
        get_winner(team1, team2, team1_goals, team2_goals, team1_sog, team2_sog)

# Final calls for season standings and playoff matchups.
sort_division_standings(metropolitan_division, atlantic_division, central_division, pacific_division, eastern_conference, western_conference, league)

