import csv
import numpy as np
from collections import defaultdict

def calculate_team_percentiles(file_path, output_file):
    # Dictionary to hold data for each team
    team_stats = defaultdict(lambda: {'GF': [], 'GA': [], 'PTS': []})

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
            for stat in ['GF', 'GA', 'PTS']:
                if stat in row and row[stat].isdigit():
                    team_stats[team_name][stat].append(int(row[stat]))
                else:
                    print(f"Warning: '{stat}' column not found or invalid in row: {row}")

    # Open the output CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Team', 'Stat', '20th Percentile', '50th Percentile', '80th Percentile'])

        # Write the data for each team
        for team, stats in team_stats.items():
            for stat, values in stats.items():
                if values:
                    percentiles = np.percentile(values, [20, 50, 80])
                    writer.writerow([
                        team,
                        stat,
                        percentiles[0],
                        percentiles[1],
                        percentiles[2]
                    ])
                else:
                    writer.writerow([
                        team,
                        stat,
                        'No data',
                        'No data',
                        'No data'
                    ])

# Call the function with the path to your CSV file and the output file path
calculate_team_percentiles('standings.csv', 'team_percentiles.csv')
