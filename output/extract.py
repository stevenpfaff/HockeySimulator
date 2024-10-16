import csv
import numpy as np
from collections import defaultdict


def calculate_team_percentiles_and_average(file_path, output_file):
    # Dictionary to hold data for each team
    team_stats = defaultdict(lambda: {'GF': [], 'GA': [], 'PTS': [], "Regulation": []})

    # Dictionary to store the average points for each team
    team_average_points = {}

    # Open the input CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        # Skip the first two rows if headers are in the third row
        for _ in range(2):
            next(reader)

        # Now the third row should be treated as headers, and subsequent rows as data
        for row in reader:
            team_name = row.get('Team')  # Adjust the key if your CSV has a different team name column
            if not team_name:
                continue

            # Collect data for each statistic
            for stat in ['PTS']:
                if stat in row and row[stat].isdigit():
                    team_stats[team_name][stat].append(int(row[stat]))
                else:
                    print(f"Warning: '{stat}' column not found or invalid in row: {row}")

    # Calculate the average points (PTS) for each team
    for team, stats in team_stats.items():
        pts_values = stats['PTS']
        if pts_values:
            team_average_points[team] = np.mean(pts_values)
        else:
            team_average_points[team] = 'No data'

    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Team', 'Average Points'])

        # Write the data for each team
        for team, stats in team_stats.items():
            for stat, values in stats.items():
                if values:
                    percentiles = np.percentile(values, [25, 50, 75])
                    average_points = team_average_points[team] if stat == 'PTS' else ''
                    writer.writerow([
                        team,
                        stat,
                        percentiles[0],
                        percentiles[1],
                        percentiles[2],
                        average_points if average_points != '' else ''  # Only show average for PTS stat
                    ])
                else:
                    writer.writerow([
                        team,
                        stat,
                        'No data',
                        'No data',
                        'No data',
                        ''
                    ])


# Call the function with the path to your CSV file and the output file path
calculate_team_percentiles_and_average('standings.csv', 'team_percentiles_with_average.csv')

def calculate_simulation_percentiles(file_path, output_file):
    # Dictionary to hold simulation data for each player
    player_simulations = defaultdict(lambda: {'Goals': [], 'Assists': [], 'Points': []})

    # Open the input CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        # Read the rows for player simulation outcomes
        for row in reader:
            player_name = row.get('Name')  # Adjust the key if your CSV has a different player name column
            if not player_name:
                continue

            # Collect data for each statistic
            for stat in ['Goals', 'Assists', 'Points']:
                if stat in row and row[stat].isdigit():
                    player_simulations[player_name][stat].append(int(row[stat]))
                else:
                    print(f"Warning: '{stat}' column not found or invalid in row: {row}")

    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Player', 'Stat', '1st Percentile', '50th Percentile (Median)', '100th Percentile'])

        # Write the percentile data for each player
        for player, stats in player_simulations.items():
            for stat, values in stats.items():
                if values:
                    percentiles = np.percentile(values, [1, 50, 100])  # Calculate 25th, 50th (median), and 75th percentiles
                    writer.writerow([player, stat, percentiles[0], percentiles[1], percentiles[2]])
                else:
                    writer.writerow([player, stat, 'No data', 'No data', 'No data'])

# Call the function with the path to your CSV file and the output file path
calculate_simulation_percentiles('skater_stats.csv', 'skater_percentiles.csv')