from season import SeasonSimulator

if __name__ == "__main__":
    simulator = SeasonSimulator()
    simulator.simulate_season()
    output_file = "playoffs.csv"
    playoff_results = simulator.playoffs(output_file)
