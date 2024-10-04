from goalie import goalies
from skater import forwards
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


def compute_team_ratings(forward_list):
    total_weighted_offense = 0
    total_weighted_defense = 0
    total_offense_weights = 0
    total_defense_weights = 0

    for skater in forward_list:
        role_weight = skater.role_weights.get(skater.role, 1.0)
        total_weighted_offense += (skater.shooting * 0.3 + skater.passing * 0.1 + skater.offense * 0.6) * role_weight
        total_weighted_defense += (skater.defense * 2) * role_weight

        total_offense_weights += (0.15 + 0.05 + 0.32) * role_weight
        total_defense_weights += .97 * role_weight

    weighted_avg_offense = total_weighted_offense / total_offense_weights
    weighted_avg_defense = total_weighted_defense / total_defense_weights

    return weighted_avg_offense, weighted_avg_defense




# Assign forwards to teams
ana_forwards = [forwards["vatrano"], forwards["terry"], forwards["zegras"], forwards["rstrome"], forwards["killorn"], forwards["rjohnston"], forwards["carlsson"], forwards["fabbri"], forwards["cgauthier"], forwards["colangelo"], forwards["mctavish"], forwards["leason"], forwards["lundestrom"], forwards["fowler"], forwards["mintyukov"], forwards["dumoulin"], forwards["zellweger"], forwards["gudas"], forwards["lindstrom"]]
bos_forwards = [forwards["pastrnak"], forwards["marchand"], forwards["coyle"], forwards["zacha"], forwards["frederic"], forwards["mgeekie"], forwards["beecher"], forwards["kastelic"], forwards["pbrown"], forwards["mjones"], forwards["elindholm"], forwards["brazeau"], forwards["mcavoy"], forwards["hlindholm"], forwards["carlo"], forwards["peeke"], forwards["zadorov"], forwards["lohrei"], forwards["wotherspoon"]]
buf_forwards = [forwards["thompson"], forwards["tuch"], forwards["cozens"], forwards["greenway"], forwards["benson"], forwards["quinn"], forwards["mcleod"], forwards["kubel"], forwards["peterka"], forwards["krebs"], forwards["lafferty"], forwards["zucker"], forwards["malenstyn"], forwards["dahlin"], forwards["power"], forwards["byram"], forwards["clifton"], forwards["jokiharju"], forwards["bryson"], forwards["samuelsson"]]
cgy_forwards = [forwards["kadri"], forwards["huby"], forwards["kuzmenko"], forwards["mantha"], forwards["coleman"], forwards["backlund"], forwards["sharangovich"], forwards["rooney"], forwards["pospisil"], forwards["zary"], forwards["lomberg"], forwards["dueher"], forwards["hunt"], forwards["weegar"], forwards["andersson"], forwards["miromanov"], forwards["bahl"], forwards["pachal"], forwards["hanley"]]
car_forwards = [forwards["aho"], forwards["svechnikov"], forwards["kotkaniemi"], forwards["staal"], forwards["martinook"], forwards["fast"], forwards["drury"], forwards["jarvis"], forwards["carrier"], forwards["necas"], forwards["robinson"], forwards["roslovic"],  forwards["orlov"], forwards["slavin"], forwards["burns"], forwards["swalker"], forwards["ghost"], forwards["chatfield"]]
chi_forwards = [forwards["bedard"], forwards["foligno"],  forwards["bertuzzi"], forwards["athanasiou"], forwards["dickinson"], forwards["teravainen"], forwards["kurashev"], forwards["donato"], forwards["reichel"], forwards["crsmith"], forwards["mikheyev"],  forwards["hall"], forwards["joanderson"], forwards["sjones"], forwards["avlassic"], forwards["murphy"], forwards["brodie"], forwards["korchinski"], forwards["martinez"]]
col_forwards = [forwards["mackinnon"], forwards["rantanen"], forwards["mittelstadt"], forwards["lehkonen"], forwards["colton"], forwards["wood"], forwards["kiviranta"], forwards["kovalenko"], forwards["landeskog"], forwards["loconnor"], forwards["wagner"], forwards["makar"], forwards["toews"], forwards["girard"], forwards["dehaan"],  forwards["brannstrom"],  forwards["kylington"], forwards["kmiddleton"], forwards["manson"]]
cbj_forwards = [forwards["jenner"], forwards["marchenko"], forwards["kjohnson"], forwards["kuraly"], forwards["monahan"], forwards["chinakhov"], forwards["olivier"],  forwards["jvr"], forwards["danforth"], forwards["fantilli"], forwards["voronkov"], forwards["sillinger"], forwards["werenski"], forwards["severson"], forwards["provorov"], forwards["jjohnson"], forwards["harris"], forwards["gudbranson"]]
dal_forwards = [forwards["robertson"], forwards["hintz"], forwards["benn"], forwards["seguin"], forwards["marchment"], forwards["duchene"],  forwards["dadonov"], forwards["johnston"], forwards["stankoven"], forwards["bourque"], forwards["steel"], forwards["blackwell"], forwards["heiskanen"], forwards["lindell"], forwards["harley"], forwards["lyubushkin"], forwards["dumba"], forwards["bsmith"], forwards["lundkvist"]]
det_forwards = [forwards["larkin"], forwards["raymond"], forwards["debrincat"], forwards["copp"], forwards["compher"], forwards["tarasenko"], forwards["fischer"], forwards["rasmussen"], forwards["veleno"], forwards["motte"], forwards["pkane"], forwards["berggren"], forwards["watson"], forwards["seider"], forwards["chiarot"], forwards["holl"], forwards["maatta"], forwards["edvinsson"], forwards["gustafsson"], forwards["petry"]]
edm_forwards = [forwards["mcdavid"], forwards["draisaitl"], forwards["hyman"], forwards["ekane"], forwards["arvidsson"], forwards["nuge"],  forwards["podkolzin"], forwards["perry"], forwards["ryan"], forwards["skinner"], forwards["brown"], forwards["nurse"], forwards["ekholm"], forwards["bouchard"], forwards["kulak"], forwards["emberson"], forwards["jbrown"], forwards["stecher"], ]
fla_forwards = [forwards["mtkachuk"], forwards["barkov"], forwards["bennett"], forwards["verhaeghe"], forwards["rodrigues"], forwards["luostarainen"], forwards["reinhart"], forwards["jboqvist"], forwards["gadjovich"], forwards["lundell"], forwards["nosek"], forwards["greer"], forwards["ekblad"], forwards["forsling"], forwards["mikkola"], forwards["kulikov"], forwards["bjornfoot"], forwards["boqvist"], forwards["schmidt"]]
la_forwards = [forwards["kopitar"], forwards["byfield"], forwards["fiala"], forwards["danault"],  forwards["jeannot"], forwards["kempe"], forwards["moore"], forwards["lafferiere"], forwards["kaliyev"], forwards["turcotte"], forwards["lewis"], forwards["foegle"], forwards["gavrikov"], forwards["manderson"], forwards["englund"], forwards["spence"], forwards["edmundson"], forwards["clarke"], forwards["burroughs"]]
min_forwards = [forwards["kaprizov"], forwards["boldy"], forwards["ek"], forwards["zuccarello"], forwards["mfoligno"], forwards["hartman"], forwards["fgaudreau"], forwards["johansson"], forwards["kushnutdinov"], forwards["rossi"],forwards["lauko"], forwards["ohgren"], forwards["trenin"], forwards["brodin"], forwards["middleton"], forwards["bogosian"], forwards["spurgeon"], forwards["merrill"], forwards["faber"]]
mtl_forwards = [forwards["suzuki"], forwards["caufield"],  forwards["laine"], forwards["gallagher"], forwards["anderson"], forwards["dvorak"], forwards["armia"], forwards["newhook"], forwards["evans"], forwards["harvey"], forwards["slafkovsky"], forwards["pezzetta"], forwards["dach"], forwards["jroy"], forwards["matheson"], forwards["savard"], forwards["hutson"], forwards["guhle"], forwards["barron"], forwards["xhekaj"]]
nsh_forwards = [forwards["forsberg"], forwards["oreilly"], forwards["novak"], forwards["stamkos"], forwards["marchessault"], forwards["tomasino"], forwards["nyquist"], forwards["sissons"], forwards["csmith"], forwards["mccarron"], forwards["jankowski"], forwards["parssinen"], forwards["evangelista"], forwards["josi"], forwards["skjei"], forwards["lschenn"], forwards["acarrier"], forwards["fabbro"], forwards["stastney"], forwards["lauzon"]]
nj_forwards = [forwards["jhughes"], forwards["hischier"], forwards["meier"], forwards["bratt"], forwards["palat"], forwards["haula"], forwards["lazar"], forwards["bastian"], forwards["noesen"], forwards["tatar"], forwards["mercer"], forwards["cotter"],  forwards["macdermid"], forwards["hamilton"], forwards["siegenthaler"], forwards["pesce"], forwards["lhughes"], forwards["nemec"], forwards["dillon"], forwards["desimone"]]
nyi_forwards = [forwards["barzal"], forwards["horvat"], forwards["lee"], forwards["nelson"], forwards["pageau"], forwards["palmieri"], forwards["engvall"], forwards["cizikas"], forwards["duclair"], forwards["gauthier"], forwards["fasching"], forwards["maclean"], forwards["holmstrom"], forwards["wahlstrom"], forwards["pulock"], forwards["pelech"], forwards["dobson"], forwards["romanov"], forwards["bolduc"], forwards["mayfield"]]
nyr_forwards = [forwards["panarin"], forwards["kreider"], forwards["zibanejad"], forwards["rsmith"], forwards["trocheck"], forwards["chytil"], forwards["lafreniere"], forwards["kakko"], forwards["edstrom"], forwards["cuylle"], forwards["carrick"], forwards["rempe"], forwards["vesey"], forwards["fox"], forwards["trouba"], forwards["zjones"], forwards["kmiller"], forwards["ruhwedel"], forwards["schneider"], forwards["lindgren"]]
ott_forwards = [forwards["giroux"], forwards["stuetzle"], forwards["btkachuk"], forwards["batherson"], forwards["pinto"], forwards["greig"], forwards["macewen"], forwards["cousins"], forwards["perron"], forwards["norris"], forwards["amadio"], forwards["gregor"], forwards["sanderson"], forwards["chabot"],  forwards["zub"], forwards["hamonic"],  forwards["jensen"], forwards["docker"]]
phi_forwards = [forwards["konecny"], forwards["tippett"], forwards["michkov"], forwards["couturier"], forwards["atkinson"], forwards["farabee"], forwards["laughton"], forwards["cates"], forwards["hathaway"], forwards["frost"], forwards["poehling"], forwards["deslauriers"], forwards["foerster"], forwards["brink"], forwards["sanheim"], forwards["seeler"], forwards["drysdale"], forwards["york"], forwards["ejohnson"], forwards["risto"]]
pit_forwards = [forwards["crosby"], forwards["malkin"], forwards["rust"], forwards["rakell"], forwards["hayes"], forwards["bunting"], forwards["glass"], forwards["eller"], forwards["oconnor"], forwards["beauvilier"], forwards["puljujarvi"], forwards["acciari"], forwards["ekarlsson"], forwards["letang"], forwards["mpettersson"], forwards["saho"], forwards["grzelyck"], forwards["graves"]]
sj_forwards = [forwards["granlund"], forwards["couture"], forwards["goodrow"], forwards["kostin"], forwards["sturm"], forwards["wennberg"], forwards["zetterlund"], forwards["wsmith"], forwards["celebrini"], forwards["eklund"], forwards["toffoli"], forwards["kunin"], forwards["grundstrom"], forwards["dellandrea"], forwards["bordeleau"], forwards["vlassic"], forwards["ferraro"], forwards["benning"],  forwards["ceci"], forwards["rutta"], forwards["walman"]]
sea_forwards = [forwards["mccann"], forwards["tolvanen"], forwards["burakovsky"], forwards["bjorkstrand"], forwards["schwartz"], forwards["gourde"], forwards["eberle"], forwards["btanev"], forwards["beniers"], forwards["wright"], forwards["kartye"], forwards["stephenson"], forwards["dunn"], forwards["oleksiak"], forwards["larsson"], forwards["borgen"], forwards["revans"], forwards["mahura"], forwards["montour"]]
stl_forwards = [forwards["thomas"], forwards["kyrou"], forwards["bschenn"],  forwards["holloway"], forwards["buchnevich"], forwards["joseph"], forwards["saad"], forwards["kapanen"], forwards["faksa"], forwards["sundqvist"], forwards["toropchenko"], forwards["texier"], forwards["neighbours"], forwards["faulk"], forwards["krug"], forwards["rsuter"], forwards["parayko"], forwards["leddy"], forwards["perunovich"], forwards["broberg"]]
tb_forwards = [forwards["kucherov"], forwards["point"],  forwards["guentzel"], forwards["hagel"], forwards["cirelli"], forwards["paul"], forwards["sheary"], forwards["eyssimont"], forwards["atkinson"], forwards["chaffee"], forwards["glendening"], forwards["girgensons"], forwards["hedman"], forwards["mcdonagh"], forwards["cernak"], forwards["moser"], forwards["raddysh"], forwards["perbix"]]
tor_forwards = [forwards["matthews"], forwards["nylander"], forwards["marner"], forwards["tavares"], forwards["kampf"], forwards["reaves"], forwards["jarnkrok"], forwards["knies"], forwards["mcmann"], forwards["domi"], forwards["nrobertson"], forwards["holmberg"], forwards["dewar"],forwards["rielly"], forwards["mccabe"], forwards["benoit"], forwards["timmins"], forwards["liljgren"], forwards["ctanev"], forwards["oel"]]
ut_forwards = [forwards["keller"], forwards["maccelli"], forwards["guenther"], forwards["schmaltz"], forwards["crouse"], forwards["kerfoot"], forwards["bjugstad"], forwards["mcbain"], forwards["cooley"], forwards["hayton"], forwards["stenlund"], forwards["doan"], forwards["carcone"], forwards["durzi"],  forwards["sergachev"], forwards["valimaki"], forwards["marino"], forwards["kesselring"], forwards["cole"]]
van_forwards = [forwards["pettersson"], forwards["miller"], forwards["boeser"], forwards["garland"], forwards["mikheyev"], forwards["psuter"], forwards["hoglander"], forwards["debrusk"], forwards["heinen"], forwards["sherwood"], forwards["sprong"], forwards["aman"], forwards["sprong"], forwards["phidi"], forwards["qhughes"], forwards["hronek"], forwards["soucy"], forwards["forbort"], forwards["myers"], forwards["desharnais"], forwards["friedman"]]
vgk_forwards = [forwards["eichel"], forwards["stone"], forwards["wkarlsson"], forwards["hertl"], forwards["barbashev"], forwards["nroy"], forwards["howden"], forwards["holtz"], forwards["dorofeyev"],  forwards["olofsson"], forwards["rondbjerg"], forwards["kolesar"], forwards["pietrangelo"], forwards["hanafin"], forwards["whitecloud"], forwards["theodore"], forwards["hague"], forwards["mcnabb"]]
wsh_forwards = [forwards["ovi"], forwards["dubois"], forwards["dstrome"], forwards["mcmichael"], forwards["oshie"], forwards["protas"], forwards["wilson"], forwards["mangiapane"], forwards["dowd"], forwards["milano"],  forwards["traddysh"], forwards["duhaime"], forwards["jcarlson"], forwards["sandin"], forwards["tvr"], forwards["fehervary"], forwards["mroy"], forwards["chychrun"]]
wpg_forwards = [forwards["scheifele"], forwards["connor"], forwards["niederreiter"], forwards["lowry"], forwards["perfetti"], forwards["vilardi"], forwards["iafallo"], forwards["namestnikov"], forwards["niederreiter"], forwards["appleton"], forwards["kupari"], forwards["barron"], forwards["morrissey"], forwards["samberg"], forwards["demelo"], forwards["cmiller"], forwards["stanley"], forwards["pionk"]]

