import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('simulated-points.csv')

# Strip whitespace from column names
df.columns = df.columns.str.strip()


# Create the matchups dictionary with results
matchups = []
for index, row in df.iterrows():
    away_team = row['away_team']
    home_team = row['home_team']
    visitor_goals = row['visitor_goals']
    home_goals = row['home_goals']
    visitor_sog = row['visitor_sog']
    home_sog = row['home_sog']
    regulation = row['regulation']
    winner = row['winner']
    visitor_goalie = row['visitor_goalie']
    home_goalie = row['home_goalie']

    matchups.append((away_team, home_team, visitor_goals, home_goals, visitor_sog, home_sog, regulation, winner, visitor_goalie, home_goalie))
