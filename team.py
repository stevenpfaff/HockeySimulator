from goalie import goalies
from skater import ducks_players,bruins_players,sabres_players,flames_players,hurricanes_players, blackhawks_players,avalanche_players,bluejackets_players,stars_players,redwings_players,oilers_players,panthers_players,kings_players,wild_players,canadiens_players,predators_players,devils_players,islanders_players,rangers_players,senators_players,flyers_players,penguins_players,sharks_players,kraken_players,blues_players,lightning_players,leafs_players,utah_players,canucks_players,knights_players,capitals_players,jets_players
import random
class Team:
    def __init__(self, name, abrv, offense, defense, starting_goalie, backup_goalie,
                 wins=0, regulation_wins=0, losses=0, otl=0, points=0, playoffs=0,
                 second_round=0, conf_final=0, cup_final=0,
                 cup_win=0):
        self.name = name
        self.abrv = abrv
        self.offense = offense
        self.defense = defense
        self.starting_goalie = starting_goalie
        self.backup_goalie = backup_goalie
        self.wins = wins
        self.regulation_wins = regulation_wins
        self.losses = losses
        self.otl = otl
        self.points = points
        self.playoffs = playoffs
        self.second_round = second_round
        self.conf_final = conf_final
        self.cup_final = cup_final
        self.cup_win = cup_win
        self.max_selections = 65
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def reset_selections(self):
        self.starting_goalie_selections = 0
        self.backup_goalie_selections = 0

    def select_goalie(self):
        total_rating = self.starting_goalie.rating + self.backup_goalie.rating

        # Calculate the probability for each goalie based on their ratings
        starting_goalie_probability = self.starting_goalie.rating / total_rating
        backup_goalie_probability = self.backup_goalie.rating / total_rating

        # Adjust probabilities to reflect a larger difference if there's a big gap in ratings
        rating_difference = abs(self.starting_goalie.rating - self.backup_goalie.rating)
        if (rating_difference > 10):
            adjustment_factor = rating_difference / 100
            starting_goalie_probability += adjustment_factor * starting_goalie_probability
            backup_goalie_probability -= adjustment_factor * backup_goalie_probability

        # Ensure the probabilities still sum to 1
        total_probability = starting_goalie_probability + backup_goalie_probability
        starting_goalie_probability /= total_probability
        backup_goalie_probability /= total_probability

        # Adjust probabilities based on the number of times goalies have been selected
        if self.starting_goalie_selections >= self.max_selections:
            starting_goalie_probability = 0
            backup_goalie_probability = 1
        elif self.backup_goalie_selections >= self.max_selections:
            starting_goalie_probability = 1
            backup_goalie_probability = 0
        else:
            total_selections = self.starting_goalie_selections + self.backup_goalie_selections
            if total_selections > 0:
                starting_goalie_probability *= (
                                                           self.max_selections - self.starting_goalie_selections) / self.max_selections
                backup_goalie_probability *= (self.max_selections - self.backup_goalie_selections) / self.max_selections

            # Re-normalize probabilities to sum to 1
            total_probability = starting_goalie_probability + backup_goalie_probability
            starting_goalie_probability /= total_probability
            backup_goalie_probability /= total_probability

        probabilities = [starting_goalie_probability, backup_goalie_probability]
        selected_goalie = random.choices([self.starting_goalie, self.backup_goalie], weights=probabilities)[0]

        # Update selection counts
        if selected_goalie == self.starting_goalie:
            self.starting_goalie_selections += 1
        else:
            self.backup_goalie_selections += 1

        return selected_goalie

    def get_goalie_by_name(self, goalie_name):
        # Compare the name to both starting and backup goalie
        if self.starting_goalie.name == goalie_name:
            return self.starting_goalie
        elif self.backup_goalie.name == goalie_name:
            return self.backup_goalie
        else:
            raise ValueError(f"Goalie {goalie_name} not found in team {self.name}")

