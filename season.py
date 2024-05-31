import random
from team import matchups
from team import ana, ari, bos, buf, car, cgy, chi, col, cbj, dal, det, fla, edm, la, min, mtl, nsh, nj, nyi, nyr, ott, phi, pit, sj, sea, stl, tb, tor, van, vgk, wsh, wpg
from team import league, eastern_conference, western_conference, metropolitan_division, atlantic_division, central_division, pacific_division
from game import Game
import csv

class SeasonSimulator:
    def __init__(self):
        self.league = league
        self.eastern_conference = eastern_conference
        self.western_conference = western_conference
        self.metropolitan_division = metropolitan_division
        self.atlantic_division = atlantic_division
        self.central_division = central_division
        self.pacific_division = pacific_division

    def update_stats(self, team1, team2, team1_sog, team2_sog, team1_goals, team2_goals, winner, regulation):
        team1.sog += team1_sog
        team1.sog_ag += team2_sog
        team1.saves += (team2_sog - team2_goals)
        team1.goals += team1_goals
        team1.goals_against += team2_goals

        team2.sog += team2_sog
        team2.sog_ag += team1_sog
        team2.saves += (team1_sog - team1_goals)
        team2.goals += team2_goals
        team2.goals_against += team1_goals

        if winner == "team1":
            if regulation:
                team1.wins += 1
                team1.points += 2
                team2.losses += 1
            else:
                team1.wins += 1
                team1.points += 2
                team2.otl += 1
                team2.points += 1
        else:
            if regulation:
                team2.wins += 1
                team2.points += 2
                team1.losses += 1
            else:
                team2.wins += 1
                team2.points += 2
                team1.otl += 1
                team1.points += 1

    def sort_and_print(self, division_name, division_teams, filename):
        sorted_standings = sorted(division_teams, key=lambda x: x.points, reverse=True)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"{division_name} Standings:"])
            writer.writerow(["Rank", "Team", "Wins", "Losses", "OTL", "Points", "Goals For", "Goals Against", "Shooting%", "Save%"])
            for i, team in enumerate(sorted_standings, start=1):
                writer.writerow([i, team.name, team.wins, team.losses, team.otl, team.points, team.goals, team.goals_against, "{:.2f}".format((team.goals/team.sog)*100)+ "%", "{:.3f}".format(team.saves/team.sog_ag)])
            writer.writerow("")

    def sort_division_standings(self):
        with open("standings.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["NHL Standings:"])

        self.sort_and_print("Metropolitan", self.metropolitan_division, "standings.csv")
        self.sort_and_print("Atlantic", self.atlantic_division, "standings.csv")
        self.sort_and_print("Central", self.central_division, "standings.csv")
        self.sort_and_print("Pacific", self.pacific_division, "standings.csv")
        self.sort_and_print("Eastern Conference", self.eastern_conference, "standings.csv")
        self.sort_and_print("Western Conference", self.western_conference, "standings.csv")
        self.sort_and_print("NHL", self.league, "standings.csv")

    def simulate_season(self):
        for (team1_name, team2_name), num_games in matchups.items():
            team1 = globals()[team1_name]
            team2 = globals()[team2_name]
            for _ in range(num_games):
                game = Game(team1, team2)
                self.update_stats(game.home, game.visitor, game.home_sog, game.visitor_sog, game.home_goals, game.visitor_goals, game.winner, game.regulation)

        self.sort_division_standings()

simulator = SeasonSimulator()
simulator.simulate_season()
