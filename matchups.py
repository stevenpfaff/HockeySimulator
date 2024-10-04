import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('matchupsv2.csv')

# Create the matchups dictionary with results
matchups = []
for index, row in df.iterrows():
    away_team = row['away_team']
    home_team = row['home_team']
    visitor_goals = row['visitor_goals']
    home_goals = row['home_goals']

    # Append each game as a tuple (away_team, home_team, away_team_goals, home_team_goals)
    matchups.append((away_team, home_team, visitor_goals, home_goals))
