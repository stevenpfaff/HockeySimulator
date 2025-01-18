from goalie import goalies
from skater import ducks_players,bruins_players,sabres_players,flames_players,hurricanes_players, blackhawks_players,avalanche_players,bluejackets_players,stars_players,redwings_players,oilers_players,panthers_players,kings_players,wild_players,canadiens_players,predators_players,devils_players,islanders_players,rangers_players,senators_players,flyers_players,penguins_players,sharks_players,kraken_players,blues_players,lightning_players,leafs_players,utah_players,canucks_players,knights_players,capitals_players,jets_players
import csv
import random

class Team:
    def __init__(self, name, abrv, offense, defense, powerplay, penaltykill, penalty, starting_goalie, backup_goalie, third_goalie=None, fourth_goalie=None,
                 wins=0, regulation_wins=0, losses=0, otl=0, points=0, playoffs=0,
                 second_round=0, conf_final=0, cup_final=0, cup_win=0):
        self.name = name
        self.abrv = abrv
        self.offense = offense
        self.defense = defense
        self.powerplay = powerplay
        self.penaltykill = penaltykill
        self.penalty = penalty
        self.starting_goalie = starting_goalie
        self.backup_goalie = backup_goalie
        self.third_goalie = third_goalie
        self.fourth_goalie = fourth_goalie
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
        self.max_selections = 32
        self.players = []
        self.reset_selections()  # Ensure goalie selections are initialized

    def reset_selections(self):
        self.starting_goalie_selections = 0
        self.backup_goalie_selections = 0
        self.third_goalie_selections = 0
        self.fourth_goalie_selections = 0

    def select_goalie(self):
        # Define a base priority based on role
        goalie_priority = {
            "Starter": 3,
            "1A": 2.5,
            "1B": 2.4,
            "Backup": 1.5,
            "Third": 0.5,
            "Inactive": 0.000000001
        }

        # Gather available goalies
        goalies = [self.starting_goalie, self.backup_goalie]
        if self.third_goalie:
            goalies.append(self.third_goalie)
        if self.fourth_goalie:
            goalies.append(self.fourth_goalie)

        # Calculate total rating with role adjustments
        total_priority = sum([goalie.rating * goalie_priority[goalie.role] for goalie in goalies])

        # Calculate probabilities based on adjusted ratings
        goalie_probabilities = [(goalie.rating * goalie_priority[goalie.role]) / total_priority for goalie in goalies]

        # Adjust probabilities based on the number of starts each goalie has already had
        total_selections = (
            self.starting_goalie_selections +
            self.backup_goalie_selections +
            (self.third_goalie_selections if self.third_goalie else 0) +
            (self.fourth_goalie_selections if self.fourth_goalie else 0)
        )

        if self.starting_goalie_selections >= self.max_selections:
            goalie_probabilities[0] = 0
        if self.backup_goalie_selections >= self.max_selections:
            goalie_probabilities[1] = 0
        if self.third_goalie and self.third_goalie_selections >= self.max_selections:
            goalie_probabilities[2] = 0
        if self.fourth_goalie and self.fourth_goalie_selections >= self.max_selections:
            goalie_probabilities[3] = 0

        # Re-normalize probabilities after adjustment
        total_probability = sum(goalie_probabilities)
        if total_probability > 0:
            goalie_probabilities = [prob / total_probability for prob in goalie_probabilities]

        # Select a goalie based on the adjusted probabilities
        selected_goalie = random.choices(goalies, weights=goalie_probabilities)[0]

        # Update selection counts based on the chosen goalie
        if selected_goalie == self.starting_goalie:
            self.starting_goalie_selections += 1
        elif selected_goalie == self.backup_goalie:
            self.backup_goalie_selections += 1
        elif self.third_goalie and selected_goalie == self.third_goalie:
            self.third_goalie_selections += 1
        elif self.fourth_goalie and selected_goalie == self.fourth_goalie:
            self.fourth_goalie_selections += 1

        return selected_goalie

    def get_goalie_by_name(self, goalie_name):
        if self.starting_goalie.name == goalie_name:
            return self.starting_goalie
        elif self.backup_goalie.name == goalie_name:
            return self.backup_goalie
        elif self.third_goalie and self.third_goalie.name == goalie_name:
            return self.third_goalie
        elif self.fourth_goalie and self.fourth_goalie.name == goalie_name:
            return self.fourth_goalie
        else:
            raise ValueError(f"Goalie {goalie_name} not found in team {self.name}")



