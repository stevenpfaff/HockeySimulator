class Team():
    def __init__(self, name, offense, defense, goalie):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.goalie = goalie

league = [
        Team("Anaheim Ducks", 50, 60, 20),
        Team("Arizona Coyotes", 40, 40, 30),
        Team("Boston Bruins", 50, 50, 70),
        Team("Buffalo Sabres", 50, 30, 50),
        Team("Calgary Flames", 40, 50, 30),
        Team("Carolina Hurricanes", 70, 80, 70),
        Team("Chicago Blackhawks", 20, 20, 40),
        Team("Colorado Avalanche", 70, 40, 50),
        Team("Columbus Blue Jackets", 40, 20, 40),
        Team("Dallas Stars", 60, 60, 50),
        Team("Detroit Red Wings", 30, 40, 50),
        Team("Edmonton Oilers", 80, 60, 60),
        Team("Florida Panthers", 60, 80, 70),
        Team("Los Angeles Kings", 60, 70, 60),
        Team("Minnesota Wild", 40, 70, 50),
        Team("Montreal Canadiens", 30, 30, 40),
        Team("Nashville Predators", 60, 60, 60),
        Team("New Jersey Devils", 70, 40, 30),
        Team("New York Islanders", 60, 40, 60),
        Team("New York Rangers", 40, 50, 60),
        Team("Ottawa Senators", 40, 50, 20),
        Team("Philadelphia Flyers", 50, 60, 20),
        Team("Pittsburgh Penguins", 70, 40, 50),
        Team("San Jose Sharks", 20, 20, 20),
        Team("Seattle Kraken", 40, 70, 70),
        Team("St. Louis Blues", 30, 30, 60),
        Team("Tampa Bay Lightning", 50, 50, 50),
        Team("Toronto Maple Leafs", 70, 50, 40),
        Team("Vancouver Canucks", 50, 60, 50),
        Team("Vegas Golden Knights", 60, 50, 50),
        Team("Washington Capitals", 30, 30, 40),
        Team("Winnipeg Jets", 60, 60, 80)]

for x in range(len(league)):
        print(league[x].name)
