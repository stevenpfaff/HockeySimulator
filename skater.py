class Skater:
    def __init__(self, name, shooting=None, passing=None, offense=None, defense=None, goals=0, assists=0, points=0):
        self.name = name
        self.shooting = shooting or 50
        self.passing = passing or 50
        self.offense = offense or 50
        self.defense = defense or 50
        self.goals = goals
        self.assists = assists
        self.points = points

    def overall(self):
        weights = {'shooting': 0.2, 'passing': 0.1, 'offense': 0.35, 'defense': 0.35}
        return (self.shooting * weights['shooting'] +
                self.passing * weights['passing'] +
                self.offense * weights['offense'] +
                self.defense * weights['defense'])


forwards = {
    # Ducks
    "vatrano": Skater("Frank Vatrano", 70, 40, 30, 20),
    "terry": Skater("Troy Terry", 60, 60, 55, 50),
    "zegras": Skater("Trevor Zegras", 55, 60, 60, 30),
    "rstrome": Skater("Ryan Strome", 45, 50, 50, 20),
    "killorn": Skater("Alex Killorn", 60, 55, 50, 45),
    "rjohnston": Skater("Ross Johnston", 20, 20, 20, 40),
    "carlsson": Skater("Leo Carlsson", 50, 30, 60, 60),
    "cgauthier": Skater("Cutter Gauthier", 55, 50, 55, 50),
    "colangelo": Skater("Sam Colangelo", 50, 40, 50, 50),
    "mctavish": Skater("Mason McTavish", 55, 60, 60, 30),
    "mcginn": Skater("Brock McGinn", 30, 20, 30, 50),
    "leason": Skater("Brett Leason", 50, 30, 20, 30),
    "fabbri": Skater("Robby Fabbri", 60, 20, 40, 30),
    "lundestrom": Skater("Isac Lundestrom", 30, 30, 20, 60),
    "fowler": Skater("Cam Fowler", 55, 50, 50, 50),
    "gudas": Skater("Radko Gudas", 50, 50, 55, 70),
    "mintyukov": Skater("Pavel Mintyukov", 50, 40, 65, 30),
    "zellweger": Skater("Olen Zellweger", 50, 50, 50, 30),
    "lindstrom": Skater("Gustav Lindstrom", 30, 60, 30, 45),
    "dumoulin": Skater("Brian Dumoulin", 50, 55, 40, 60),
     # Bruins
    "marchand": Skater("Brad Marchand", 60, 65, 65, 50),
    "pastrnak": Skater("David Pastrnak", 90, 80, 85, 50),
    "coyle": Skater("Charlie Coyle", 65, 55, 45, 40),
    "zacha": Skater("Pavel Zacha", 60, 60, 45, 40),
    "frederic": Skater("Trent Frederic", 60, 55, 60, 55),
    "mgeekie": Skater("Morgan Geekie", 55, 60, 50, 30),
    "beecher": Skater("John Beecher", 60, 30, 20, 40),
    "kastelic": Skater("Mark Kastelic", 40, 20, 40, 60),
    "pbrown": Skater("Patrick Brown", 30, 30, 30, 50),
    "elindholm": Skater("Elias Lindholm", 55, 60, 35, 45),
    "brazeau": Skater("Justin Brazeau", 55, 30, 50, 60),
    "mjones": Skater("Max Jones", 20, 50, 50, 45),
    "mcavoy": Skater("Charlie McAvoy", 60, 65, 80, 60),
    "hlindholm": Skater("Hampus Lindholm", 35, 60, 65, 70),
    "carlo": Skater("Brandon Carlo", 50, 55, 30, 65),
    "peeke": Skater("Andrew Peeke", 40, 50, 20, 60),
    "lohrei": Skater("Mason Lohrei", 60, 30, 20, 20),
    "zadorov": Skater("Nikita Zadorov", 60, 55, 40, 60),
    "wotherspoon": Skater("Parker Wotherspoon", 20, 20, 60, 60),
    # Sabres
    "thompson": Skater("Tage Thompson", 80, 65, 65, 30),
    "tuch": Skater("Alex Tuch", 55, 80, 70, 45),
    "cozens": Skater("Dylan Cozens", 50, 60, 60, 30),
    "greenway": Skater("Jordan Greenway", 30, 30, 30, 65),
    "benson": Skater("Zach Benson", 40, 60, 60, 60),
    "quinn": Skater("Jack Quinn", 60, 60, 60, 50),
    "peterka": Skater("JJ Peterka", 60, 55, 60, 30),
    "krebs": Skater("Peyton Krebs", 30, 30, 20, 55),
    "lafferty": Skater("Sam Lafferty", 55, 35, 20, 50),
    "kubel": Skater("Nicolas Aube-Kubel", 35, 45, 30, 70),
    "zucker": Skater("Jason Zucker", 55, 50, 70, 30),
    "dahlin": Skater("Rasmus Dahlin", 70, 70, 80, 65),
    "power": Skater("Owen Power", 30, 50, 60, 40),
    "byram": Skater("Bowen Byram", 80, 60, 30, 20),
    "clifton": Skater("Connor Clifton", 30, 60, 50, 35),
    "bryson": Skater("Jacob Bryson", 35, 55, 30, 60),
    "samuelsson": Skater("Mattias Samuelsson", 20, 30, 40, 50),
    # Flames
    "kadri": Skater("Nazem Kadri", 55, 80, 60, 50),
    "huby": Skater("Jonathan Huberdeau", 40, 70, 60, 35),
    "kuzmenko": Skater("Andrei Kuzmenko", 80, 60, 55,50),
    "coleman": Skater("Blake Coleman", 55, 50, 60,65),
    "backlund": Skater("Mikael Backlund", 30, 60, 60, 65),
    "sharangovich": Skater("Yegor Sharangovich", 65, 40, 45, 30),
    "rooney": Skater("Kevin Rooney", 30, 20, 30, 55),
    "pospisil": Skater("Martin Pospisil", 30, 50, 60, 45),
    "mantha": Skater("Anthony Mantha", 65, 60, 60,  70),
    "lomberg": Skater("Ryan Lomberg", 40, 30, 50, 45),
    "zary": Skater("Connor Zary", 65, 60, 30, 65),
    "dueher": Skater("Walker Dueher", 50, 65, 50, 30),
    "hunt": Skater("Dryden Hunt", 30, 30, 20, 60),
    "weegar": Skater("MacKenzie Weegar", 65, 55, 60, 70),
    "andersson": Skater("Rasmus Andersson", 50, 65, 65, 30),
    "bahl": Skater("Kevin Bahl", 40, 35, 30, 60),
    "hanley": Skater("Joel Hanley", 35, 30, 30, 60),
    "bean": Skater("Jake Bean", 60, 50, 35, 30),
    "miromanov": Skater("Danill Miromanov", 65, 60, 50, 50),
    "okhotiuk": Skater("Nikita Okhotiuk", 30, 50, 50, 20),
    # Hurricanes
    "aho": Skater("Sebastian Aho", 70, 70, 70, 60),
    "svechnikov": Skater("Andrei Svechnikov", 50, 65, 80, 40),
    "kotkaniemi": Skater("Jesperi Kotkaniemi", 50, 40, 50, 50),
    "kuznetsov": Skater("Evgeni Kuznetsov", 30, 60, 20, 30),
    "staal": Skater("Jordan Staal", 30, 30, 50, 80),
    "fast": Skater("Jesper Fast", 30, 40, 60, 70),
    "drury": Skater("Jack Drury", 20, 50, 35, 70),
    "jarvis": Skater("Seth Jarvis", 60, 50, 60, 80),
    "lemieux": Skater("Brendan Lemieux", 40, 50, 35, 30),
    "martinook": Skater("Jordan Martinook", 30, 60, 55, 60),
    "carrier": Skater("William Carrier", 30, 35, 60, 60),
    "robinson": Skater("Eric Robinson", 20, 45, 50, 20),
    "jost": Skater("Tyson Jost", 30, 40, 30, 40),
    "roslovic": Skater("Jack Roslovic", 40, 65, 50, 30),
    "rsuzuki": Skater("Ryan Suzuki", 30, 40, 35, 35),
    "necas": Skater("Martin Necas", 60, 60, 60, 20),
    "orlov": Skater("Dimitry Orlov", 60, 40, 60, 60),
    "slavin": Skater("Jaccob Slavin", 30, 60, 70, 80),
    "burns": Skater("Brent Burns", 70, 60, 70, 55),
    "swalker": Skater("Sean Walker", 60, 55, 65, 50),
    "ghost": Skater("Shayne Gostisbehere", 80, 60, 55, 30),
    "chatfield": Skater("Jalen Chatfield", 60, 35, 60, 60),
    # Blackhawks
    "bedard": Skater("Connor Bedard", 60, 60, 55, 20),
    "foligno": Skater("Nick Foligno", 35, 55, 40, 60),
    "bertuzzi": Skater("Tyler Bertuzzi", 50, 60, 80, 30),
    "athanasiou": Skater("Andreas Athanasiou", 45, 45, 40, 20),
    "dickinson": Skater("Jason Dickinson", 60, 30, 30,70),
    "kurashev": Skater("Philip Kurashev", 50, 30, 30,20),
    "crsmith": Skater("Craig Smith", 50, 30, 60, 45),
    "teravainen": Skater("Teuvo Teravainen", 60, 60, 30, 60),
    "donato": Skater("Ryan Donato", 50, 55, 50, 40),
    "joanderson": Skater("Joey Anderson", 50, 60, 30, 65),
    "maroon": Skater("Patrick Maroon", 30, 40, 40, 40),
    "reichel": Skater("Lukas Reichel", 30, 50, 30, 30),
    "nazar": Skater("Frank Nazar", 50, 50, 50, 20),
    "hall": Skater("Taylor Hall", 50, 50, 50, 20),
    "slaggert": Skater("Nolan Slaggert", 50, 50, 50, 20),
    "mikheyev": Skater("Ilya Mikheyev", 55, 60, 55, 60),
    "sjones": Skater("Seth Jones", 40, 55, 60, 55),
    "avlassic": Skater("Alex Vlassic", 35, 30, 50, 70),
    "murphy": Skater("Connor Murphy", 60, 20, 50, 70),
    "martinez": Skater("Alec Martinez", 60, 30, 40, 55),
    "brodie": Skater("TJ Brodie", 30, 50, 35,65),
    "korchinski": Skater("Kevin Korchinski", 60, 20, 50, 20),
    # Avalanche
    "mackinnon": Skater("Nathan MacKinnon", 85, 90, 85, 30),
    "rantanen": Skater("Mikko Rantanen", 80, 60, 70,20),
    "mittelstadt": Skater("Casey Mittelstadt", 60, 70, 55, 55),
    "lehkonen": Skater("Artturi Lehkonen", 60, 60, 65, 80),
    "colton": Skater("Ross Colton", 45, 55, 60, 40),
    "wood": Skater("Miles Wood", 20, 65, 55, 20),
    "drouin": Skater("Jonathan Drouin", 55, 60, 60,40),
    "kiviranta": Skater("Joel Kiviranta", 20, 20, 35, 60),
    "kovalenko": Skater("Nikolai Kovalenko", 50, 50, 50, 30 ),
    "landeskog": Skater("Gabriel Landeskog", 60, 60, 60, 60),
    "loconnor": Skater("Logan O'Connor", 40, 50, 60, 80),
    "kelly": Skater("Parker Kelly", 20, 20, 20, 60),
    "wagner": Skater("Chris Wagner", 30, 30, 30, 30),
    "makar": Skater("Cale Makar", 80, 70, 50, 65),
    "toews": Skater("Devon Toews", 65, 65, 60, 70),
    "girard": Skater("Samuel Girard", 55, 60, 60, 40),
    "manson": Skater("Josh Manson", 60, 70, 50, 50),
    "brannstrom": Skater("Erik Brannstrom", 20, 50, 60, 60),
    "dehaan": Skater("Calvin deHaan", 40, 40, 55, 60),
    "kmiddleton": Skater("Keaton Middleton", 30, 30, 30, 50),
    # Blue Jackets
    "jenner": Skater("Boone Jenner", 60, 30, 55, 55),
    "marchenko": Skater("Kirill Marchenko", 60, 30, 30, 50),
    "gaudreau": Skater("Johnny Gaudreau", 40, 80, 80, 20),
    "kjohnson": Skater("Kent Johnson", 55, 60, 20, 40),
    "kuraly": Skater("Sean Kuraly", 50, 30, 35, 40),
    "chinakhov": Skater("Yegor Chinakhov", 60, 30, 30, 60),
    "olivier": Skater("Mathieu Olivier", 30, 30, 50, 55),
    "danforth": Skater("Justin Danforth", 40, 30, 60, 60),
    "brindley": Skater("Gavin Brindley", 30, 30, 30,30),
    "fantilli": Skater("Adam Fantilli", 60, 60, 30,30),
    "monahan": Skater("Sean Monahan", 55, 65, 60,30),
    "laine": Skater("Patrik Laine", 80, 50, 50, 40),
    "voronkov": Skater("Dimitri Voronkov", 50, 60, 65,30),
    "sillinger": Skater("Cole Sillinger", 20, 40, 40,30),
    "werenski": Skater("Zach Werenski", 60, 80, 70, 40),
    "severson": Skater("Damon Severson", 60, 60, 80, 55),
    "provorov": Skater("Ivan Provorov", 55, 35, 50, 30),
    "gudbranson": Skater("Erik Gudbranson", 50, 35, 20, 30),
    "jjohnson": Skater("Jack Johnson", 35, 35, 20, 30),
    # Stars
    "robertson": Skater("Jason Robertson", 80, 70, 80, 80),
    "hintz": Skater("Roope Hintz", 70, 65, 70, 60),
    "benn": Skater("Jamie Benn", 60, 60, 70, 30),
    "seguin": Skater("Tyler Seguin", 65, 50, 70,20),
    "marchment": Skater("Mason Marchment", 60, 65, 60,60),
    "dadonov": Skater("Evgeni Dadonov", 55, 30,50, 40),
    "johnston": Skater("Wyatt Johnston", 60, 60, 60, 55),
    "stankoven": Skater("Logan Stankoven", 40, 65, 65, 60),
    "steel": Skater("Sam Steel", 35, 50, 50, 60),
    "duchene": Skater("Matt Duchene", 65, 65, 60,20),
    "bourque": Skater("Mavrik Bourque", 50, 50, 50, 30),
    "heiskanen": Skater("Miro Heiskanen", 30, 60, 70,70),
    "lindell": Skater("Esa Lindell", 50, 55, 60, 70),
    "harley": Skater("Thomas Harley", 80, 55, 70, 45),
    "lundkvist": Skater("Nils Lundkvist", 45, 50, 50, 30),
    "lyubushkin": Skater("Ilya Lyubushkin", 30, 40, 30, 45),
    "dumba": Skater("Matt Dumba", 40, 30, 30, 30),
    "bsmith": Skater("Brendan Smith", 50, 20, 30, 50),
    # Red Wings
    "larkin": Skater("Dylan Larkin", 70, 70, 70, 55),
    "raymond": Skater("Lucas Raymond", 65, 50, 30, 30),
    "debrincat": Skater("Alex DeBrincat", 60, 60, 65, 30),
    "pkane": Skater("Patrick Kane", 70, 60, 20, 20),
    "copp": Skater("Andrew Copp", 40, 50, 30, 50),
    "compher": Skater("JT Compher", 60, 55, 50, 70),
    "rasmussen": Skater("Michael Rasmussen", 40, 60, 50, 55),
    "veleno": Skater("Joe Veleno", 50, 30, 30,45),
    "tarasenko": Skater("Vladimir Tarasenko", 65, 60, 60, 20),
    "fischer": Skater("Christian Fischer", 30, 40, 50, 45),
    "motte": Skater("Tyler Motte", 30, 40, 35, 60),
    "seider": Skater("Moritz Seider", 50, 60, 30, 55),
    "chiarot": Skater("Ben Chiarot", 50, 60, 30, 35),
    "holl": Skater("Justin Holl", 30, 20, 40, 40),
    "maatta": Skater("Olli Maatta", 50, 45, 30, 60),
    "petry": Skater("Jeff Petry", 60, 55, 50, 55),
    "gustafsson": Skater("Erik Gustafsson", 50, 65, 60, 60),
    # Oilers
    "mcdavid": Skater("Connor McDavid", 80, 90, 90, 60),
    "draisaitl": Skater("Leon Draisaitl", 90, 85, 80,20),
    "hyman": Skater("Zach Hyman", 70, 60, 85, 35),
    "ekane": Skater("Evander Kane", 45, 30, 30,20),
    "nuge": Skater("Ryan Nugent-Hopkins", 40, 60, 60, 60),
    "henrique": Skater("Adam Henrique", 60, 45, 60, 45),
    "mcleod": Skater("Ryan McLeod", 50, 60, 60, 65),
    "ryan": Skater("Derek Ryan", 40, 30, 55, 70),
    "arvidsson": Skater("Viktor Arvidsson", 50, 50, 65, 40),
    "perry": Skater("Corey Perry", 40, 40, 50, 60),
    "skinner": Skater("Jeff Skinner", 65, 70, 80,20),
    "holloway": Skater("Dylan Holloway", 40, 20, 30, 50),
    "janmark": Skater("Mattias Janmark", 30, 40, 30, 60),
    "brown": Skater("Connor Brown", 20, 50, 50, 50),
    "nurse": Skater("Darnell Nurse", 70, 60, 70,50),
    "ekholm": Skater("Mattias Ekholm", 55, 80, 80, 65),
    "bouchard": Skater("Evan Bouchard", 70, 60, 80, 45),
    "ceci": Skater("Cody Ceci", 45, 30, 35, 30),
    "kulak": Skater("Brett Kulak", 50, 30, 40, 50),
    "broberg": Skater("Philip Broberg", 30, 55, 55, 40),
    # Panthers
    "mtkachuk": Skater("Matthew Tkachuk", 30, 80, 90, 35),
    "barkov": Skater("Aleksander Barkov", 60, 80, 70, 85),
    "bennett": Skater("Sam Bennett", 50, 60, 65, 60),
    "reinhart": Skater("Sam Reinhart", 85, 65, 60, 85),
    "verhaeghe": Skater("Carter Verhaeghe", 70, 60, 70, 30),
    "rodrigues": Skater("Evan Rodrigues", 20, 50, 65, 80),
    "luostarainen": Skater("Eetu Luostarainen", 40, 40, 60, 70),
    "gadjovich": Skater("Jonah Gadjovich", 20, 30, 45, 40),
    "jboqvist": Skater("Jesper Boqvist", 55, 45, 40, 60),
    "lundell": Skater("Anton Lundell", 30, 40, 45, 40),
    "greer": Skater("AJ Greer", 30, 30, 45, 55),
    "nosek": Skater("Tomas Nosek", 20, 45, 30, 45),
    "ekblad": Skater("Aaron Ekblad", 70, 60, 60, 55),
    "forsling": Skater("Gustav Forsling", 70, 80, 60, 65),
    "kulikov": Skater("Dimitry Kulikov", 30,60, 40, 40),
    "mikkola": Skater("Niko Mikkola", 30, 30, 30, 60),
    "schmidt": Skater("Nate Schmidt", 40, 35, 50, 55),
    "balinskis": Skater("Uvis Balinskis", 35, 30, 30, 40),
    "bjornfoot": Skater("Tobias Bjornfoot", 30, 30, 30, 30),
    # Kings
    "kopitar": Skater("Anze Kopitar", 65, 60, 60, 60),
    "byfield": Skater("Quinton Byfield", 35, 65, 60, 80),
    "fiala": Skater("Kevin Fiala", 60, 80, 80,55),
    "danault": Skater("Phillip Danault", 60, 55, 60, 60),
    "kempe": Skater("Adrian Kempe", 70, 40, 60, 50),
    "jeannot": Skater("Tanner Jeannot", 50, 30, 45, 50),
    "moore": Skater("Trevor Moore", 55, 60, 55, 70),
    "lafferiere": Skater("Alexis Lafferiere", 30, 20, 35, 30),
    "foegle": Skater("Warren Foegle", 30, 60, 70, 50),
    "kaliyev": Skater("Arthur Kaliyev", 35, 50, 60, 45),
    "doughty": Skater("Drew Doughty", 65, 50, 55,80),
    "gavrikov": Skater("Vladislav Gavrikov", 50, 50, 55, 50),
    "manderson": Skater("Mikey Anderson", 30, 35, 20, 65),
    "englund": Skater("Andreas Englund", 30, 30, 30, 60),
    "spence": Skater("Jordan Spence", 30, 60, 60, 35),
    "edmundson": Skater("Joel Edmundson", 40, 20, 55, 20),
    "moverare": Skater("Jacob Moverare", 20, 20, 50, 50),
    "burroughs": Skater("Kyle Burroughs", 35, 30, 45, 55),
    # Wild
    "kaprizov": Skater("Kirill Kaprizov", 85, 65, 80, 60),
    "boldy": Skater("Matthew Boldy", 60, 55, 70, 70),
    "ek": Skater("Joel Eriksson-Ek", 30, 60, 60, 65),
    "zuccarello": Skater("Mats Zuccarello", 60, 80, 55, 40),
    "mfoligno": Skater("Marcus Foligno", 55, 50, 60, 70),
    "hartman": Skater("Ryan Hartman", 60, 60, 60, 30),
    "fgaudreau": Skater("Frederick Gaudreau", 40, 30, 20, 35),
    "johansson": Skater("Marcus Johansson", 45, 35, 55, 60),
    "kushnutdinov": Skater("Marat Kushnutdinov", 50, 50, 45, 30),
    "rossi": Skater("Marco Rossi", 55, 30, 40, 40),
    "ohgren": Skater("Liam Ohgren", 35, 35, 35, 35),
    "trenin": Skater("Yakov Trenin", 30, 20, 50, 70),
    "lauko": Skater("Jakub Lauko", 20, 50, 30, 55),
    "brodin": Skater("Jonas Brodin", 55, 30, 50, 70),
    "middleton": Skater("Jake Middleton", 40, 40, 20, 40),
    "bogosian": Skater("Zach Bogosian", 30, 45, 45,45),
    "spurgeon": Skater("Jared Spurgeon", 60, 50, 65, 85),
    "merrill": Skater("Jon Merrill", 45, 40, 20, 50),
    "faber": Skater("Brock Faber", 45, 70, 40, 50),
    # Canadiens
    "suzuki": Skater("Nick Suzuki", 70, 60, 55, 50),
    "caufield": Skater("Cole Caufield", 65, 45, 60, 20),
    "gallagher": Skater("Brendan Gallagher", 20, 55, 60, 40),
    "anderson": Skater("Josh Anderson", 20, 30, 60, 20),
    "dvorak": Skater("Christian Dvorak", 35, 35, 35, 20),
    "armia": Skater("Joel Armia", 60, 30, 55, 60),
    "newhook": Skater("Alex Newhook", 60, 50, 50, 30),
    "evans": Skater("Jake Evans", 30, 60, 50, 60),
    "harvey": Skater("Rafael Harvey-Pinard", 35, 50, 45, 65),
    "slafkovsky": Skater("Juraj Slafkovsky", 55, 30, 55, 40),
    "pezzetta": Skater("Michael Pezzetta", 45, 55, 30, 45),
    "dach": Skater("Kriby Dach", 50, 30, 35, 35),
    "matheson": Skater("Mike Matheson", 65, 70, 45,45),
    "savard": Skater("David Savard", 40, 50, 60, 20),
    "harris": Skater("Jordan Harris", 55, 60, 60, 55),
    "hutson": Skater("Lane Hutson", 50, 40, 40, 45),
    "guhle": Skater("Kaiden Guhle", 60, 70, 20, 65),
    "xhekaj": Skater("Arber Xhekaj", 50, 50, 35, 30),
    # Predators
    "forsberg": Skater("Filip Forsberg", 85, 60, 70, 55),
    "oreilly": Skater("Ryan O'Reilly", 60, 45, 65, 65),
    "novak": Skater("Tommy Novak", 65, 55, 65, 20),
    "nyquist": Skater("Gustav Nyquist", 60, 70, 45, 20),
    "sissons": Skater("Colton Sissons", 30, 40, 55, 40),
    "glass": Skater("Cody Glass", 20, 30, 30, 50),
    "stamkos": Skater("Steven Stamkos", 80, 70, 45, 30),
    "marchessault": Skater("Jonathan Marchessault", 70, 60, 65, 50),
    "csmith": Skater("Cole Smith", 20, 45, 40, 60),
    "mccarron": Skater("Michael McCarron", 45, 30, 45, 40),
    "jankowski": Skater("Mark Jankowski", 50, 20, 40, 60),
    "evangelista": Skater("Luke Evangelista", 50, 70, 60, 40),
    "josi": Skater("Roman Josi", 85, 90, 80, 40),
    "skjei": Skater("Brady Skjei", 70, 60, 40, 65),
    "lschenn": Skater("Luke Schenn", 40, 55, 30, 35),
    "fabbro": Skater("Dante Fabbro", 35, 55, 50, 60),
    "acarrier": Skater("Alexandre Carrier", 20, 45, 50, 65),
    "lauzon": Skater("Jeremy Lauzon", 40, 20, 45, 50),
    # Devils
    "jhughes": Skater("Jack Hughes", 70, 65, 80, 45),
    "hischier": Skater("Nico Hischier", 55, 80, 80, 35),
    "meier": Skater("Timo Meier", 70, 50, 70, 30),
    "bratt": Skater("Jesper Bratt", 60, 80, 85, 30),
    "palat": Skater("Ondrej Palat", 50, 60, 65, 70),
    "haula": Skater("Erik Haula", 40, 60, 60, 70),
    "lazar": Skater("Curtis Lazar", 30, 35, 40, 60),
    "nfoote": Skater("Nolan Foote", 30, 30, 40, 40),
    "mercer": Skater("Dawson Mercer", 60, 50, 60, 35),
    "cotter": Skater("Paul Cotter", 35, 35, 30, 20),
    "tatar": Skater("Tomas Tatar", 50, 35, 60, 55),
    "noesen": Skater("Stefan Noesen", 20, 60, 65, 55),
    "hamilton": Skater("Dougie Hamilton", 80, 60, 85, 35),
    "siegenthaler": Skater("Jonas Siegenthaler", 30, 35, 20, 65),
    "dillon": Skater("Brenden Dillon", 50, 45, 45, 70),
    "pesce": Skater("Brett Pesce", 45, 40, 65, 55),
    "lhughes": Skater("Luke Hughes", 65, 35, 60, 30),
    "macdermid": Skater("Kurtis MacDermid", 40, 40, 35, 30),
    "nemec": Skater("Simon Nemec", 20, 70, 70, 30),
    "desimone": Skater("Nick DeSimone", 50, 20, 50, 20),
    # Islanders
    "barzal": Skater("Mat Barzal", 60, 85, 65, 30),
    "horvat": Skater("Bo Horvat", 80, 60, 65, 50),
    "lee": Skater("Anders Lee", 55, 20, 70, 55),
    "nelson": Skater("Brock Nelson", 80, 65, 60, 30),
    "pageau": Skater("JG Pageau", 35, 60, 60, 60),
    "palmieri": Skater("Kyle Palmieri", 60, 50, 65, 35),
    "engvall": Skater("Pierre Engvall", 50, 50, 70, 70),
    "cizikas": Skater("Casey Cizikas", 35, 30, 30, 60),
    "gauthier": Skater("Julien Gauthier", 50, 30, 35, 30),
    "fasching": Skater("Hudson Fasching", 50, 55, 50, 60),
    "maclean": Skater("Kyle MacLean", 50, 50, 30, 60),
    "duclair": Skater("Anthony Duclair", 70, 70, 65,20),
    "holmstrom": Skater("Simon Holmstrom", 65, 30, 20, 65),
    "wahlstrom": Skater("Oliver Wahlstrom", 35, 30, 35, 35),
    "pulock": Skater("Ryan Pulock", 40, 40, 45, 55),
    "pelech": Skater("Adam Pelech", 35, 60, 35, 85),
    "dobson": Skater("Noah Dobson", 70, 80, 60, 35),
    "romanov": Skater("Alexander Romanov", 50, 50, 50, 35),
    "bolduc": Skater("Samuel Bolduc", 55, 20, 40, 35),
    "mayfield": Skater("Scott Mayfield", 40, 50, 30, 60),
    "mireilly": Skater("Mike Reilly", 35, 60, 60, 60),
    # Rangers
    "panarin": Skater("Artemi Panarin", 85, 70, 80, 40),
    "kreider": Skater("Chris Kreider", 70, 30, 70, 55),
    "zibanejad": Skater("Mika Zibanejad", 65, 70, 40, 55),
    "trocheck": Skater("Vincent Trocheck", 20, 80, 70, 50),
    "chytil": Skater("Filip Chytil", 50, 50, 50, 50),
    "lafreniere": Skater("Alexis Lafreniere", 60, 50, 50, 30),
    "kakko": Skater("Kaapo Kakko", 60, 35, 40, 50),
    "rsmith": Skater("Reilly Smith", 40, 65, 55, 50),
    "edstrom": Skater("Adam Edstrom", 50, 50, 50, 50),
    "cuylle": Skater("Will Cuylle", 50, 20, 40, 60),
    "rempe": Skater("Matt Rempe", 20, 20, 20, 40),
    "vesey": Skater("Jimmy Vesey", 30, 30, 60, 70),
    "carrick": Skater("Sam Carrick", 40, 30, 20, 30),
    "fox": Skater("Adam Fox", 70, 80, 80, 70),
    "trouba": Skater("Jacob Trouba", 30, 60, 55,35),
    "zjones": Skater("Zachary Jones", 45, 40, 35, 30),
    "kmiller": Skater("K'Andre Miller", 60, 45, 30, 60),
    "lindgren": Skater("Ryan Lindgren", 20, 60, 20, 60),
    # Senators
    "stuetzle": Skater("Tim Stuetzle", 50, 60, 60, 35),
    "giroux": Skater("Claude Giroux", 65, 60, 70, 50),
    "btkachuk": Skater("Brady Tkachuk", 50, 80, 85, 30),
    "batherson": Skater("Drake Batherson", 60, 60, 50, 35),
    "greig": Skater("Ridley Greig", 50, 60, 65,60),
    "macewen": Skater("Zack MacEwen", 30, 30),
    "pinto": Skater("Shane Pinto", 20, 40, 50, 70),
    "perron": Skater("David Perron", 60, 55, 45, 50),
    "amadio": Skater("Michael Amadio", 60, 40, 45, 60),
    "gregor": Skater("Noah Gregor", 20, 40, 45, 20),
    "norris": Skater("Josh Norris", 80, 20, 30, 40),
    "sanderson": Skater("Jake Sanderson", 50, 50, 60, 65),
    "chabot": Skater("Thomas Chabot", 60, 40, 80, 35),
    "zub": Skater("Artem Zub", 45, 50, 30, 70),
    "jensen": Skater("Nick Jensen", 40, 65, 45, 60),
    "hamonic": Skater("Travis Hamonic", 55, 35, 35, 20),
    "docker": Skater("Jacob Bernard-Docker", 45, 30, 20, 55),
    # Flyers
    "konecny": Skater("Travis Konecny", 60, 70, 70, 20),
    "tippett": Skater("Owen Tippett", 60, 60, 70, 30),
    "michkov": Skater("Matvei Michkov", 60, 50, 60, 30),
    "couturier": Skater("Sean Couturier", 20, 50, 60, 60),
    "farabee": Skater("Joel Farabee", 60, 60, 60, 30),
    "laughton": Skater("Scott Laughton", 40, 30,55,20),
    "cates": Skater("Noah Cates", 30, 40, 60, 70),
    "hathaway": Skater("Garnet Hathaway", 40, 30, 50, 70),
    "frost": Skater("Morgan Frost", 30, 60, 60, 60),
    "poehling": Skater("Ryan Poehling", 40, 50, 60, 40),
    "deslauriers": Skater("Nicolas Deslauriers", 30, 20, 20, 45),
    "foerster": Skater("Tyson Foerster", 50, 20, 50, 80),
    "brink": Skater("Bobby Brink", 50, 60, 30, 40),
    "sanheim": Skater("Travis Sanheim", 40, 60, 60, 45),
    "seeler": Skater("Nick Seeler", 35, 50, 50, 60),
    "drysdale": Skater("Jamie Drysdale", 45, 40, 30, 20),
    "york": Skater("Cam York", 50, 50, 60, 60),
    "ejohnson": Skater("Erik Johnson", 50, 30, 55, 30),
    "risto": Skater("Rasmus Ristolainen", 20, 30, 60, 60),
    # Penguins
    "crosby": Skater("Sidney Crosby", 65, 80, 85, 30),
    "malkin": Skater("Evgeni Malkin", 65, 70, 70, 35),
    "rust": Skater("Bryan Rust", 55, 50, 60, 40),
    "rakell": Skater("Rickard Rakell", 40, 30, 60, 50),
    "bunting": Skater("Michael Bunting", 45, 70, 60, 20),
    "eller": Skater("Lars Eller", 40, 35, 35, 70),
    "oconnor": Skater("Drew O'Connor", 35, 40, 55, 35),
    "puljujarvi": Skater("Jesse Puljujarvi", 20, 30, 45, 60),
    "hayes": Skater("Kevin Hayes", 50, 55, 60, 40),
    "beauvilier": Skater("Anthony Beauvilier", 20, 45, 40, 30),
    "acciari": Skater("Noel Acciari", 30, 20, 45, 60),
    "ekarlsson": Skater("Erik Karlsson", 80, 90, 90, 20),
    "letang": Skater("Kris Letang", 70, 60, 60, 20),
    "mpettersson": Skater("Marcus Pettersson", 20, 70, 65, 70),
    "ludvig": Skater("John Ludvig", 50, 30, 45, 40),
    "grzelyck": Skater("Matt Grzelyck", 45, 60, 35, 30),
    "graves": Skater("Ryan Graves", 55, 35, 55, 40),
    "saho": Skater("Sebastian Aho", 55, 30, 50, 45),
    # Sharks
    "granlund": Skater("Mikael Granlund", 30, 50, 50, 20),
    "couture": Skater("Logan Couture", 40, 50, 50, 30),
    "goodrow": Skater("Barclay Goodrow", 40, 45, 30, 35),
    "kostin": Skater("Klim Kostin", 60, 45, 20, 45),
    "sturm": Skater("Nico Sturm", 40, 40, 45, 35),
    "toffoli": Skater("Tyler Toffoli", 65, 50, 65, 50),
    "zetterlund": Skater("Fabian Zetterlund", 50, 55, 50, 20),
    "wsmith": Skater("Will Smith", 50, 30),
    "celebrini": Skater("Macklin Celebrini", 50, 50),
    "eklund": Skater("William Eklund", 45, 40, 45, 50),
    "dellandrea": Skater("Ty Dellandrea", 20, 50, 30, 60),
    "wennberg": Skater("Alexander Wennberg", 40, 50, 30, 65),
    "kunin": Skater("Luke Kunin", 35, 30, 20,20),
    "bordeleau": Skater("Thomas Bordeleau", 50, 35, 45, 30),
    "afanaseyev": Skater("Egor Afanaseyev", 40, 30, 40, 30),
    "grundstrom": Skater("Carl Grundstrom", 55, 30, 55, 50),
    "vlassic": Skater("Marc-Eduoard Vlassic", 50, 30, 55, 40),
    "ferraro": Skater("Mario Ferraro", 20, 35, 40, 35),
    "rutta": Skater("Jan Rutta", 45, 20, 20, 50),
    "benning": Skater("Matt Benning", 20, 60, 30, 45),
    "walman": Skater("Jake Walman", 65, 20, 55, 55),
    # Kraken
    "mccann": Skater("Jared McCann", 80, 60, 60, 55),
    "tolvanen": Skater("Eeli Tolvanen", 55, 45, 30, 60),
    "burakovsky": Skater("Andre Burakovsky", 60, 60, 50, 20),
    "schwartz": Skater("Jaden Schwartz", 30, 50, 50, 65),
    "gourde": Skater("Yanni Gourde", 30, 60, 60, 60),
    "eberle": Skater("Jordan Eberle", 50, 70, 80, 45),
    "btanev": Skater("Brandon Tanev", 35, 40, 30, 60),
    "beniers": Skater("Matty Beniers", 60, 55, 20, 80),
    "wright": Skater("Shane Wright", 30, 50),
    "stephenson": Skater("Chandler Stephenson", 55, 70, 35, 30),
    "dunn": Skater("Vince Dunn", 80, 65, 80, 40),
    "oleksiak": Skater("Jamie Oleksiak", 40, 45, 70, 55),
    "larsson": Skater("Adam Larsson", 55, 50, 20, 45),
    "montour": Skater("Brandon Montour", 65, 50, 60, 35),
    "borgen": Skater("William Borgen", 40, 60, 45, 50),
    # Blues
    "thomas": Skater("Robert Thomas", 65, 80, 65, 30),
    "kyrou": Skater("Jordan Kyrou", 70, 65, 55, 50),
    "bschenn": Skater("Brayden Schenn", 60, 60, 35, 30),
    "buchnevich": Skater("Pavel Buchnevich", 65, 60, 70, 65),
    "saad": Skater("Brandon Saad", 65, 50, 60, 30),
    "sundqvist": Skater("Oskar Sundqvist", 35, 45, 30, 30),
    "faksa": Skater("Radek Faksa", 30, 40, 20, 65),
    "joseph": Skater("Mathieu Joseph", 45, 65, 35, 60),
    "toropchenko": Skater("Alexey Toropchenko", 55, 30, 30, 50),
    "kapanen": Skater("Kasperi Kapanen", 35, 55, 40, 30),
    "neighbours": Skater("Jake Neighbours", 70, 20, 35, 30),
    "texier": Skater("Alexandre Texier", 55, 50, 50, 30),
    "faulk": Skater("Justin Faulk", 60, 70, 50, 30),
    "krug": Skater("Torey Krug", 30, 60, 55, 20),
    "parayko": Skater("Colton Parayko", 50, 35, 20, 70),
    "leddy": Skater("Nick Leddy", 30, 60, 55, 30),
    "perunovich": Skater("Scott Perunovich", 20, 60, 50, 35),
    "tucker": Skater("Tyler Tucker", 45, 20, 20, 50),
    # Lightning
    "kucherov": Skater("Nikita Kucherov", 70, 85, 80, 30),
    "point": Skater("Brayden Point", 90, 60, 80, 30),
    "hagel": Skater("Brandon Hagel", 60, 65, 65, 65),
    "cirelli": Skater("Anthony Cirelli", 50, 55, 60, 80),
    "paul": Skater("Nicholas Paul", 60, 35, 20, 80),
    "guentzel": Skater("Jake Guentzel", 40, 70, 80, 20),
    "sheary": Skater("Conor Sheary", 45, 60, 50, 30),
    "eyssimont": Skater("Mikey Eyssimont", 30, 40, 60, 60),
    "atkinson": Skater("Cam Atkinson", 30, 45, 40, 20),
    "girgensons": Skater("Zemgus Girgensons", 45, 20, 40, 50),
    "glendening": Skater("Luke Glendening", 35, 20, 20, 55),
    "chaffee": Skater("Mitchell Chaffee", 50, 20, 35, 35),
    "hedman": Skater("Victor Hedman", 65, 80, 70, 35),
    "mcdonagh": Skater("Ryan McDonagh", 30, 60, 70, 60),
    "cernak": Skater("Erik Cernak", 35, 50, 35, 60),
    "moser": Skater("JJ Moser", 55, 60, 50, 40),
    "perbix": Skater("Nick Perbix", 45, 60, 40, 60),
    # Maple Leafs
    "matthews": Skater("Auston Matthews", 90, 70, 90, 60),
    "nylander": Skater("William Nylander", 70, 65, 80,20),
    "marner": Skater("Mitch Marner", 80, 90, 60, 60),
    "tavares": Skater("John Tavares", 55, 55, 70, 55),
    "jarnkrok": Skater("Calle Jarnkrok", 60, 45, 50, 45),
    "kampf": Skater("David Kampf", 40, 30, 20, 55),
    "mcmann": Skater("Bobby McMann", 55, 30, 45, 60),
    "reaves": Skater("Ryan Reaves", 35, 30, 30, 40),
    "nrobertson": Skater("Nicholas Robertson", 65, 55, 45, 40),
    "knies": Skater("Matthew Knies", 55, 60, 40, 60),
    "domi": Skater("Max Domi", 35, 85, 65, 20),
    "dewar": Skater("Connor Dewar", 35, 35, 35, 70),
    "holmberg": Skater("Pontus Holmberg", 50, 60, 35, 60),
    "cowan": Skater("Easton Cowan", 40, 30),
    "minten": Skater("Fraser Minten", 30, 30),
    "rielly": Skater("Morgan Rielly", 35, 85, 60, 20),
    "ctanev": Skater("Chris Tanev", 40, 50, 60, 90),
    "benoit": Skater("Simon Benoit", 30, 20, 20, 45),
    "mccabe": Skater("Jake McCabe", 55, 60, 60, 60),
    "liljgren": Skater("Timothy Liljgren", 60, 35, 60, 60),
    "webber": Skater("Cade Webber", 30, 50),
    "oel": Skater("Oliver Ekman-Larsson", 55, 60, 55, 35),
    "timmins": Skater("Conor Timmins", 45, 65, 60, 50),
    # Utah Hockey Club
    "keller": Skater("Clayton Keller", 80, 70, 60, 30),
    "maccelli": Skater("Mattias Maccelli", 50, 60, 60, 55),
    "schmaltz": Skater("Nick Schmaltz", 65, 65, 60, 40),
    "crouse": Skater("Lawson Crouse", 60, 50, 60, 45),
    "kerfoot": Skater("Alex Kerfoot", 30, 65, 30, 60),
    "bjugstad": Skater("Nick Bjugstad", 60, 35, 60, 45),
    "mcbain": Skater("Jack McBain", 45, 60, 55, 30),
    "cooley": Skater("Logan Cooley", 60, 55, 50, 50),
    "hayton": Skater("Barrett Hayton", 20, 30, 60, 65),
    "stenlund": Skater("Kevin Stenlund", 35, 30, 30, 60),
    "carcone": Skater("Michael Carcone", 70, 20, 45, 20),
    "durzi": Skater("Sean Durzi", 55, 50, 50, 40),
    "cole": Skater("Ian Cole", 35, 40, 55, 70),
    "marino": Skater("John Marino", 30, 60, 30, 65),
    "valimaki": Skater("Juuso Valimaki", 20, 50, 65, 70),
    "sergachev": Skater("Mikhail Sergachev", 50, 65, 60,50),
    "kesselring": Skater("Michael Kesselring", 50, 50, 50, 30),
    # Canucks
    "pettersson": Skater("Elias Pettersson", 70, 80, 70, 60),
    "miller": Skater("JT Miller", 80, 65, 60, 50),
    "boeser": Skater("Brock Boeser", 60, 60, 40, 30),
    "garland": Skater("Conor Garland", 60, 60, 60, 70),
    "psuter": Skater("Pius Suter", 55, 40, 50, 80),
    "hoglander": Skater("Nils Hoglander", 65, 55, 60, 60),
    "podkolzin": Skater("Vasaily Podkolzin", 35, 30, 40, 45),
    "aman": Skater("Nils Aman", 30, 40, 20, 60),
    "heinen": Skater("Danton Heinen", 55, 60, 60, 55),
    "sherwood": Skater("Kieffer Sherwood", 55, 55, 45, 50),
    "phidi": Skater("Phil Di Gisueppe", 45, 30, 45, 50),
    "blueger": Skater("Teddy Blueger", 20, 60, 60, 60),
    "joshua": Skater("Dakota Joshua", 60, 45, 60, 45),
    "debrusk": Skater("Jake DeBrusk", 60, 50, 70, 60),
    "qhughes": Skater("Quinn Hughes", 60, 70, 70, 60),
    "hronek": Skater("Filip Hronek", 30, 60, 45, 40),
    "soucy": Skater("Carson Soucy", 60, 30, 35, 60),
    "myers": Skater("Tyler Myers", 30, 60, 50, 50),
    "forbort": Skater("Derek Forbort", 45, 40, 30, 60),
    "desharnais": Skater("Vincent Desharnais", 30, 35, 45, 55),
    "friedman": Skater("Mark Friedman", 20, 20, 50, 50),
    # Golden Knights
    "eichel": Skater("Jack Eichel", 80, 60, 60, 70),
    "stone": Skater("Mark Stone", 60, 70, 80, 80),
    "hertl": Skater("Tomas Hertl", 50, 60, 65, 35),
    "wkarlsson": Skater("William Karlsson", 60, 60, 65, 70),
    "barbashev": Skater("Ivan Barbashev", 60, 65, 60, 20),
    "nroy": Skater("Nicolas Roy", 35, 60, 55, 60),
    "howden": Skater("Brett Howden", 40, 40, 35, 35),
    "kolesar": Skater("Keegan Kolesar", 40, 50, 40, 50),
    "holtz": Skater("Alexander Holtz", 55, 40, 40, 30),
    "olofsson": Skater("Victor Olofsson", 60, 35, 30, 30),
    "dorofeyev": Skater("Pavel Dorofeyev", 60, 40, 50, 60),
    "rondbjerg": Skater("Jonas Rondbjerg", 20, 45, 20, 60),
    "pietrangelo": Skater("Alex Pietrangelo", 60, 60, 80, 35),
    "hanafin": Skater("Noah Hanafin", 60, 60, 65, 50),
    "theodore": Skater("Shea Theodore", 60, 85, 70, 20),
    "mcnabb": Skater("Brayden McNabb", 30, 45, 50, 80),
    "hague": Skater("Nick Hague", 30, 35, 50, 50),
    "whitecloud": Skater("Zach Whitecloud", 55, 45, 40, 60),
    # Capitals
    "ovi": Skater("Alexander Ovechkin", 70, 55, 60, 20),
    "dubois": Skater("Pierre-Luc Dubois", 30, 60, 65, 35),
    "dstrome": Skater("Dylan Strome", 60, 60, 70, 60),
    "oshie": Skater("TJ Oshie", 45, 30, 30,30),
    "wilson": Skater("Tom Wilson", 45, 35, 45, 65),
    "protas": Skater("Aliaksi Protas", 20, 55,55,60),
    "milano": Skater("Sonny Milano", 70, 50, 60, 60),
    "dowd": Skater("Nic Dowd", 60, 50, 40, 70),
    "mangiapane": Skater("Andrew Mangiapane", 50, 60, 70, 35),
    "mcmichael": Skater("Connor McMichael", 45, 50, 45, 35),
    "duhaime": Skater("Brandon Duhaime", 35, 35, 50, 40),
    "jcarlson": Skater("John Carlson", 65, 60, 85, 35),
    "sandin": Skater("Rasmus Sandin", 60, 55, 60, 20),
    "chychrun": Skater("Jakob Chychrun", 65, 55, 55,40),
    "tvr": Skater("Trevor Van Riemsdyk", 40, 50, 55, 70),
    "fehervary": Skater("Martin Fehervary", 60, 35, 35, 60),
    "mroy": Skater("Matt Roy", 50, 60, 65, 80),
    "bear": Skater("Ethan Bear", 35, 30, 35, 45),
    # Jets
    "connor": Skater("Kyle Connor", 80, 45, 60, 20),
    "lowry": Skater("Adam Lowry", 30, 40, 65, 70),
    "perfetti": Skater("Cole Perfetti", 50, 65, 30, 60),
    "vilardi": Skater("Gabriel Vilardi", 70, 50, 45, 50),
    "iafallo": Skater("Alex Iafallo", 35, 50, 45, 80),
    "niederreiter": Skater("Nino Niederreiter", 60, 40, 60, 60),
    "appleton": Skater("Mason Appleton", 45, 40, 60, 35),
    "ehlers": Skater("Nikolai Ehlers", 60, 80, 80, 40),
    "namestnikov": Skater("Vladislav Namestnikov", 35, 50, 50, 60),
    "barron": Skater("Morgan Barron", 35, 30, 45, 45),
    "kupari": Skater("Rasmus Kupari", 20, 45, 30, 55),
    "scheifele": Skater("Mark Scheifele", 70, 60, 65, 20),
    "morrissey": Skater("Josh Morrissey", 65, 80, 85, 40),
    "pionk": Skater("Neal Pionk", 45, 45, 35, 30),
    "demelo": Skater("Dylan DeMelo", 30, 60, 30, 80),
    "stanley": Skater("Logan Stanley", 35, 30, 45, 35),
    "samberg": Skater("Dylan Samberg", 35, 55, 45, 55),

    # Free Agents
    "sprong": Skater("Daniel Sprong", 60, 30),
    "jvr": Skater("James van Riemsdyk", 40, 50),
    "schultz": Skater("Justin Schultz", 40, 40),
    "shattenkirk": Skater("Kevin Shattenkirk", 60, 40),
    "hoffman": Skater("Mike Hoffman", 40, 30),
    "pacioretty": Skater("Max Pacioretty", 40, 30),
    "barrie": Skater("Tyson Barrie", 40, 20),
    "giordano": Skater("Mark Giordano", 50, 60),
    "suter": Skater("Ryan Suter", 40, 50),
    "boqvist": Skater("Adam Boqvist", 60, 20),
    "zadina": Skater("Filip Zadina", 40, 30),
}