def compute_team_ratings(players):
    total_weighted_offense = 0
    total_weighted_defense = 0
    total_offense_weights = 0
    total_defense_weights = 0

    for skater in players:
        role_weight = skater.role_weights.get(skater.role, 1.0)
        total_weighted_offense += (skater.shooting * 0.3 + skater.passing * 0.1 + skater.offense * 0.6) * role_weight
        total_weighted_defense += (skater.defense * 2) * role_weight

        total_offense_weights += (0.15 + 0.05 + 0.30) * role_weight
        total_defense_weights += .97 * role_weight

    weighted_avg_offense = total_weighted_offense / total_offense_weights
    weighted_avg_defense = total_weighted_defense / total_defense_weights

    return weighted_avg_offense, weighted_avg_defense

# Compute team ratings
ana_offense, ana_defense = compute_team_ratings(ducks_players)
bos_offense, bos_defense = compute_team_ratings(bruins_players)
buf_offense, buf_defense = compute_team_ratings(sabres_players)
cgy_offense, cgy_defense = compute_team_ratings(flames_players)
car_offense, car_defense = compute_team_ratings(hurricanes_players)
chi_offense, chi_defense = compute_team_ratings(blackhawks_players)
col_offense, col_defense = compute_team_ratings(avalanche_players)
cbj_offense, cbj_defense = compute_team_ratings(bluejackets_players)
dal_offense, dal_defense = compute_team_ratings(stars_players)
det_offense, det_defense = compute_team_ratings(redwings_players)
edm_offense, edm_defense = compute_team_ratings(oilers_players)
fla_offense, fla_defense = compute_team_ratings(panthers_players)
la_offense, la_defense = compute_team_ratings(kings_players)
min_offense, min_defense = compute_team_ratings(wild_players)
mtl_offense, mtl_defense = compute_team_ratings(canadiens_players)
nsh_offense, nsh_defense = compute_team_ratings(predators_players)
nj_offense, nj_defense = compute_team_ratings(devils_players)
nyi_offense, nyi_defense = compute_team_ratings(islanders_players)
nyr_offense, nyr_defense = compute_team_ratings(rangers_players)
ott_offense, ott_defense = compute_team_ratings(senators_players)
phi_offense, phi_defense = compute_team_ratings(flyers_players)
pit_offense, pit_defense = compute_team_ratings(penguins_players)
sj_offense, sj_defense = compute_team_ratings(sharks_players)
sea_offense, sea_defense = compute_team_ratings(kraken_players)
stl_offense, stl_defense = compute_team_ratings(blues_players)
tb_offense, tb_defense = compute_team_ratings(lightning_players)
tor_offense, tor_defense = compute_team_ratings(leafs_players)
ut_offense, ut_defense = compute_team_ratings(utah_players)
van_offense, van_defense = compute_team_ratings(canucks_players)
vgk_offense, vgk_defense = compute_team_ratings(knights_players)
wsh_offense, wsh_defense = compute_team_ratings(capitals_players)
wpg_offense, wpg_defense = compute_team_ratings(jets_players)

