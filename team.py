from goalie import goalies
import random
class Team(object):
    def __init__(self, name, offense, defense, starting_goalie, backup_goalie,
                 wins=0, losses=0, otl=0, points=0, playoffs=0,
                 second_round=0, conf_final=0, cup_final=0,
                 cup_win=0):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.starting_goalie = starting_goalie
        self.backup_goalie = backup_goalie
        self.wins = wins
        self.losses = losses
        self.otl = otl
        self.points = points
        self.playoffs = playoffs
        self.second_round = second_round
        self.conf_final = conf_final
        self.cup_final = cup_final
        self.cup_win = cup_win

    def select_goalie(self):
        probabilities = [0.65, 0.5]  # 65% for starting goalie, 35% for backup goalie
        selected_goalie = random.choices([self.starting_goalie, self.backup_goalie], weights=probabilities)[0]
        return selected_goalie

teams = {
    "ana": Team("Anaheim Ducks", 30, 30, goalies["gibson"], goalies["dostal"]),
    "bos": Team("Boston Bruins", 50, 50, goalies["swayman"], goalies["ullmark"]),
    "buf": Team("Buffalo Sabres", 50, 40, goalies["luukkonen"], goalies["levi"]),
    "cgy": Team("Calgary Flames", 40, 50, goalies["markstrom"], goalies["vladar"]),
    "car": Team("Carolina Hurricanes", 60, 80, goalies["andersen"], goalies["kochetkov"]),
    "chi": Team("Chicago Blackhawks", 20, 30, goalies["mrazek"], goalies["soderblom"]),
    "col": Team("Colorado Avalanche", 70, 50, goalies["georgiev"], goalies["annunen"]),
    "cbj": Team("Columbus Blue Jackets", 30, 20, goalies["merzlikins"], goalies["tarasov"]),
    "dal": Team("Dallas Stars", 70, 70, goalies["oettinger"], goalies["wedgewood"]),
    "det": Team("Detroit Red Wings", 40, 40, goalies["husso"], goalies["lyon"]),
    "edm": Team("Edmonton Oilers", 80, 60, goalies["skinner"], goalies["campbell"]),
    "fla": Team("Florida Panthers", 70, 70, goalies["bobrovsky"], goalies["stolarz"]),
    "la": Team("Los Angeles Kings", 60, 70, goalies["talbot"], goalies["rittich"]),
    "min": Team("Minnesota Wild", 50, 60, goalies["gustavsson"], goalies["fleury"]),
    "mtl": Team("Montreal Canadiens", 20, 30, goalies["montembeault"], goalies["primeau"]),
    "nsh": Team("Nashville Predators", 50, 60, goalies["askarov"], goalies["lankinen"]),
    "nj": Team("New Jersey Devils", 60, 40, goalies["allen"], goalies["kahkonen"]),
    "nyi": Team("New York Islanders", 40, 50, goalies["sorokin"], goalies["varlamov"]),
    "nyr": Team("New York Rangers", 50, 60, goalies["shesterkin"], goalies["quick"]),
    "ott": Team("Ottawa Senators", 40, 60, goalies["korp"], goalies["forsberg"]),
    "phi": Team("Philadelphia Flyers", 40, 60, goalies["fedotov"], goalies["ersson"]),
    "pit": Team("Pittsburgh Penguins", 50, 50, goalies["jarry"], goalies["ned"]),
    "sj": Team("San Jose Sharks", 20, 20, goalies["blackwood"], goalies["cooley"]),
    "sea": Team("Seattle Kraken", 30, 70, goalies["daccord"], goalies["grubauer"]),
    "stl": Team("St. Louis Blues", 40, 40, goalies["binner"], goalies["hofer"]),
    "tb": Team("Tampa Bay Lightning", 50, 50, goalies["vasy"], goalies["johansson"]),
    "tor": Team("Toronto Maple Leafs", 60, 50, goalies["saros"], goalies["woll"]),
    "ari": Team("Utah Mammoth", 40, 30, goalies["vemelka"], goalies["ingram"]),
    "van": Team("Vancouver Canucks", 60, 60, goalies["demko"], goalies["silvos"]),
    "vgk": Team("Vegas Golden Knights", 50, 60, goalies["hill"], goalies["thompson"]),
    "wsh": Team("Washington Capitals", 40, 50, goalies["lindgren"], goalies["kuemper"]),
    "wpg": Team("Winnipeg Jets", 50, 60, goalies["hellebuyck"], goalies["comrie"]),
}
metropolitan_division = [teams["car"],teams["cbj"],teams["phi"],teams["pit"],teams["nj"], teams["nyi"], teams["nyr"],teams["wsh"]]
atlantic_division = [teams["bos"], teams["buf"], teams["det"], teams["fla"], teams["mtl"], teams["ott"], teams["tb"], teams["tor"]]
central_division = [teams["ari"], teams["chi"], teams["col"], teams["dal"], teams["min"], teams["nsh"], teams["stl"], teams["wpg"]]
pacific_division = [teams["ana"], teams["cgy"], teams["edm"], teams["la"], teams["sj"], teams["sea"], teams["van"], teams["vgk"]]

eastern_conference = atlantic_division + metropolitan_division
western_conference = central_division + pacific_division

league = eastern_conference + western_conference