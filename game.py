import random
from skater import Skater
import csv

class Game:
    def __init__(self, home_team, away_team, home_goalie, away_goalie):
        self.home = home_team
        self.visitor = away_team
        self.home_goalie = home_goalie
        self.visitor_goalie = away_goalie
        self.home_sog = self.__get_sog(self.home.offense, self.visitor.defense)
        self.visitor_sog = self.__get_sog(self.visitor.offense, self.home.defense)
        self.home_goals = self.__get_goals(self.home_sog, self.visitor_goalie.rating)
        self.visitor_goals = self.__get_goals(self.visitor_sog, self.home_goalie.rating)
        self.winner, self.regulation = self.__get_winner()
        self.goal_assist_data = []

    @staticmethod
    def find_closest_value(value, keys):
        return min(keys, key=lambda k: abs(k - value))

    @classmethod
    def __get_sog(cls, offense, defense, home_team=False):
        # Dictionary mapping offense ranges to defense ranges and corresponding SOG ranges
        ranges = [
            (80, [(80, (15, 38)), (85, (15, 35)), (90, (15, 32)), (95, (15, 30)), (100, (15, 28)), (105, (15, 25)),
                  (110, (14, 25))]),
            (85, [(80, (16, 40)), (85, (16, 38)), (90, (16, 35)), (95, (16, 32)), (100, (16, 30)), (105, (16, 28)),
                  (110, (15, 28))]),
            (90, [(80, (17, 40)), (85, (17, 38)), (90, (17, 35)), (95, (17, 32)), (100, (17, 30)), (105, (17, 28)),
                  (110, (16, 28))]),
            (95, [(80, (18, 40)), (85, (18, 38)), (90, (18, 36)), (95, (18, 35)), (100, (18, 32)), (105, (18, 30)),
                  (110, (17, 30))]),
            (100, [(80, (19, 40)), (85, (19, 38)), (90, (19, 36)), (95, (19, 35)), (100, (19, 34)), (105, (19, 32)),
                   (110, (18, 31))]),
            (102, [(80, (20, 40)), (85, (20, 38)), (90, (20, 36)), (95, (20, 36)), (100, (20, 34)), (105, (20, 32)),
                   (110, (18, 32))]),
            (105, [(80, (21, 42)), (85, (21, 40)), (90, (21, 38)), (95, (21, 36)), (100, (20, 35)), (105, (20, 32)),
                   (110, (19, 32))]),
            (107, [(80, (22, 45)), (85, (22, 42)), (90, (22, 40)), (95, (22, 38)), (100, (22, 35)), (105, (22, 32)),
                   (110, (20, 32))]),
            (110, [(80, (23, 46)), (85, (23, 45)), (90, (23, 42)), (95, (23, 40)), (100, (23, 38)), (105, (23, 35)),
                   (110, (22, 34))]),
            (115, [(80, (24, 48)), (85, (24, 46)), (90, (24, 45)), (95, (24, 42)), (100, (24, 40)), (105, (24, 38)),
                   (110, (23, 35))])
        ]

        # Find the closest offense and defense ranges
        closest_offense = min(ranges, key=lambda x: abs(x[0] - offense))
        closest_defense = min(closest_offense[1], key=lambda x: abs(x[0] - defense))

        # Extract the min and max SOG values
        sog_min, sog_max = closest_defense[1]

        # Apply home-ice advantage: If home team, increase SOG range slightly
        if home_team:
            sog_min += 1  # Slight boost for the home team
            sog_max += 1  # Slight boost for the home team

        # Generate the random SOG value within the adjusted range
        sog = random.randint(sog_min, sog_max)

        return sog

        def get_random_value(offense_val, defense_val):
            for o_max, defense_ranges in ranges:
                if offense_val <= o_max:
                    for d_threshold, value_range in defense_ranges:
                        if defense_val <= d_threshold:
                            return random.randint(*value_range)
            return 0

        return get_random_value(offense, defense)

    def __get_goals(self, sog, goalie_rating):
        goals = 0
        for _ in range(sog):
            probability = self.get_goal_probability(goalie_rating)
            if random.random() <= probability:
                goals += 1
        return goals


    @staticmethod
    def get_goal_probability(goalie_rating):
        threshold = 20  # Example threshold, adjust as needed
        if goalie_rating <= threshold:
            return 0.115
        elif goalie_rating > threshold and goalie_rating <= 30:
            return 0.110
        elif goalie_rating > 30 and goalie_rating <= 40:
            return 0.105
        elif goalie_rating > 40 and goalie_rating <= 45:
            return 0.102
        elif goalie_rating > 45 and goalie_rating <= 50:
            return 0.100
        elif goalie_rating > 50 and goalie_rating <= 55:
            return 0.097
        elif goalie_rating > 55 and goalie_rating <= 60:
            return 0.095
        elif goalie_rating > 60 and goalie_rating <= 70:
            return 0.092
        elif goalie_rating > 70 and goalie_rating <= 80:
            return 0.090
        elif goalie_rating > 80:
            return 0.085

    def __get_winner(self):
        team1_goals = self.home_goals
        team2_goals = self.visitor_goals
        regulation = True  # By default, assume regulation unless overtime is triggered

        # Check for a tie to enter overtime
        if team1_goals == team2_goals:
            regulation = False  # Game went to overtime
            # Simulate overtime/shootout until a winner is determined
            while team1_goals == team2_goals:
                goal1 = random.random()  # Randomize goal for home team
                goal2 = random.random()  # Randomize goal for away team
                if goal1 > goal2:
                    team1_goals += 1  # Home team scores in OT
                else:
                    team2_goals += 1  # Away team scores in OT

        # Determine winner based on final goals
        if team1_goals > team2_goals:
            self.home_goals = team1_goals  # Update final home team goals
            self.visitor_goals = team2_goals  # Update final away team goals
            return self.home, regulation  # Home team wins, return regulation status
        else:
            self.home_goals = team1_goals  # Update final home team goals
            self.visitor_goals = team2_goals  # Update final away team goals
            return self.visitor, regulation  # Away team wins, return regulation status

    def assign_goals_and_assists(self):
        # Assign goals to the home team players
        self.assign_team_goals_and_assists(self.home, self.home_goals)

        # Assign goals to the visitor team players
        self.assign_team_goals_and_assists(self.visitor, self.visitor_goals)

        # Debugging: Print all collected goal and assist data after processing all skaters
        print("Final Goal and Assist Data:", self.goal_assist_data)

    def assign_team_goals_and_assists(self, team, goals):
        """ Assign goals and assists to the players on the team """
        goals = int(goals)  # Ensure goals is an integer

        if goals == 0:
            print(f"No goals to assign for {team.name}.")
            return  # No goals to assign

        players = team.players
        if not players:
            print(f"No players available for {team.name}.")
            return  # No players to assign goals or assists to

        print(f"Assigning {goals} goals for {team.name}.")

        # Ensure valid role weights for each player
        role_weights = [
            Skater.role_weights.get(skater.role, 0.2)  # Default to a low weight if role is missing
            for skater in players
        ]

        for _ in range(goals):  # Iterate through each goal to be assigned
            # Randomly choose a goal scorer based on role weights
            goal_scorer = random.choices(players, weights=role_weights, k=1)[0]
            goal_scorer.update_stats(goals=1)
            print(f"Goal scored by {goal_scorer.name} for {team.name}.")

            # Now assign 1 or 2 assists (if possible) from the remaining players
            possible_assist_players = [p for p in players if p != goal_scorer]
            if possible_assist_players:
                assist_weights = [Skater.role_weights.get(skater.role, 0.2) * skater.passing for skater in
                                  possible_assist_players]

                # Select up to two players for assists
                assists_given = random.choices(possible_assist_players, weights=assist_weights,
                                               k=min(2, len(possible_assist_players)))

                # Update assist stats for the chosen players
                for assist_player in assists_given:
                    assist_player.update_stats(assists=1)

                # Save the goal and assist data for each event
                self.goal_assist_data.append({
                    'goal_scorer': goal_scorer.name,
                    'assists': [player.name for player in assists_given]
                })
                print(f"Assists for goal by {goal_scorer.name}: {[player.name for player in assists_given]}")

    def save_to_csv(self, filename='game_stats.csv'):
        if not self.goal_assist_data:
            print("No goal assist data to save.")
            return

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Skater", "Goals", "Assists"])
            writer.writerows(self.goal_assist_data)