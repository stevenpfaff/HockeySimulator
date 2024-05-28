import random
from team import matchups
from team import ana, ari, bos, buf, car, cgy, chi, col, cbj, dal, det, fla, edm, la, min, mtl, nsh, nj, nyi, nyr, ott, phi, pit, sj, sea, stl, tb, tor, van, vgk, wsh, wpg
from team import league, eastern_conference, western_conference, metropolitan_division, atlantic_division, central_division, pacific_division
import csv

class Sim(object):
    def __init__(self, name, offense, defense, goalie, sog, sog_ag, saves, goals, goals_against, wins, losses, otl, points):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.goalie = goalie
        self.sog = sog
        self.sog_ag = sog_ag
        self.sog = saves
        self.goals = goals
        self.goals_against = goals_against
        self.wins = wins
        self.losses = losses
        self.otl = otl
        self.points = points

def get_sog(team1, team2):
    if team1.offense <= 20 and team2.defense <= 20:
        return random.randint(18, 35)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 20:
        return random.randint(20, 35)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 20:
        return random.randint(22, 38)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 20:
        return random.randint(25, 40)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 20:
        return random.randint(28, 42)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 20:
        return random.randint(28, 45)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 20:
        return random.randint(30, 50)

    # 30-21 Defense Team 2
    elif team1.offense <= 20 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(15, 32)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(18, 32)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(18, 35)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(20, 35)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(25, 38)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(28, 42)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 30 & team2.defense > 20:
        return random.randint(30, 50)

    # 40-31 Defense Team 2
    elif team1.offense <= 20 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(13, 28)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(15, 30)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(15, 32)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(18, 35)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(22, 38)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(25, 40)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 40 & team2.defense > 30:
        return random.randint(28, 48)


    # 50-41 Defense Team 2
    elif team1.offense <= 20 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(13, 25)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(13, 28)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(15, 30)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(18, 32)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(22, 35)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(25, 40)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 50 & team2.defense > 40:
        return random.randint(25, 40)


    # 60-51 Defense Team 2
    elif team1.offense <= 20 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(13, 22)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(13, 25)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(15, 28)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(18, 30)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(22, 32)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(25, 35)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 60 & team2.defense > 50:
        return random.randint(25, 45)


    # 70-61 Defense Team 2
    elif team1.offense <= 20 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(13, 20)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(13, 22)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(15, 25)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(17, 30)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(20, 32)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(22, 35)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 70 & team2.defense > 60:
        return random.randint(25, 40)


    # 80-71 Defense
    elif team1.offense <= 20 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(10, 20)

    elif team1.offense <= 30 & team1.offense > 20 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(13, 22)

    elif team1.offense <= 40 & team1.offense > 30 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(15, 22)

    elif team1.offense <= 50 & team1.offense > 40 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(17, 25)

    elif team1.offense <= 60 & team1.offense > 50 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(20, 28)

    elif team1.offense <= 70 & team1.offense > 60 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(22, 30)

    elif team1.offense <= 80 & team1.offense > 70 and team2.defense <= 80 & team2.defense > 70:
        return random.randint(22, 30)

    return 0

def get_goals(defense, sog):
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

def get_winner(team1, team2, team1_goals, team2_goals, team1_sog, team2_sog):
    in_reg = True

    # Simulate overtime until a winner is determined
    while team1_goals == team2_goals:
        in_reg = False
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
        return "team1", in_reg
    else:
        return "team2", in_reg

def sim_game(team1, team2):
    team1_sog = get_sog(team1, team2)
    team2_sog = get_sog(team2, team1)
    team1_goals = get_goals(team2, team1_sog)
    team2_goals = get_goals(team1, team2_sog)
    winner, in_reg = get_winner(team1, team2, team1_goals, team2_goals, team1_sog, team2_sog)
    update_stats(team1, team2, team1_sog, team2_sog, team1_goals, team2_goals, winner, in_reg)

def update_stats(team1, team2, team1_sog, team2_sog, team1_goals, team2_goals, winner, in_reg):
    # Team 1 stats
    team1.sog += team1_sog
    team1.sog_ag += team2_sog
    team1.saves += (team2_sog - team2_goals)
    team1.goals += team1_goals
    team1.goals_against += team2_goals

    # Team 2 stats
    team2.sog += team2_sog
    team2.sog_ag += team1_sog
    team2.saves += (team1_sog - team1_goals)
    team2.goals += team2_goals
    team2.goals_against += team1_goals

    if winner == "team1" :
        if in_reg :
            team1.wins += 1
            team1.points += 2
            team2.losses += 1
        else:
            team1.wins += 1
            team1.points += 2
            team2.otl += 1
            team2.points += 1
    else:
        if in_reg :
            team2.wins += 1
            team2.points += 2
            team1.losses += 1
        else:
            team2.wins += 1
            team2.points += 2
            team1.otl += 1
            team1.points += 1

def sort_and_print(division_name, division_teams, filename):
    sorted_standings = sorted(division_teams, key=lambda x: x.points, reverse=True)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"{division_name} Standings:"])
        writer.writerow(["Rank", "Team", "Wins", "Losses", "OTL", "Points", "Goals For", "Goals Against", "Shooting%," "Save%"])
        for i, team in enumerate(sorted_standings, start=1):
            writer.writerow([i, team.name, team.wins, team.losses, team.otl, team.points, team.goals, team.goals_against, team.goals/team.sog, team.saves/team.sog_ag])

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
        sim_game(team1, team2)

# Final calls for season standings and playoff matchups.
sort_division_standings(metropolitan_division, atlantic_division, central_division, pacific_division, eastern_conference, western_conference, league)

