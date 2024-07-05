from goalie import goalies
from skater import forwards
import random
class Team:
    def __init__(self, name, abrv, offense, defense, starting_goalie, backup_goalie,
                 wins=0, losses=0, otl=0, points=0, playoffs=0,
                 second_round=0, conf_final=0, cup_final=0,
                 cup_win=0):
        self.name = name
        self.abrv = abrv
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
        total_rating = self.starting_goalie.rating + self.backup_goalie.rating

        # Calculate the probability for each goalie based on their ratings
        starting_goalie_probability = self.starting_goalie.rating / total_rating
        backup_goalie_probability = self.backup_goalie.rating / total_rating

        # Adjust probabilities to reflect a larger difference if there's a big gap in ratings
        rating_difference = abs(self.starting_goalie.rating - self.backup_goalie.rating)
        if rating_difference > 10:
            adjustment_factor = rating_difference / 100
            starting_goalie_probability += adjustment_factor * starting_goalie_probability
            backup_goalie_probability -= adjustment_factor * backup_goalie_probability

        # Ensure the probabilities still sum to 1
        total_probability = starting_goalie_probability + backup_goalie_probability
        starting_goalie_probability /= total_probability
        backup_goalie_probability /= total_probability

        probabilities = [starting_goalie_probability, backup_goalie_probability]
        selected_goalie = random.choices([self.starting_goalie, self.backup_goalie], weights=probabilities)[0]
        return selected_goalie


def compute_team_ratings(forward_list):
    total_weighted_offense = 0
    total_weighted_defense = 0
    total_offense_weights = 0
    total_defense_weights = 0

    for skater in forward_list:
        total_weighted_offense += skater.shooting * 0.3 + skater.passing * 0.1 + skater.offense * 0.6
        total_weighted_defense += skater.defense * 2

        total_offense_weights += 0.15 + 0.05 + 0.30
        total_defense_weights += 1

    weighted_avg_offense = total_weighted_offense / total_offense_weights
    weighted_avg_defense = total_weighted_defense / total_defense_weights

    return weighted_avg_offense, weighted_avg_defense


