from season import SeasonSimulator


if __name__ == "__main__":
    num_simulations = 1000
    playoff_statistics = []

    for i in range(num_simulations):
        simulator = SeasonSimulator()
        simulator.simulate_season()
        standings_output_file = f"output/standings.csv"
        simulator.sort_division_standings()
        output_file = f"output/playoffs.csv"
        playoff_results = simulator.playoffs(output_file)
        playoff_statistics.extend(playoff_results)
        simulator.write_cup_winners()
