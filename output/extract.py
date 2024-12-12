import csv
import numpy as np
from collections import defaultdict
import re  # For cleaning non-numeric characters

def calculate_team_percentiles_and_average(file_path, output_file):
    # Dictionary to hold data for each team
    team_stats = defaultdict(lambda: {'GF': [], 'GA': [], 'PTS': [], "Regulation": []})

    # Dictionary to store the average points for each team
    team_average_points = {}

    # Helper function to clean and convert values to numbers
    def clean_numeric_value(value):
        if value:
            # Remove commas and other non-numeric characters
            clean_value = re.sub(r'[^\d.]', '', value)
            try:
                return float(clean_value) if '.' in clean_value else int(clean_value)
            except ValueError:
                return None
        return None

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

            # Collect data for each statistic, ensuring numeric conversion
            for stat in ['GF', 'GA', 'PTS']:
                value = clean_numeric_value(row.get(stat))
                if value is not None:
                    team_stats[team_name][stat].append(value)
                else:
                    print(f"Warning: Invalid or missing '{stat}' value in row: {row}")

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
        writer.writerow(['Team', 'Stat','0th Percentile', '25th Percentile', '50th Percentile (Median)', '75th Percentile', '100th Percentile', 'Average Points'])

        # Write the data for each team
        for team, stats in team_stats.items():
            for stat, values in stats.items():
                if values:
                    percentiles = np.percentile(values, [0, 25, 50, 75, 100])
                    average_points = team_average_points[team] if stat == 'PTS' else ''
                    writer.writerow([
                        team,
                        stat,
                        percentiles[0],
                        percentiles[1],
                        percentiles[2],
                        percentiles[3],
                        percentiles[4],
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