from season import SeasonSimulator
from team import teams
from matchups import matchups

if __name__ == "__main__":
    num_simulations = 10000
    playoff_statistics = []

    for i in range(1, num_simulations + 1):
        simulator = SeasonSimulator()
        simulator.simulate_season(teams, matchups)
        simulator.sort_division_standings(filename="output/standings.csv", sim_number=i)
        output_file = f"output/playoffs.csv"
        playoff_results = simulator.playoffs(output_file)
        playoff_statistics.extend(playoff_results)
        simulator.write_cup_winners()