def compute_team_ratings(players):
    total_weighted_offense = 0
    total_weighted_defense = 0
    total_weighted_powerplay = 0
    total_weighted_penaltykill = 0
    total_weighted_penalty = 0
    total_role_weight = 0
    total_pp_weight = 0
    total_pk_weight = 0
    total_penalty_weight = 0

    for skater in players:
        # Use the appropriate role weights based on whether they’re for even-strength or special teams
        role_weight = skater.get_role_weight()

        # Calculate weighted offensive and defensive scores
        total_weighted_offense += skater.offensive_overall() * role_weight
        total_weighted_defense += skater.defensive_overall() * role_weight
        total_role_weight += role_weight

        # Powerplay and penalty kill contributions, if applicable
        if skater.powerplay is not None:
            total_weighted_powerplay += skater.powerplay * role_weight
            total_pp_weight += role_weight
        if skater.penaltykill is not None:
            total_weighted_penaltykill += skater.penaltykill * role_weight
            total_pk_weight += role_weight

        # Penalties taken by the skater, contributing to the penalty rating
        if skater.penalties is not None:
            total_weighted_penalty += skater.penalties * role_weight
            total_penalty_weight += role_weight

    # Calculate team ratings by averaging the weighted scores
    team_offensive_rating = total_weighted_offense / total_role_weight if total_role_weight > 0 else 0
    team_defensive_rating = total_weighted_defense / total_role_weight if total_role_weight > 0 else 0
    team_powerplay_rating = total_weighted_powerplay / total_pp_weight if total_pp_weight > 0 else 0
    team_penaltykill_rating = total_weighted_penaltykill / total_pk_weight if total_pk_weight > 0 else 0
    team_penalty_rating = total_weighted_penalty / total_penalty_weight if total_penalty_weight > 0 else 0

    return team_offensive_rating, team_defensive_rating, team_powerplay_rating, team_penaltykill_rating, team_penalty_rating