# Create team objects
teams = {
    "ana": Team("Anaheim Ducks", "ANA", ana_offense, ana_defense, goalies["gibson"], goalies["dostal"]),
    "bos": Team("Boston Bruins", "BOS", bos_offense, bos_defense, goalies["swayman"], goalies["korp"]),
    "buf": Team("Buffalo Sabres", "BUF", buf_offense, buf_defense, goalies["luukkonen"], goalies["levi"]),
    "cgy": Team("Calgary Flames", "CGY", cgy_offense, cgy_defense, goalies["wolf"], goalies["vladar"]),
    "car": Team("Carolina Hurricanes", "CAR", car_offense, car_defense, goalies["andersen"], goalies["kochetkov"]),
    "chi": Team("Chicago Blackhawks", "CHI", chi_offense, chi_defense, goalies["mrazek"], goalies["brossoit"]),
    "col": Team("Colorado Avalanche", "COL", col_offense, col_defense, goalies["georgiev"], goalies["annunen"]),
    "cbj": Team("Columbus Blue Jackets", "CBJ", cbj_offense, cbj_defense, goalies["merzlikins"], goalies["tarasov"]),
    "dal": Team("Dallas Stars", "DAL", dal_offense, dal_defense, goalies["oettinger"], goalies["desmith"]),
    "det": Team("Detroit Red Wings", "DET", det_offense, det_defense, goalies["husso"], goalies["talbot"]),
    "edm": Team("Edmonton Oilers", "EDM", edm_offense, edm_defense, goalies["skinner"], goalies["pickard"]),
    "fla": Team("Florida Panthers", "FLA", fla_offense, fla_defense, goalies["bobrovsky"], goalies["knight"]),
    "la": Team("Los Angeles Kings", "LA", la_offense, la_defense, goalies["kuemper"], goalies["rittich"]),
    "min": Team("Minnesota Wild", "MIN", min_offense, min_defense, goalies["gustavsson"], goalies["fleury"]),
    "mtl": Team("Montreal Canadiens", "MTL", mtl_offense, mtl_defense, goalies["montembeault"], goalies["primeau"]),
    "nsh": Team("Nashville Predators", "NSH", nsh_offense, nsh_defense, goalies["saros"], goalies["wedgewood"]),
    "nj": Team("New Jersey Devils", "NJ", nj_offense, nj_defense, goalies["markstrom"], goalies["allen"]),
    "nyi": Team("New York Islanders", "NYI", nyi_offense, nyi_defense, goalies["sorokin"], goalies["varlamov"]),
    "nyr": Team("New York Rangers", "NYR", nyr_offense, nyr_defense, goalies["shesterkin"], goalies["quick"]),
    "ott": Team("Ottawa Senators", "OTT", ott_offense, ott_defense, goalies["ullmark"], goalies["forsberg"]),
    "phi": Team("Philadelphia Flyers", "PHI", phi_offense, phi_defense, goalies["fedotov"], goalies["ersson"]),
    "pit": Team("Pittsburgh Penguins", "PIT", pit_offense, pit_defense, goalies["jarry"], goalies["ned"]),
    "sj": Team("San Jose Sharks", "SJ", sj_offense, sj_defense, goalies["blackwood"], goalies["vanacek"]),
    "sea": Team("Seattle Kraken", "SEA", sea_offense, sea_defense, goalies["daccord"], goalies["grubauer"]),
    "stl": Team("St. Louis Blues", "STL", stl_offense, stl_defense, goalies["binner"], goalies["hofer"]),
    "tb": Team("Tampa Bay Lightning", "TB", tb_offense, tb_defense, goalies["vasy"], goalies["johansson"]),
    "tor": Team("Toronto Maple Leafs", "TOR", tor_offense, tor_defense, goalies["woll"], goalies["stolarz"]),
    "ari": Team("Utah Hockey Club", "UT", ut_offense, ut_defense, goalies["vemelka"], goalies["ingram"]),
    "van": Team("Vancouver Canucks", "VAN", van_offense, van_defense, goalies["demko"], goalies["silvos"]),
    "vgk": Team("Vegas Golden Knights", "VGK", vgk_offense, vgk_defense, goalies["hill"], goalies["samsonov"]),
    "wsh": Team("Washington Capitals", "WSH", wsh_offense, wsh_defense, goalies["lindgren"], goalies["thompson"]),
    "wpg": Team("Winnipeg Jets", "WPG", wpg_offense, wpg_defense, goalies["hellebuyck"], goalies["kahkonen"]),
}

