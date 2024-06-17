import random
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
        self.goalie_games = {}

    def update_stats(self, team1, team2, team1_sog, team2_sog, team1_goals, team2_goals, winner, regulation, team1_goalie, team2_goalie):
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

        if team1_goalie not in self.goalie_games:
            self.goalie_games[team1_goalie] = []
        self.goalie_games[team1_goalie].append(
            (team1.name, team2.name, team1_goals, team2_goals, winner == team1, regulation))

        if team2_goalie not in self.goalie_games:
            self.goalie_games[team2_goalie] = []
        self.goalie_games[team2_goalie].append(
            (team2.name, team1.name, team2_goals, team1_goals, winner == team2, regulation))

        if winner == team1:
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

    def reset_standings(self):
        for team in self.league:
            team.wins = 0
            team.losses = 0
            team.otl = 0
            team.points = 0
            team.goals = 0
            team.goals_against = 0
            team.sog = 0
            team.sog_ag = 0
            team.saves = 0
    def log_game_result(self, game):
        with open('output/game_results.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Team 1", "Team 1 Score", "Team 1 Shots", "Team 2", "Team 2 Score", "Team 2 Shots", "Overtime?"])
            writer.writerow([game.home.name, game.home_goals, game.home_sog, game.visitor.name, game.visitor_goals, game.visitor_sog,
                            game.regulation])

    def sort_and_print(self, division_name, division_teams, filename):
        sorted_standings = sorted(division_teams, key=lambda x: x.points, reverse=True)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"{division_name} Standings:"])
            writer.writerow(["Rank", "Team", "W", "L", "OTL", "PTS", "GF", "GA", "SH%", "SV%"])
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
        # self.sort_and_print("Eastern Conference", self.eastern_conference, "standings.csv")
        # self.sort_and_print("Western Conference", self.western_conference, "standings.csv")
        # self.sort_and_print("NHL", self.league, "standings.csv")

    def playoff_bracket(self, output_file):
        def add_playoff_appearance(matchups):
            for team1, team2 in matchups:
                team1.playoffs += 1
                team2.playoffs += 1
        def simulate_series(matchup):
            team1, team2 = matchup
            team1_wins = 0
            team2_wins = 0
            total_games = 0

            while team1_wins < 4 and team2_wins < 4 and total_games < 7:
                game = Game(team1, team2)
                if game.winner == team1:
                    team1_wins += 1
                elif game.winner == team2:
                    team2_wins += 1
                total_games += 1

            if team1_wins > team2_wins:
                series_winner = team1
            else:
                series_winner = team2

            return series_winner, total_games

        # Define the matchups
        west_winner = sorted(self.western_conference, key=lambda x: x.points, reverse=True)[:1]
        central_winner = sorted(self.central_division, key=lambda x: x.points, reverse=True)[:1]
        pacific_winner = sorted(self.pacific_division, key=lambda x: x.points, reverse=True)[:1]
        central_div_teams = sorted(self.central_division, key=lambda x: x.points, reverse=True)[:3]
        pacific_div_teams = sorted(self.pacific_division, key=lambda x: x.points, reverse=True)[:3]
        east_winner = sorted(self.eastern_conference, key=lambda x: x.points, reverse=True)[:1]
        atlantic_winner = sorted(self.atlantic_division, key=lambda x: x.points, reverse=True)[:1]
        metro_winner = sorted(self.metropolitan_division, key=lambda x: x.points, reverse=True)[:1]
        atlantic_div_teams = sorted(self.atlantic_division, key=lambda x: x.points, reverse=True)[:3]
        metro_div_teams = sorted(self.metropolitan_division, key=lambda x: x.points, reverse=True)[:3]
        central_non_top3 = sorted(self.central_division, key=lambda x: x.points, reverse=True)[3:]
        pacific_non_top3 = sorted(self.pacific_division, key=lambda x: x.points, reverse=True)[3:]
        atlantic_non_top3 = sorted(self.atlantic_division, key=lambda x: x.points, reverse=True)[3:]
        metro_non_top3 = sorted(self.metropolitan_division, key=lambda x: x.points, reverse=True)[3:]
        west_wildcard = sorted(central_non_top3 + pacific_non_top3, key=lambda x: x.points, reverse=True)[:2]
        east_wildcard = sorted(atlantic_non_top3 + metro_non_top3, key=lambda x: x.points, reverse=True)[:2]

        # Round 1 Begins
        round1_east_matchups = [
            (east_winner[0], east_wildcard[1]),
            (atlantic_div_teams[1], atlantic_div_teams[2]),
            (metro_div_teams[1], metro_div_teams[2])
        ]
        if east_winner != atlantic_winner:
            round1_east_matchups.append((atlantic_winner[0], east_wildcard[0]))
        elif east_winner != metro_winner:
            round1_east_matchups.append((metro_winner[0], east_wildcard[0]))

        east_first_round_results = []
        for matchup in round1_east_matchups:
            series_winner, total_games = simulate_series(matchup)
            series_winner.second_round += 1
            east_first_round_results.append((series_winner, total_games))

        round1_west_matchups = [
            (west_winner[0], west_wildcard[1]),
            (central_div_teams[1], central_div_teams[2]),
            (pacific_div_teams[1], pacific_div_teams[2])
        ]
        if west_winner != central_winner:
            round1_west_matchups.append((central_winner[0], west_wildcard[0]))
        elif east_winner != pacific_winner:
            round1_west_matchups.append((pacific_winner[0], west_wildcard[0]))

        west_first_round_results = []
        for matchup in round1_west_matchups:
            series_winner, total_games = simulate_series(matchup)
            series_winner.second_round += 1
            west_first_round_results.append((series_winner, total_games))

        # Round 2 Begins
        add_playoff_appearance(round1_east_matchups)
        add_playoff_appearance(round1_west_matchups)

        round2_east_matchups = [
            (east_first_round_results[0][0], east_first_round_results[1][0]),
            (east_first_round_results[2][0], east_first_round_results[3][0]),
        ]

        east_second_round_results = []
        for matchup in round2_east_matchups:
            series_winner, total_games = simulate_series(matchup)
            series_winner.conf_final += 1
            east_second_round_results.append((series_winner, total_games))

        round2_west_matchups = [
            (west_first_round_results[0][0], west_first_round_results[1][0]),
            (west_first_round_results[2][0], west_first_round_results[3][0]),
        ]

        west_second_round_results = []
        for matchup in round2_west_matchups:
            series_winner, total_games = simulate_series(matchup)
            series_winner.conf_final += 1
            west_second_round_results.append((series_winner, total_games))

        # Conference Final
        eastern_final = [
            (east_second_round_results[0][0], east_second_round_results[1][0])
        ]

        ecf_results = []
        for matchup in eastern_final:
            series_winner, total_games = simulate_series(matchup)
            series_winner.cup_final += 1
            ecf_results.append((series_winner, total_games))

        western_final = [
            (west_second_round_results[0][0], west_second_round_results[1][0])
        ]

        wcf_results = []
        for matchup in western_final:
            series_winner, total_games = simulate_series(matchup)
            series_winner.cup_final += 1
            wcf_results.append((series_winner, total_games))

        # Cup Final
        cup_final = [
            (ecf_results[0][0], wcf_results[0][0])
        ]

        cup_final_results = []
        for matchup in cup_final:
            series_winner, total_games = simulate_series(matchup)
            series_winner.cup_win += 1
            cup_final_results.append(series_winner)

        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Playoff Round", "Team 1", "Team 2", "Series Winner", "Total Games"])

            # Round 1
            writer.writerow(["Round 1"])
            # Write round 1 matchups...
            for matchup, result in zip(round1_east_matchups + round1_west_matchups,
                                       east_first_round_results + west_first_round_results):
                writer.writerow(["Round 1", matchup[0].name, matchup[1].name, result[0].name, result[1]])

            # Round 2
            writer.writerow(["Round 2"])
            # Write round 2 matchups...
            for matchup, result in zip(round2_east_matchups + round2_west_matchups,
                                       east_second_round_results + west_second_round_results):
                writer.writerow(["Round 2", matchup[0].name, matchup[1].name, result[0].name, result[1]])

            # Conference Finals
            writer.writerow(["Conference Finals"])
            # Write conference final matchups...
            for matchup, result in zip(eastern_final + western_final, ecf_results + wcf_results):
                writer.writerow(["Conference Finals", matchup[0].name, matchup[1].name, result[0].name, result[1]])

            # Cup Final
            writer.writerow(["Cup Final"])
            # Write cup final matchup...
            for matchup, result in zip(cup_final, cup_final_results):
                writer.writerow(["Cup Final", matchup[0].name, matchup[1].name, result.name, total_games])

        return cup_final_results

    def playoffs(self, output_file):
        playoff_results = self.playoff_bracket(output_file)
        return playoff_results

    def write_cup_winners(self):
        with open('output/playoff_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Team", "Playoff Appearances", "2nd Round Appearances", "Conference Finals", "Stanley Cup Finals",
                 "Stanley Cups"])
            for team in league:
                writer.writerow(
                    [team.name, team.playoffs, team.second_round, team.conf_final, team.cup_final, team.cup_win])

    def simulate_season(self, teams, matchups):
        self.reset_standings()
        for (team1_name, team2_name), num_games in matchups.items():
            team1 = teams[team1_name]
            team2 = teams[team2_name]
            for _ in range(num_games):
                weights = [0.7, 0.3]
                team1_goalie = random.choices([team1.starting_goalie, team1.backup_goalie], weights=weights)[0]
                team2_goalie = random.choices([team2.starting_goalie, team2.backup_goalie], weights=weights)[0]
                game = Game(team1, team2, team1_goalie, team2_goalie)
                self.update_stats(game.home, game.visitor, game.home_sog, game.visitor_sog, game.home_goals,
                                  game.visitor_goals, game.winner, game.regulation, team1_goalie, team2_goalie)
                # self.log_game_result(game)