# Compute team ratings
ana_offense, ana_defense = compute_team_ratings(ana_forwards)
bos_offense, bos_defense = compute_team_ratings(bos_forwards)
buf_offense, buf_defense = compute_team_ratings(buf_forwards)
cgy_offense, cgy_defense = compute_team_ratings(cgy_forwards)
car_offense, car_defense = compute_team_ratings(car_forwards)
chi_offense, chi_defense = compute_team_ratings(chi_forwards)
col_offense, col_defense = compute_team_ratings(col_forwards)
cbj_offense, cbj_defense = compute_team_ratings(cbj_forwards)
dal_offense, dal_defense = compute_team_ratings(dal_forwards)
det_offense, det_defense = compute_team_ratings(det_forwards)
edm_offense, edm_defense = compute_team_ratings(edm_forwards)
fla_offense, fla_defense = compute_team_ratings(fla_forwards)
la_offense, la_defense = compute_team_ratings(la_forwards)
min_offense, min_defense = compute_team_ratings(min_forwards)
mtl_offense, mtl_defense = compute_team_ratings(mtl_forwards)
nsh_offense, nsh_defense = compute_team_ratings(nsh_forwards)
nj_offense, nj_defense = compute_team_ratings(nj_forwards)
nyi_offense, nyi_defense = compute_team_ratings(nyi_forwards)
nyr_offense, nyr_defense = compute_team_ratings(nyr_forwards)
ott_offense, ott_defense = compute_team_ratings(ott_forwards)
phi_offense, phi_defense = compute_team_ratings(phi_forwards)
pit_offense, pit_defense = compute_team_ratings(pit_forwards)
sj_offense, sj_defense = compute_team_ratings(sj_forwards)
sea_offense, sea_defense = compute_team_ratings(sea_forwards)
stl_offense, stl_defense = compute_team_ratings(stl_forwards)
tb_offense, tb_defense = compute_team_ratings(tb_forwards)
tor_offense, tor_defense = compute_team_ratings(tor_forwards)
ut_offense, ut_defense = compute_team_ratings(ut_forwards)
van_offense, van_defense = compute_team_ratings(van_forwards)
vgk_offense, vgk_defense = compute_team_ratings(vgk_forwards)
wsh_offense, wsh_defense = compute_team_ratings(wsh_forwards)
wpg_offense, wpg_defense = compute_team_ratings(wpg_forwards)

# Create team objects
teams = {
    "ana": Team("Anaheim Ducks", "ANA", ana_offense, ana_defense, goalies["gibson"], goalies["dostal"]),
    "bos": Team("Boston Bruins", "BOS", bos_offense, bos_defense, goalies["bussi"], goalies["korp"]),
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