teams["ana"].players = ducks_players
teams["bos"].players = bruins_players
teams["buf"].players = sabres_players
teams["cgy"].players = flames_players
teams["car"].players = hurricanes_players
teams["chi"].players = blackhawks_players
teams["col"].players = avalanche_players
teams["cbj"].players = bluejackets_players
teams["dal"].players = stars_players
teams["det"].players = redwings_players
teams["edm"].players = oilers_players
teams["fla"].players = panthers_players
teams["la"].players = kings_players
teams["min"].players = wild_players
teams["mtl"].players = canadiens_players
teams["nsh"].players = predators_players
teams["nj"].players = devils_players
teams["nyi"].players = islanders_players
teams["nyr"].players = rangers_players
teams["ott"].players = senators_players
teams["phi"].players = flyers_players
teams["pit"].players = penguins_players
teams["sj"].players = sharks_players
teams["sea"].players = kraken_players
teams["stl"].players = blues_players
teams["tb"].players = lightning_players
teams["tor"].players = leafs_players
teams["ari"].players = utah_players
teams["van"].players = canucks_players
teams["vgk"].players = knights_players
teams["wsh"].players = capitals_players
teams["wpg"].players = jets_players

print(f"ANA {ana_offense:.1f} {ana_defense:.1f}")
print(f"BOS {bos_offense:.1f} {bos_defense:.1f}")
print(f"BUF {buf_offense:.1f} {buf_defense:.1f}")
print(f"CGY {cgy_offense:.1f} {cgy_defense:.1f}")
print(f"CAR {car_offense:.1f} {car_defense:.1f}")
print(f"CHI {chi_offense:.1f} {chi_defense:.1f}")
print(f"COL {col_offense:.1f} {col_defense:.1f}")
print(f"CBJ {cbj_offense:.1f} {cbj_defense:.1f}")
print(f"DAL {dal_offense:.1f} {dal_defense:.1f}")
print(f"DET {det_offense:.1f} {det_defense:.1f}")
print(f"EDM {edm_offense:.1f} {edm_defense:.1f}")
print(f"FLA {fla_offense:.1f} {fla_defense:.1f}")
print(f"LA {la_offense:.1f} {la_defense:.1f}")
print(f"MIN {min_offense:.1f} {min_defense:.1f}")
print(f"MTL {mtl_offense:.1f} {mtl_defense:.1f}")
print(f"NSH {nsh_offense:.1f} {nsh_defense:.1f}")
print(f"NJ {nj_offense:.1f} {nj_defense:.1f}")
print(f"NYI {nyi_offense:.1f} {nyi_defense:.1f}")
print(f"NYR {nyr_offense:.1f} {nyr_defense:.1f}")
print(f"OTT {ott_offense:.1f} {ott_defense:.1f}")
print(f"PHI {phi_offense:.1f} {phi_defense:.1f}")
print(f"PIT {pit_offense:.1f} {pit_defense:.1f}")
print(f"SJ {sj_offense:.1f} {sj_defense:.1f}")
print(f"SEA {sea_offense:.1f} {sea_defense:.1f}")
print(f"STL {stl_offense:.1f} {stl_defense:.1f}")
print(f"TB {tb_offense:.1f} {tb_defense:.1f}")
print(f"TOR {tor_offense:.1f} {tor_defense:.1f}")
print(f"UT {ut_offense:.1f} {ut_defense:.1f}")
print(f"VAN {van_offense:.1f} {van_defense:.1f}")
print(f"VGK {vgk_offense:.1f} {vgk_defense:.1f}")
print(f"WSH {wsh_offense:.1f} {wsh_defense:.1f}")
print(f"WPG {wpg_offense:.1f} {wpg_defense:.1f}")

# Define divisions
metropolitan_division = [teams["car"], teams["cbj"], teams["phi"], teams["pit"], teams["nj"], teams["nyi"], teams["nyr"], teams["wsh"]]
atlantic_division = [teams["bos"], teams["buf"], teams["det"], teams["fla"], teams["mtl"], teams["ott"], teams["tb"], teams["tor"]]
central_division = [teams["ari"], teams["chi"], teams["col"], teams["dal"], teams["min"], teams["nsh"], teams["stl"], teams["wpg"]]
pacific_division = [teams["ana"], teams["cgy"], teams["edm"], teams["la"], teams["sj"], teams["sea"], teams["van"], teams["vgk"]]

eastern_conference = atlantic_division + metropolitan_division
western_conference = central_division + pacific_division

league = eastern_conference + western_conference