# Assign forwards to teams
ana_forwards = [forwards["vatrano"], forwards["terry"], forwards["zegras"], forwards["rstrome"], forwards["killorn"], forwards["rjohnston"], forwards["carlsson"], forwards["fabbri"], forwards["cgauthier"], forwards["colangelo"], forwards["mctavish"], forwards["mcginn"], forwards["lundestrom"], forwards["fowler"], forwards["mintyukov"], forwards["dumoulin"], forwards["zellweger"], forwards["lindstrom"]]
bos_forwards = [forwards["pastrnak"], forwards["marchand"], forwards["coyle"], forwards["zacha"], forwards["frederic"], forwards["mgeekie"], forwards["beecher"], forwards["kastelic"], forwards["pbrown"], forwards["mjones"], forwards["elindholm"], forwards["brazeau"], forwards["mcavoy"], forwards["hlindholm"], forwards["carlo"], forwards["peeke"], forwards["zadorov"], forwards["lohrei"], forwards["wotherspoon"]]
buf_forwards = [forwards["thompson"], forwards["tuch"], forwards["skinner"], forwards["cozens"], forwards["greenway"], forwards["benson"], forwards["quinn"], forwards["kubel"], forwards["peterka"], forwards["krebs"], forwards["lafferty"], forwards["zucker"], forwards["dahlin"], forwards["power"], forwards["byram"], forwards["clifton"], forwards["bryson"], forwards["samuelsson"]]
cgy_forwards = [forwards["kadri"], forwards["huby"], forwards["kuzmenko"], forwards["mantha"], forwards["coleman"], forwards["backlund"], forwards["sharangovich"], forwards["rooney"], forwards["pospisil"], forwards["zary"], forwards["lomberg"], forwards["dueher"], forwards["hunt"], forwards["weegar"], forwards["andersson"], forwards["miromanov"], forwards["bahl"], forwards["hanley"]]
car_forwards = [forwards["aho"], forwards["svechnikov"], forwards["kotkaniemi"], forwards["kuznetsov"], forwards["staal"], forwards["martinook"], forwards["fast"], forwards["drury"], forwards["jarvis"], forwards["carrier"], forwards["necas"], forwards["robinson"], forwards["roslovic"],  forwards["orlov"], forwards["slavin"], forwards["burns"], forwards["swalker"], forwards["ghost"], forwards["chatfield"]]
chi_forwards = [forwards["bedard"], forwards["foligno"],  forwards["bertuzzi"], forwards["athanasiou"], forwards["dickinson"], forwards["teravainen"], forwards["kurashev"], forwards["donato"], forwards["reichel"], forwards["crsmith"], forwards["mikheyev"],  forwards["hall"], forwards["joanderson"], forwards["sjones"], forwards["avlassic"], forwards["murphy"], forwards["korchinski"], forwards["martinez"]]
col_forwards = [forwards["mackinnon"], forwards["rantanen"], forwards["mittelstadt"], forwards["lehkonen"], forwards["colton"], forwards["wood"], forwards["kiviranta"], forwards["kovalenko"], forwards["landeskog"], forwards["loconnor"], forwards["wagner"], forwards["makar"], forwards["toews"], forwards["girard"], forwards["dehaan"],  forwards["brannstrom"], forwards["kmiddleton"], forwards["manson"]]
cbj_forwards = [forwards["jenner"], forwards["marchenko"], forwards["gaudreau"], forwards["kjohnson"], forwards["kuraly"], forwards["monahan"], forwards["chinakhov"], forwards["olivier"], forwards["danforth"], forwards["laine"], forwards["fantilli"], forwards["voronkov"], forwards["sillinger"], forwards["werenski"], forwards["severson"], forwards["provorov"], forwards["gudbranson"]]
dal_forwards = [forwards["robertson"], forwards["hintz"], forwards["benn"], forwards["seguin"], forwards["marchment"], forwards["duchene"],  forwards["dadonov"], forwards["johnston"], forwards["stankoven"], forwards["bourque"], forwards["steel"], forwards["heiskanen"], forwards["lindell"], forwards["harley"], forwards["lyubushkin"], forwards["dumba"], forwards["bsmith"], forwards["lundkvist"]]
det_forwards = [forwards["larkin"], forwards["raymond"], forwards["debrincat"], forwards["copp"], forwards["compher"], forwards["tarasenko"], forwards["fischer"], forwards["rasmussen"], forwards["veleno"], forwards["motte"], forwards["pkane"], forwards["seider"], forwards["chiarot"], forwards["holl"], forwards["maatta"], forwards["gustafsson"], forwards["petry"]]
edm_forwards = [forwards["mcdavid"], forwards["draisaitl"], forwards["hyman"], forwards["ekane"], forwards["arvidsson"], forwards["nuge"], forwards["perry"], forwards["mcleod"], forwards["ryan"], forwards["holloway"], forwards["brown"], forwards["nurse"], forwards["ekholm"], forwards["bouchard"], forwards["ceci"], forwards["kulak"], forwards["broberg"]]
fla_forwards = [forwards["mtkachuk"], forwards["barkov"], forwards["bennett"], forwards["verhaeghe"], forwards["rodrigues"], forwards["luostarainen"], forwards["reinhart"], forwards["jboqvist"], forwards["gadjovich"], forwards["lundell"], forwards["nosek"], forwards["greer"], forwards["ekblad"], forwards["forsling"], forwards["mikkola"], forwards["kulikov"], forwards["schmidt"]]
la_forwards = [forwards["kopitar"], forwards["byfield"], forwards["fiala"], forwards["danault"],  forwards["jeannot"], forwards["kempe"], forwards["moore"], forwards["lafferiere"], forwards["kaliyev"], forwards["foegle"], forwards["doughty"], forwards["gavrikov"], forwards["manderson"], forwards["englund"], forwards["spence"], forwards["edmundson"], forwards["burroughs"]]
min_forwards = [forwards["kaprizov"], forwards["boldy"], forwards["ek"], forwards["zuccarello"], forwards["mfoligno"], forwards["hartman"], forwards["fgaudreau"], forwards["johansson"], forwards["kushnutdinov"], forwards["rossi"],forwards["lauko"], forwards["ohgren"], forwards["trenin"], forwards["brodin"], forwards["middleton"], forwards["bogosian"], forwards["spurgeon"], forwards["merrill"], forwards["faber"]]
mtl_forwards = [forwards["suzuki"], forwards["caufield"], forwards["gallagher"], forwards["anderson"], forwards["dvorak"], forwards["armia"], forwards["newhook"], forwards["evans"], forwards["harvey"], forwards["slafkovsky"], forwards["pezzetta"], forwards["dach"], forwards["matheson"], forwards["savard"], forwards["harris"], forwards["hutson"], forwards["guhle"], forwards["xhekaj"]]
nsh_forwards = [forwards["forsberg"], forwards["oreilly"], forwards["novak"], forwards["stamkos"], forwards["marchessault"],forwards["nyquist"], forwards["sissons"], forwards["glass"], forwards["csmith"], forwards["mccarron"], forwards["jankowski"], forwards["evangelista"], forwards["josi"], forwards["skjei"], forwards["lschenn"], forwards["acarrier"], forwards["fabbro"], forwards["lauzon"]]
nj_forwards = [forwards["jhughes"], forwards["hischier"], forwards["meier"], forwards["bratt"], forwards["palat"], forwards["haula"], forwards["lazar"], forwards["nfoote"], forwards["noesen"], forwards["tatar"], forwards["mercer"], forwards["hamilton"], forwards["siegenthaler"], forwards["pesce"], forwards["lhughes"], forwards["macdermid"], forwards["nemec"], forwards["dillon"], forwards["desimone"]]
nyi_forwards = [forwards["barzal"], forwards["horvat"], forwards["lee"], forwards["nelson"], forwards["pageau"], forwards["palmieri"], forwards["engvall"], forwards["cizikas"], forwards["duclair"], forwards["gauthier"], forwards["fasching"], forwards["maclean"], forwards["holmstrom"], forwards["wahlstrom"], forwards["pulock"], forwards["pelech"], forwards["dobson"], forwards["romanov"], forwards["bolduc"], forwards["mayfield"]]
nyr_forwards = [forwards["panarin"], forwards["kreider"], forwards["zibanejad"], forwards["rsmith"], forwards["trocheck"], forwards["chytil"], forwards["lafreniere"], forwards["kakko"], forwards["edstrom"], forwards["cuylle"], forwards["carrick"], forwards["rempe"], forwards["vesey"], forwards["fox"], forwards["trouba"], forwards["zjones"], forwards["kmiller"], forwards["lindgren"]]
ott_forwards = [forwards["giroux"], forwards["stuetzle"], forwards["btkachuk"], forwards["batherson"], forwards["pinto"], forwards["greig"], forwards["macewen"], forwards["perron"], forwards["norris"], forwards["amadio"], forwards["gregor"], forwards["sanderson"], forwards["chabot"],  forwards["zub"], forwards["hamonic"],  forwards["jensen"], forwards["docker"]]
phi_forwards = [forwards["konecny"], forwards["tippett"], forwards["michkov"], forwards["couturier"], forwards["atkinson"], forwards["farabee"], forwards["laughton"], forwards["cates"], forwards["hathaway"], forwards["frost"], forwards["poehling"], forwards["deslauriers"], forwards["foerster"], forwards["brink"], forwards["sanheim"], forwards["seeler"], forwards["drysdale"], forwards["york"], forwards["ejohnson"], forwards["risto"]]
pit_forwards = [forwards["crosby"], forwards["malkin"], forwards["rust"], forwards["rakell"], forwards["hayes"], forwards["bunting"], forwards["eller"], forwards["oconnor"], forwards["beauvilier"], forwards["puljujarvi"], forwards["acciari"], forwards["ekarlsson"], forwards["letang"], forwards["mpettersson"], forwards["saho"], forwards["grzelyck"], forwards["graves"]]
sj_forwards = [forwards["granlund"], forwards["couture"], forwards["goodrow"], forwards["kostin"], forwards["sturm"], forwards["wennberg"], forwards["zetterlund"], forwards["wsmith"], forwards["celebrini"], forwards["eklund"], forwards["toffoli"], forwards["kunin"], forwards["grundstrom"], forwards["afanaseyev"], forwards["dellandrea"], forwards["bordeleau"], forwards["vlassic"], forwards["ferraro"], forwards["rutta"], forwards["walman"]]
sea_forwards = [forwards["mccann"], forwards["tolvanen"], forwards["burakovsky"], forwards["schwartz"], forwards["gourde"], forwards["eberle"], forwards["btanev"], forwards["beniers"], forwards["wright"], forwards["stephenson"], forwards["dunn"], forwards["oleksiak"], forwards["larsson"], forwards["borgen"], forwards["montour"]]
stl_forwards = [forwards["thomas"], forwards["kyrou"], forwards["bschenn"], forwards["buchnevich"], forwards["kapanen"],  forwards["joseph"], forwards["saad"], forwards["kapanen"], forwards["faksa"], forwards["sundqvist"], forwards["toropchenko"], forwards["texier"], forwards["neighbours"], forwards["faulk"], forwards["krug"], forwards["parayko"], forwards["leddy"], forwards["perunovich"], forwards["tucker"]]
tb_forwards = [forwards["kucherov"], forwards["point"],  forwards["guentzel"], forwards["hagel"], forwards["cirelli"], forwards["paul"], forwards["sheary"], forwards["eyssimont"], forwards["atkinson"], forwards["chaffee"], forwards["glendening"], forwards["girgensons"], forwards["hedman"], forwards["mcdonagh"], forwards["cernak"], forwards["moser"],forwards["perbix"]]
tor_forwards = [forwards["matthews"], forwards["nylander"], forwards["marner"], forwards["tavares"], forwards["kampf"], forwards["reaves"], forwards["jarnkrok"], forwards["knies"], forwards["mcmann"], forwards["domi"], forwards["nrobertson"], forwards["holmberg"], forwards["dewar"],forwards["rielly"], forwards["mccabe"], forwards["benoit"], forwards["timmins"], forwards["liljgren"], forwards["ctanev"], forwards["oel"]]
ut_forwards = [forwards["keller"], forwards["maccelli"], forwards["schmaltz"], forwards["crouse"], forwards["kerfoot"], forwards["bjugstad"], forwards["mcbain"], forwards["cooley"], forwards["hayton"], forwards["stenlund"], forwards["carcone"], forwards["durzi"],  forwards["sergachev"], forwards["valimaki"], forwards["marino"], forwards["kesselring"], forwards["cole"]]
van_forwards = [forwards["pettersson"], forwards["miller"], forwards["boeser"], forwards["garland"], forwards["mikheyev"], forwards["psuter"], forwards["hoglander"], forwards["podkolzin"], forwards["debrusk"], forwards["heinen"], forwards["sherwood"], forwards["aman"], forwards["phidi"], forwards["qhughes"], forwards["hronek"], forwards["soucy"], forwards["forbort"], forwards["myers"], forwards["desharnais"], forwards["friedman"]]
vgk_forwards = [forwards["eichel"], forwards["stone"], forwards["wkarlsson"], forwards["hertl"], forwards["barbashev"], forwards["nroy"], forwards["howden"], forwards["holtz"], forwards["dorofeyev"],  forwards["olofsson"], forwards["rondbjerg"], forwards["kolesar"], forwards["pietrangelo"], forwards["hanafin"], forwards["whitecloud"], forwards["theodore"], forwards["hague"], forwards["mcnabb"], forwards["okhotiuk"]]
wsh_forwards = [forwards["ovi"], forwards["dubois"], forwards["dstrome"], forwards["mcmichael"], forwards["oshie"], forwards["protas"], forwards["wilson"], forwards["mangiapane"], forwards["dowd"], forwards["milano"], forwards["duhaime"], forwards["jcarlson"], forwards["sandin"], forwards["tvr"], forwards["fehervary"], forwards["mroy"], forwards["chychrun"]]
wpg_forwards = [forwards["scheifele"], forwards["connor"], forwards["niederreiter"], forwards["lowry"], forwards["perfetti"], forwards["vilardi"], forwards["iafallo"], forwards["namestnikov"], forwards["niederreiter"], forwards["appleton"], forwards["kupari"], forwards["barron"], forwards["morrissey"], forwards["schmidt"], forwards["samberg"], forwards["pionk"]]

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
    "nsh": Team("Nashville Predators", "NSH", nsh_offense, nsh_defense, goalies["saros"], goalies["askarov"]),
    "nj": Team("New Jersey Devils", "NJ", nj_offense, nj_defense, goalies["markstrom"], goalies["allen"]),
    "nyi": Team("New York Islanders", "NYI", nyi_offense, nyi_defense, goalies["sorokin"], goalies["varlamov"]),
    "nyr": Team("New York Rangers", "NYR", nyr_offense, nyr_defense, goalies["shesterkin"], goalies["quick"]),
    "ott": Team("Ottawa Senators", "OTT", ott_offense, ott_defense, goalies["ullmark"], goalies["forsberg"]),
    "phi": Team("Philadelphia Flyers", "PHI", phi_offense, phi_defense, goalies["fedotov"], goalies["ersson"]),
    "pit": Team("Pittsburgh Penguins", "PIT", pit_offense, pit_defense, goalies["jarry"], goalies["ned"]),
    "sj": Team("San Jose Sharks", "SJ", sj_offense, sj_defense, goalies["blackwood"], goalies["cooley"]),
    "sea": Team("Seattle Kraken", "SEA", sea_offense, sea_defense, goalies["daccord"], goalies["grubauer"]),
    "stl": Team("St. Louis Blues", "STL", stl_offense, stl_defense, goalies["binner"], goalies["hofer"]),
    "tb": Team("Tampa Bay Lightning", "TB", tb_offense, tb_defense, goalies["vasy"], goalies["johansson"]),
    "tor": Team("Toronto Maple Leafs", "TOR", tor_offense, tor_defense, goalies["woll"], goalies["stolarz"]),
    "ari": Team("Utah Hockey Club", "UT", ut_offense, ut_defense, goalies["vemelka"], goalies["ingram"]),
    "van": Team("Vancouver Canucks", "VAN", van_offense, van_defense, goalies["demko"], goalies["silvos"]),
    "vgk": Team("Vegas Golden Knights", "VGK", vgk_offense, vgk_defense, goalies["hill"], goalies["samsonov"]),
    "wsh": Team("Washington Capitals", "WSH", wsh_offense, wsh_defense, goalies["lindgren"], goalies["thompson"]),
    "wpg": Team("Winnipeg Jets", "WPG", wpg_offense, wpg_defense, goalies["hellebuyck"], goalies["comrie"]),
}