# Compute team ratings
ana_offense, ana_defense, ana_powerplay, ana_penaltykill, ana_penalty = compute_team_ratings(ducks_players)
bos_offense, bos_defense, bos_powerplay, bos_penaltykill, bos_penalty = compute_team_ratings(bruins_players)
buf_offense, buf_defense, buf_powerplay, buf_penaltykill, buf_penalty = compute_team_ratings(sabres_players)
cgy_offense, cgy_defense, cgy_powerplay, cgy_penaltykill, cgy_penalty = compute_team_ratings(flames_players)
car_offense, car_defense, car_powerplay, car_penaltykill, car_penalty = compute_team_ratings(hurricanes_players)
chi_offense, chi_defense, chi_powerplay, chi_penaltykill, chi_penalty = compute_team_ratings(blackhawks_players)
col_offense, col_defense, col_powerplay, col_penaltykill, col_penalty = compute_team_ratings(avalanche_players)
cbj_offense, cbj_defense, cbj_powerplay, cbj_penaltykill, cbj_penalty = compute_team_ratings(bluejackets_players)
dal_offense, dal_defense, dal_powerplay, dal_penaltykill, dal_penalty = compute_team_ratings(stars_players)
det_offense, det_defense, det_powerplay, det_penaltykill, det_penalty = compute_team_ratings(redwings_players)
edm_offense, edm_defense, edm_powerplay, edm_penaltykill, edm_penalty = compute_team_ratings(oilers_players)
fla_offense, fla_defense, fla_powerplay, fla_penaltykill, fla_penalty = compute_team_ratings(panthers_players)
la_offense, la_defense, la_powerplay, la_penaltykill, la_penalty = compute_team_ratings(kings_players)
min_offense, min_defense, min_powerplay, min_penaltykill, min_penalty = compute_team_ratings(wild_players)
mtl_offense, mtl_defense, mtl_powerplay, mtl_penaltykill, mtl_penalty = compute_team_ratings(canadiens_players)
nsh_offense, nsh_defense, nsh_powerplay, nsh_penaltykill, nsh_penalty = compute_team_ratings(predators_players)
nj_offense, nj_defense, nj_powerplay, nj_penaltykill, nj_penalty = compute_team_ratings(devils_players)
nyi_offense, nyi_defense, nyi_powerplay, nyi_penaltykill, nyi_penalty = compute_team_ratings(islanders_players)
nyr_offense, nyr_defense, nyr_powerplay, nyr_penaltykill, nyr_penalty = compute_team_ratings(rangers_players)
ott_offense, ott_defense, ott_powerplay, ott_penaltykill, ott_penalty = compute_team_ratings(senators_players)
phi_offense, phi_defense, phi_powerplay, phi_penaltykill, phi_penalty = compute_team_ratings(flyers_players)
pit_offense, pit_defense, pit_powerplay, pit_penaltykill, pit_penalty = compute_team_ratings(penguins_players)
sj_offense, sj_defense, sj_powerplay, sj_penaltykill, sj_penalty = compute_team_ratings(sharks_players)
sea_offense, sea_defense, sea_powerplay, sea_penaltykill, sea_penalty = compute_team_ratings(kraken_players)
stl_offense, stl_defense, stl_powerplay, stl_penaltykill, stl_penalty = compute_team_ratings(blues_players)
tb_offense, tb_defense, tb_powerplay, tb_penaltykill, tb_penalty = compute_team_ratings(lightning_players)
tor_offense, tor_defense, tor_powerplay, tor_penaltykill, tor_penalty = compute_team_ratings(leafs_players)
ut_offense, ut_defense, ut_powerplay, ut_penaltykill, ut_penalty = compute_team_ratings(utah_players)
van_offense, van_defense, van_powerplay, van_penaltykill, van_penalty = compute_team_ratings(canucks_players)
vgk_offense, vgk_defense, vgk_powerplay, vgk_penaltykill, vgk_penalty = compute_team_ratings(knights_players)
wsh_offense, wsh_defense, wsh_powerplay, wsh_penaltykill, wsh_penalty = compute_team_ratings(capitals_players)
wpg_offense, wpg_defense, wpg_powerplay, wpg_penaltykill, wpg_penalty = compute_team_ratings(jets_players)

