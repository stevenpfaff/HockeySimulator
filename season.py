import random
from team import league, eastern_conference, western_conference, metropolitan_division, atlantic_division, central_division, pacific_division
from game import Game
import csv
import os
import functools

class SeasonSimulator:
    def __init__(self):
        self.league = league
        self.eastern_conference = eastern_conference
        self.western_conference = western_conference
        self.metropolitan_division = metropolitan_division
        self.atlantic_division = atlantic_division
        self.central_division = central_division
        self.pacific_division = pacific_division

    def update_stats(self, team1, team2, team1_sog, team2_sog, team1_goals, team2_goals, winner, regulation,
                     team1_goalie, team2_goalie):
        # Update goalie stats
        team1_goalie.games += 1
        team1_goalie.shots_against += team2_sog
        team1_goalie.saves += (team2_sog - team2_goals)
        team1_goalie.goals_allowed += team2_goals

        team2_goalie.games += 1
        team2_goalie.shots_against += team1_sog
        team2_goalie.saves += (team1_sog - team1_goals)
        team2_goalie.goals_allowed += team1_goals

        # Update team stats
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

        # Update standings based on game result
        if winner == team1:
            if regulation:
                team1.regulation_wins += 1
                team1.wins += 1
                team1.points += 2
                team2.losses += 1
                team1_goalie.wins += 1
                team2_goalie.losses += 1
            else:
                team1.wins += 1
                team1.points += 2
                team2.otl += 1
                team2.points += 1
                team1.goals += team1_goals
                team1.goals_against += team2_goals
                team2.goals += team2_goals
                team2.goals_against += team1_goals
                team2_goalie.losses += 1
                team1_goalie.wins += 1
        else:
            if regulation:
                team2.regulation_wins += 1
                team2.wins += 1
                team2.points += 2
                team1.losses += 1
                team2_goalie.wins += 1
                team1_goalie.losses += 1
            else:
                team2.wins += 1
                team2.points += 2
                team1.otl += 1
                team1.points += 1
                team1.goals += team1_goals
                team1.goals_against += team2_goals
                team2.goals += team2_goals
                team2.goals_against += team1_goals
                team1_goalie.losses += 1
                team2_goalie.wins += 1

        # Update shutouts for goalies
        if team1_goals == 0:
            team2_goalie.shutouts += 1
        elif team2_goals == 0:
            team1_goalie.shutouts += 1
    def reset_standings(self):
        for team in self.league:
            team.wins = 0
            team.regulation_wins = 0
            team.row = 0
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
            # Check if file is empty to add headers
            if file.tell() == 0:
                writer.writerow(["Team 1", "Team 1 Goalie", "Team 1 Score", "Team 1 Shots",
                                 "Team 2", "Team 2 Goalie", "Team 2 Score", "Team 2 Shots",
                                 "Overtime?"])
            writer.writerow([game.home.name, game.home_goalie.name, game.home_goals, game.home_sog,
                             game.visitor.name, game.visitor_goalie.name, game.visitor_goals, game.visitor_sog,
                             game.regulation])

    def reset_goalie_stats(self):
        for team in self.league:
            team.starting_goalie.games = 0
            team.starting_goalie.shots_against = 0
            team.starting_goalie.saves = 0
            team.starting_goalie.goals_allowed = 0
            team.backup_goalie.games = 0
            team.backup_goalie.shots_against = 0
            team.backup_goalie.saves = 0
            team.backup_goalie.goals_allowed = 0
            team.starting_goalie_selections = 0
            team.backup_goalie_selections = 0
    def log_goalie_stats(self, sim_number):
        output_file = "output/goalie_stats.csv"
        file_exists = os.path.isfile(output_file)

        # Append to the CSV file
        with open(output_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"Simulation {sim_number} Goalie Stats:"])
            # Write header only if the file is new
            if not file_exists:
                writer.writerow(["Goalie", "Team", "GP", "W", "L", "SO", "SV%"])
            for team in self.league:
                for goalie in [team.starting_goalie, team.backup_goalie]:
                    if goalie.shots_against > 0:
                        save_percentage = goalie.saves / goalie.shots_against
                    else:
                        save_percentage = 0
                    writer.writerow([goalie.name, team.abrv, goalie.games, goalie.wins, goalie.losses, goalie.shutouts,
                                     "{:.3f}%".format(save_percentage)])

    import csv
    import os

    def sort_and_print(self, division_name, division_teams, filename):
        sorted_standings = sorted(division_teams, key=lambda x: (x.points, x.wins, x.regulation_wins, x.row, x.goals - x.goals_against,),
                                  reverse=True)

        # Check if the file exists and if it's empty
        file_exists = os.path.exists(filename)
        file_is_empty = os.path.getsize(filename) == 0 if file_exists else True

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Only write the header if the file is empty
            if file_is_empty:
                writer.writerow(["Rank", "Team", "W", "L", "OTL", "PTS", "GF", "GA", "SH%", "SV%", "Regulation"])

            # Write the sorted standings
            for i, team in enumerate(sorted_standings, start=1):
                if team.sog_ag > 0:
                    save_percentage = team.saves / team.sog_ag
                else:
                    save_percentage = 0

                if team.sog > 0:
                    shooting_percentage = "{:.2f}".format((team.goals / team.sog) * 100) + "%"
                else:
                    shooting_percentage = "0.00%"

                writer.writerow(
                    [i, team.abrv, team.wins, team.losses, team.otl, team.points, team.goals, team.goals_against,
                     shooting_percentage, "{:.3f}".format(save_percentage), team.regulation_wins,])

            # Optional: Add an empty row to separate simulations
            writer.writerow("")

    def sort_division_standings(self, filename, sim_number):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
        #     writer.writerow([f"Simulation {sim_number} Standings:"])
        #
        self.sort_and_print("Metropolitan", self.metropolitan_division, filename)
        self.sort_and_print("Atlantic", self.atlantic_division, filename)
        self.sort_and_print("Central", self.central_division, filename)
        self.sort_and_print("Pacific", self.pacific_division, filename)
        # self.sort_and_print("Eastern Conference", self.eastern_conference, "standings.csv")
        # self.sort_and_print("Western Conference", self.western_conference, "standings.csv")
        # self.sort_and_print("NHL", self.league, filename)

    def playoff_bracket(self, output_file):

        def nhl_tiebreaker(team1, team2):
            if team1.points > team2.points:
                return -1
            elif team1.points < team2.points:
                return 1
            if team1.regulation_wins > team2.regulation_wins:
                return -1
            elif team1.regulation_wins < team2.regulation_wins:
                return 1
            return 0

        def add_playoff_appearance(matchups):
            for team1, team2 in matchups:
                team1.playoffs += 1
                team2.playoffs += 1

        def simulate_series(matchup, home_goalie, away_goalie):
            team1, team2 = matchup
            team1_wins = 0
            team2_wins = 0
            total_games = 0

            while team1_wins < 4 and team2_wins < 4 and total_games < 7:
                game = Game(team1, team2, home_goalie, away_goalie)
                if game.winner == team1:
                    team1_wins += 1
                elif game.winner == team2:
                    team2_wins += 1
                total_games += 1

            series_winner = team1 if team1_wins > team2_wins else team2
            return series_winner, total_games

            # Sort divisions and determine wildcards

        central_div_teams = sorted(self.central_division, key=functools.cmp_to_key(nhl_tiebreaker))
        pacific_div_teams = sorted(self.pacific_division, key=functools.cmp_to_key(nhl_tiebreaker))
        atlantic_div_teams = sorted(self.atlantic_division, key=functools.cmp_to_key(nhl_tiebreaker))
        metro_div_teams = sorted(self.metropolitan_division, key=functools.cmp_to_key(nhl_tiebreaker))

        # Top 3 from each division
        central_top3 = central_div_teams[:3]
        pacific_top3 = pacific_div_teams[:3]
        atlantic_top3 = atlantic_div_teams[:3]
        metro_top3 = metro_div_teams[:3]

        # Remaining teams for wildcards
        west_remaining = central_div_teams[3:] + pacific_div_teams[3:]
        east_remaining = atlantic_div_teams[3:] + metro_div_teams[3:]

        west_wildcards = sorted(west_remaining, key=functools.cmp_to_key(nhl_tiebreaker))[:2]
        east_wildcards = sorted(east_remaining, key=functools.cmp_to_key(nhl_tiebreaker))[:2]

        # Identify division winners
        central_winner = central_top3[0]
        pacific_winner = pacific_top3[0]
        atlantic_winner = atlantic_top3[0]
        metro_winner = metro_top3[0]

        # Determine top seeds in each conference
        west_top_teams = [central_winner, pacific_winner]
        east_top_teams = [atlantic_winner, metro_winner]

        west_top_teams_sorted = sorted(west_top_teams, key=lambda x: x.points, reverse=True)
        east_top_teams_sorted = sorted(east_top_teams, key=lambda x: x.points, reverse=True)

        west_first_seed = west_top_teams_sorted[0]
        west_second_seed = west_top_teams_sorted[1]

        east_first_seed = east_top_teams_sorted[0]
        east_second_seed = east_top_teams_sorted[1]

        # Wildcards matchups
        west_wildcard1, west_wildcard2 = sorted(west_wildcards, key=lambda x: x.points, reverse=True)
        east_wildcard1, east_wildcard2 = sorted(east_wildcards, key=lambda x: x.points, reverse=True)

        # First round matchups - Eastern Conference
        round1_east_matchups = [
            (east_first_seed, east_wildcard2),  # 1 vs WC2
            (east_second_seed, east_wildcard1),  # 2 vs WC1
            (atlantic_top3[1], atlantic_top3[2]),  # 3 vs 4 in Atlantic
            (metro_top3[1], metro_top3[2])  # 3 vs 4 in Metro
        ]

        # First round matchups - Western Conference
        round1_west_matchups = [
            (west_first_seed, west_wildcard2),  # 1 vs WC2
            (west_second_seed, west_wildcard1),  # 2 vs WC1
            (pacific_top3[1], pacific_top3[2]),  # 3 vs 4 in Pacific
            (central_top3[1], central_top3[2])  # 3 vs 4 in Central
        ]

        east_first_round_results = []
        for matchup in round1_east_matchups:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.second_round += 1
            east_first_round_results.append((series_winner, total_games))

        west_first_round_results = []
        for matchup in round1_west_matchups:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.second_round += 1
            west_first_round_results.append((series_winner, total_games))

        # Second round matchups
        add_playoff_appearance(round1_east_matchups)
        add_playoff_appearance(round1_west_matchups)

        round2_east_matchups = [
            (east_first_round_results[0][0], east_first_round_results[1][0]),
            (east_first_round_results[2][0], east_first_round_results[3][0])
        ]

        round2_west_matchups = [
            (west_first_round_results[0][0], west_first_round_results[1][0]),
            (west_first_round_results[2][0], west_first_round_results[3][0])
        ]

        east_second_round_results = []
        for matchup in round2_east_matchups:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.conf_final += 1
            east_second_round_results.append((series_winner, total_games))

        west_second_round_results = []
        for matchup in round2_west_matchups:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.conf_final += 1
            west_second_round_results.append((series_winner, total_games))

        # Conference Finals
        eastern_final = [
            (east_second_round_results[0][0], east_second_round_results[1][0])
        ]

        ecf_results = []
        for matchup in eastern_final:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.cup_final += 1
            ecf_results.append((series_winner, total_games))

        western_final = [
            (west_second_round_results[0][0], west_second_round_results[1][0])
        ]

        wcf_results = []
        for matchup in western_final:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.cup_final += 1
            wcf_results.append((series_winner, total_games))

        # Stanley Cup Final
        cup_final = [
            (ecf_results[0][0], wcf_results[0][0])
        ]

        cup_final_results = []
        for matchup in cup_final:
            home_team, away_team = matchup
            home_goalie = home_team.starting_goalie
            away_goalie = away_team.starting_goalie
            series_winner, total_games = simulate_series(matchup, home_goalie, away_goalie)
            series_winner.cup_win += 1
            cup_final_results.append(series_winner)

        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Round", "Home", "Visitor", "Winner", "Games"])

            # Round 1
            # Write round 1 matchups...
            for matchup, result in zip(round1_east_matchups, east_first_round_results):
                writer.writerow(["East Round 1", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Write round 1 matchups...
            for matchup, result in zip(round1_west_matchups, west_first_round_results):
                writer.writerow(["West Round 1", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Round 2
            # Write round 2 matchups...
            for matchup, result in zip(round2_east_matchups,east_second_round_results):
                writer.writerow(["East Round 2", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Write round 2 matchups...
            for matchup, result in zip(round2_west_matchups, west_second_round_results):
                writer.writerow(["West Round 2", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Conference Finals
            # Write conference final matchups...
            for matchup, result in zip(eastern_final, ecf_results):
                writer.writerow(["East Conference Finals", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Write conference final matchups...
            for matchup, result in zip(western_final, wcf_results):
                writer.writerow(["West Conference Finals", matchup[0].abrv, matchup[1].abrv, result[0].abrv, result[1]])

            # Cup Final
            # Write cup final matchup...
            for matchup, result in zip(cup_final, cup_final_results):
                writer.writerow(["Cup Final", matchup[0].abrv, matchup[1].abrv, result.abrv, total_games])

        return cup_final_results

    def playoffs(self, output_file):
        playoff_results = self.playoff_bracket(output_file)
        return playoff_results

    import csv

    def write_cup_winners(self, num_simulations):
        with open('output/playoff_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Team", "Playoff%", "Round 2%", "Conf Final%",
                 "Cup Final%", "Win Cup%"])

            for team in league:  # Assuming `league` is a list of team objects
                playoff_percentage = (team.playoffs / num_simulations) * 100
                second_round_percentage = (team.second_round / num_simulations) * 100
                conf_final_percentage = (team.conf_final / num_simulations) * 100
                cup_final_percentage = (team.cup_final / num_simulations) * 100
                cup_win_percentage = (team.cup_win / num_simulations) * 100

                writer.writerow(
                    [team.name, f"{playoff_percentage:.2f}%", f"{second_round_percentage:.2f}%",
                     f"{conf_final_percentage:.2f}%", f"{cup_final_percentage:.2f}%",
                     f"{cup_win_percentage:.2f}%"])

    def simulate_season(self, teams, matchups):
        self.reset_standings()
        self.reset_goalie_stats()
        for (team1_name, team2_name), num_games in matchups.items():
            team1 = teams[team1_name]
            team2 = teams[team2_name]
            for _ in range(num_games):
                team1_goalie = team1.select_goalie()
                team2_goalie = team2.select_goalie()
                game = Game(team1, team2, team1_goalie, team2_goalie)
                self.update_stats(game.home, game.visitor, game.home_sog, game.visitor_sog, game.home_goals,
                                  game.visitor_goals, game.winner, game.regulation, game.home_goalie,
                                  game.visitor_goalie)
                # self.log_game_result(game)
        # self.log_goalie_stats(sim_number)