import random
from team import matchups
from team import ana, ari, bos, buf, car, cgy, chi, col, cbj, dal, det, fla, edm, la, min, mtl, nsh, nj, nyi, nyr, ott, phi, pit, sj, sea, stl, tb, tor, van, vgk, wsh, wpg
from team import league, eastern_conference, western_conference, metropolitan_division, atlantic_division, central_division, pacific_division
from game import Game
from team import Team
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

    def playoff_bracket(self, output_file):
        def simulate_series(matchup):
            team1, team2 = matchup
            team1_wins = 0
            team2_wins = 0
            total_games = 0

            while total_games < 7:
                game = Game(team1, team2)
                print(f"Game {total_games + 1}: {team1.name} vs {team2.name}, Winner: {game.winner}")
                if game.winner == team1:
                    team1_wins += 1
                elif game.winner == team2:
                    team2_wins += 1
                total_games += 1
                print(f"Team 1 wins: {team1_wins}, Team 2 wins: {team2_wins}")

            if team1_wins > team2_wins:
                series_winner = team1
            else:
                series_winner = team2
            print(f"Series Winner: {series_winner.name}")

            # Update overall win counts
            team1.wins += team1_wins
            team2.wins += team2_wins

            return series_winner

        # Define the matchups
        west_winner = sorted(western_conference, key=lambda x: x.points, reverse=True)[:1]
        central_winner = sorted(central_division, key=lambda x: x.points, reverse=True)[:1]
        pacific_winner = sorted(pacific_division, key=lambda x: x.points, reverse=True)[:1]
        west_wildcard1 = sorted(western_conference, key=lambda x: x.points, reverse=True)[:7]
        west_wildcard2 = sorted(western_conference, key=lambda x: x.points, reverse=True)[:8]
        central_div_teams = sorted(central_division, key=lambda x: x.points, reverse=True)[:3]
        pacific_div_teams = sorted(pacific_division, key=lambda x: x.points, reverse=True)[:3]
        east_winner = sorted(eastern_conference, key=lambda x: x.points, reverse=True)[:1]
        atlantic_winner = sorted(atlantic_division, key=lambda x: x.points, reverse=True)[:1]
        metro_winner = sorted(metropolitan_division, key=lambda x: x.points, reverse=True)[:1]
        atlantic_div_teams = sorted(atlantic_division, key=lambda x: x.points, reverse=True)[:3]
        metro_div_teams = sorted(metropolitan_division, key=lambda x: x.points, reverse=True)[:3]
        east_wildcard1 = sorted(eastern_conference, key=lambda x: x.points, reverse=True)[:7]
        east_wildcard2 = sorted(eastern_conference, key=lambda x: x.points, reverse=True)[:8]

        matchups = [
            (west_winner[0], west_wildcard2[7]),
            (central_div_teams[1], central_div_teams[2]),
            (pacific_div_teams[1], pacific_div_teams[2]),
            (east_winner[0], east_wildcard2[7]),
            (atlantic_div_teams[1], atlantic_div_teams[2]),
            (metro_div_teams[1], metro_div_teams[2])
        ]
        if west_winner != central_winner:
            matchups.append((central_winner[0], west_wildcard1[0]))
        elif west_winner != pacific_winner:
            matchups.append((pacific_winner[0], west_wildcard1[0]))
        if east_winner != atlantic_winner:
            matchups.append((atlantic_winner[0], east_wildcard1[0]))
        elif east_winner != metro_winner:
            matchups.append((metro_winner[0], east_wildcard1[0]))

        playoff_results = []

        for matchup in matchups:
            series_winner = simulate_series(matchup)
            playoff_results.append((matchup[0].name, matchup[1].name, series_winner))

        # Write playoff results to CSV
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Team 1", "Team 2", "Series Winner"])
            for i, matchup in enumerate(matchups):
                team1, team2 = matchup
                writer.writerow([playoff_results[i][0], playoff_results[i][1], playoff_results[i][2]])

        return playoff_results

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
output_file = "playoffs.csv"
playoff_results = simulator.playoff_bracket(output_file)