# Create team objects
teams = {
    "ana": Team("Anaheim Ducks", "ANA", ana_offense, ana_defense, ana_powerplay, ana_penaltykill, ana_penalty, goalies["gibson"], goalies["dostal"], goalies["reimer"]),
    "bos": Team("Boston Bruins", "BOS", bos_offense, bos_defense, bos_powerplay,bos_penaltykill, bos_penalty, goalies["swayman"], goalies["korp"]),
    "buf": Team("Buffalo Sabres", "BUF", buf_offense, buf_defense, buf_powerplay, buf_penaltykill, buf_penalty, goalies["luukkonen"], goalies["levi"], goalies["reimerbuf"]),
    "cgy": Team("Calgary Flames", "CGY", cgy_offense, cgy_defense, cgy_powerplay, cgy_penaltykill, cgy_penalty,  goalies["wolf"], goalies["vladar"]),
    "car": Team("Carolina Hurricanes", "CAR", car_offense, car_defense, car_powerplay, car_penaltykill, car_penalty, goalies["andersen"], goalies["kochetkov"], goalies["martin"], goalies["tokarski"]),
    "chi": Team("Chicago Blackhawks", "CHI", chi_offense, chi_defense, chi_powerplay, chi_penaltykill, chi_penalty, goalies["mrazek"], goalies["brossoit"], goalies["soderblom"], goalies["commesso"]),
    "col": Team("Colorado Avalanche", "COL", col_offense, col_defense, col_powerplay, col_penaltykill, col_penalty, goalies["blackwoodcol"], goalies["wedgewoodcol"],goalies["annunen"],goalies["georgiev"]),
    "cbj": Team("Columbus Blue Jackets", "CBJ", cbj_offense, cbj_defense, cbj_powerplay, cbj_penaltykill, cbj_penalty, goalies["merzlikins"], goalies["tarasov"], goalies["greaves"]),
    "dal": Team("Dallas Stars", "DAL", dal_offense, dal_defense, dal_powerplay, dal_penaltykill, dal_penalty, goalies["oettinger"], goalies["desmith"]),
    "det": Team("Detroit Red Wings", "DET", det_offense, det_defense, det_powerplay, det_penaltykill, det_penalty, goalies["talbot"], goalies["lyon"], goalies["husso"],),
    "edm": Team("Edmonton Oilers", "EDM", edm_offense, edm_defense, edm_powerplay, edm_penaltykill, edm_penalty, goalies["skinner"], goalies["pickard"]),
    "fla": Team("Florida Panthers", "FLA", fla_offense, fla_defense, fla_powerplay, fla_penaltykill, fla_penalty, goalies["bobrovsky"], goalies["knight"]),
    "la": Team("Los Angeles Kings", "LA", la_offense, la_defense, la_powerplay, la_penaltykill, la_penalty, goalies["kuemper"], goalies["rittich"], goalies["copley"]),
    "min": Team("Minnesota Wild", "MIN", min_offense, min_defense, min_powerplay, min_penaltykill, min_penalty, goalies["gustavsson"], goalies["fleury"], goalies["wallstedt"]),
    "mtl": Team("Montreal Canadiens", "MTL", mtl_offense, mtl_defense, mtl_powerplay, mtl_penaltykill, mtl_penalty,goalies["montembeault"], goalies["dobes"], goalies["primeau"]),
    "nsh": Team("Nashville Predators", "NSH", nsh_offense, nsh_defense, nsh_powerplay, nsh_penaltykill, nsh_penalty, goalies["saros"], goalies["wedgewood"], goalies["annunennsh"]),
    "nj": Team("New Jersey Devils", "NJ", nj_offense, nj_defense, nj_powerplay, nj_penaltykill, nj_penalty, goalies["markstrom"], goalies["allen"]),
    "nyi": Team("New York Islanders", "NYI", nyi_offense, nyi_defense, nyi_powerplay, nyi_penaltykill, nyi_penalty, goalies["sorokin"], goalies["varlamov"], goalies["hogberg"]),
    "nyr": Team("New York Rangers", "NYR", nyr_offense, nyr_defense, nyr_powerplay, nyr_penaltykill, nyr_penalty, goalies["shesterkin"], goalies["quick"], goalies["domingue"]),
    "ott": Team("Ottawa Senators", "OTT", ott_offense, ott_defense, ott_powerplay, ott_penaltykill, ott_penalty, goalies["ullmark"], goalies["forsberg"], goalies["merilainen"], goalies["sogaard"]),
    "phi": Team("Philadelphia Flyers", "PHI", phi_offense, phi_defense, phi_powerplay, phi_penaltykill, phi_penalty, goalies["fedotov"], goalies["ersson"], goalies["kolosov"]),
    "pit": Team("Pittsburgh Penguins", "PIT", pit_offense, pit_defense, pit_powerplay, pit_penaltykill, pit_penalty,goalies["jarry"], goalies["ned"], goalies["blomqvist"]),
    "sj": Team("San Jose Sharks", "SJ", sj_offense, sj_defense, sj_powerplay, sj_penaltykill, sj_penalty, goalies["vanacek"], goalies["georgievsj"],goalies["blackwood"],goalies["askarov"]),
    "sea": Team("Seattle Kraken", "SEA", sea_offense, sea_defense, sea_powerplay, sea_penaltykill, sea_penalty,goalies["daccord"], goalies["grubauer"]),
    "stl": Team("St. Louis Blues", "STL", stl_offense, stl_defense, stl_powerplay, stl_penaltykill, stl_penalty, goalies["binner"], goalies["hofer"]),
    "tb": Team("Tampa Bay Lightning", "TB", tb_offense, tb_defense, tb_powerplay, tb_penaltykill, tb_penalty, goalies["vasy"], goalies["johansson"]),
    "tor": Team("Toronto Maple Leafs", "TOR", tor_offense, tor_defense, tor_powerplay, tor_penaltykill, tor_penalty, goalies["stolarz"], goalies["woll"], goalies["murray"], goalies["hildeby"]),
    "ari": Team("Utah Hockey Club", "UT", ut_offense, ut_defense, ut_powerplay, ut_penaltykill, ut_penalty, goalies["ingram"], goalies["vemelka"], goalies["stauber"]),
    "van": Team("Vancouver Canucks", "VAN", van_offense, van_defense, van_powerplay, van_penaltykill, van_penalty, goalies["demko"], goalies["lankinen"], goalies["silvos"]),
    "vgk": Team("Vegas Golden Knights", "VGK", vgk_offense, vgk_defense, vgk_powerplay, vgk_penaltykill, vgk_penalty, goalies["hill"], goalies["samsonov"]),
    "wsh": Team("Washington Capitals", "WSH", wsh_offense, wsh_defense, wsh_powerplay, wsh_penaltykill, wsh_penalty,  goalies["lindgren"], goalies["thompson"]),
    "wpg": Team("Winnipeg Jets", "WPG", wpg_offense, wpg_defense, wpg_powerplay, wpg_penaltykill, wpg_penalty, goalies["hellebuyck"], goalies["comrie"]),
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

def print_team_ratings(teams):
    for team, stats in teams.items():
        output = f"{team.upper()} OFF:{stats.offense:.1f} DEF:{stats.defense:.1f} PP:{stats.powerplay:.1f} PK:{stats.penaltykill:.1f} PEN:{stats.penalty:.1f}"
        print(output)

print_team_ratings(teams)

# Define divisions
metropolitan_division = [teams["car"], teams["cbj"], teams["phi"], teams["pit"], teams["nj"], teams["nyi"], teams["nyr"], teams["wsh"]]
atlantic_division = [teams["bos"], teams["buf"], teams["det"], teams["fla"], teams["mtl"], teams["ott"], teams["tb"], teams["tor"]]
central_division = [teams["ari"], teams["chi"], teams["col"], teams["dal"], teams["min"], teams["nsh"], teams["stl"], teams["wpg"]]
pacific_division = [teams["ana"], teams["cgy"], teams["edm"], teams["la"], teams["sj"], teams["sea"], teams["van"], teams["vgk"]]

eastern_conference = atlantic_division + metropolitan_division
western_conference = central_division + pacific_division

league = eastern_conference + western_conference


def save_team_ratings_to_csv(teams, filename="output/team_ratings.csv"):
    # Define CSV headers
    headers = ["Team","Offense", "Defense", "Powerplay", "Penalty Kill", "Penalty"]

    # Open the CSV file for writing
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write header row

        # Write each team's ratings to the CSV
        for team_code, team in teams.items():
            row = [
                team.name,  # Team name
                team.offense,  # Offense rating
                team.defense,  # Defense rating
                team.powerplay,  # Powerplay rating
                team.penaltykill,  # Penalty kill rating
                team.penalty  # Penalty rating
            ]
            writer.writerow(row)


# Example usage
save_team_ratings_to_csv(teams)