print("ANA", ana_offense, ana_defense)
print("BOS", bos_offense, bos_defense)
print("BUF", buf_offense, buf_defense)
print("CGY", cgy_offense, cgy_defense)
print("CAR", car_offense, car_defense)
print("CHI", chi_offense, chi_defense)
print("COL", col_offense, col_defense)
print("CBJ", cbj_offense, cbj_defense)
print("DAL", dal_offense, dal_defense)
print("DET", det_offense, det_defense)
print("EDM", edm_offense, edm_defense)
print("FLA", fla_offense, fla_defense)
print("LA", la_offense, la_defense)
print("MIN", min_offense, min_defense)
print("MTL", mtl_offense, mtl_defense)
print("NSH", nsh_offense, nsh_defense)
print("NJ", nj_offense, nj_defense)
print("NYI", nyi_offense, nyi_defense)
print("NYR", nyr_offense, nyr_defense)
print("OTT", ott_offense, ott_defense)
print("PHI", phi_offense, phi_defense)
print("PIT", pit_offense, pit_defense)
print("SJ", sj_offense, sj_defense)
print("SEA", sea_offense, sea_defense)
print("STL", stl_offense, stl_defense)
print("TB", tb_offense, tb_defense)
print("TOR", tor_offense, tor_defense)
print("UT", ut_offense, ut_defense)
print("VAN", van_offense, van_defense)
print("VGK", vgk_offense, vgk_defense)
print("WSH", wsh_offense, wsh_defense)
print("WPG", wpg_offense, wpg_defense)
# Define divisions
metropolitan_division = [teams["car"], teams["cbj"], teams["phi"], teams["pit"], teams["nj"], teams["nyi"], teams["nyr"], teams["wsh"]]
atlantic_division = [teams["bos"], teams["buf"], teams["det"], teams["fla"], teams["mtl"], teams["ott"], teams["tb"], teams["tor"]]
central_division = [teams["ari"], teams["chi"], teams["col"], teams["dal"], teams["min"], teams["nsh"], teams["stl"], teams["wpg"]]
pacific_division = [teams["ana"], teams["cgy"], teams["edm"], teams["la"], teams["sj"], teams["sea"], teams["van"], teams["vgk"]]

eastern_conference = atlantic_division + metropolitan_division
western_conference = central_division + pacific_division

league = eastern_conference + western_conference