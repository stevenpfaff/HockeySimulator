class Skater:
    fwd_role_weights = {
        '1st Line': 1.2,
        '2nd Line': 1,
        '3rd Line': 0.8,
        '4th Line': 0.5,
        'Depth': 0.2,
        'bench': 0.1
    }

    def_role_weights = {
        'Number 1': 1.3,
        'Top Pair': 1.2,
        'Second Pair': 1,
        'Third Pair': 0.8,
        'Depth': 0.5,
        'bench': 0.1
    }

    def __init__(self, name, shooting=None, passing=None, offense=None, defense=None, penalties=None, powerplay=None, penaltykill=None, position="forward", role="bench", goals=0, assists=0, points=0, sog=0):
        self.name = name
        self.shooting = shooting or 40
        self.passing = passing or 40
        self.offense = offense or 40
        self.defense = defense or 40
        self.penalties = penalties or 40
        self.powerplay = powerplay
        self.penaltykill = penaltykill
        self.goals = goals
        self.assists = assists
        self.points = points
        self.position = position
        self.role = role
        self.sog = sog


    def get_role_weight(self):
        if self.position == "forward":
            return self.fwd_role_weights.get(self.role, 0.2)
        elif self.position == "defense":
            return self.def_role_weights.get(self.role, 0.2)
        else:
            return 0.2  # Default weight if role or position is not recognized

    def offensive_overall(self):
        if self.position == "forward":
            weights = {'shooting': 0.50, 'passing': 0.05, 'offense': 0.45, 'penalties': 0, 'powerplay': 0}
        elif self.position == "defense":
            weights = {'shooting': 0.05, 'passing': 0.05, 'offense': .7, 'penalties': 0, 'powerplay': 0}

        # Initialize score and weight sum
        offensive_score = 0
        weight_sum = 0

        # Calculate score only for non-None attributes
        offensive_score += self.shooting * weights['shooting']
        weight_sum += weights['shooting']

        offensive_score += self.passing * weights['passing']
        weight_sum += weights['passing']

        offensive_score += self.offense * weights['offense']
        weight_sum += weights['offense']

        offensive_score += self.penalties * weights['penalties']
        weight_sum += weights['penalties']

        # Include powerplay only if it is not None
        if self.powerplay is not None:
            offensive_score += self.powerplay * weights['powerplay']
            weight_sum += weights['powerplay']

        # Adjust score to account for only the included weights
        if weight_sum > 0:
            offensive_score = offensive_score / weight_sum * sum(weights.values())

        return max(offensive_score, 20)

    def defensive_overall(self):
        if self.position == "forward":
            weights = {'defense': 1, 'penalties': 0, 'penaltykill': 0}
        elif self.position == "defense":
            weights = {'defense': 1.15, 'penalties': 0, 'penaltykill': 0}

        # Initialize score and weight sum
        defensive_score = 0
        weight_sum = 0

        # Calculate score only for non-None attributes
        defensive_score += self.defense * weights['defense']
        weight_sum += weights['defense']

        defensive_score += self.penalties * weights['penalties']
        weight_sum += weights['penalties']

        # Include penaltykill only if it is not None
        if self.penaltykill is not None:
            defensive_score += self.penaltykill * weights['penaltykill']
            weight_sum += weights['penaltykill']

        # Adjust score to account for only the included weights
        if weight_sum > 0:
            defensive_score = defensive_score / weight_sum * sum(weights.values())

        return max(defensive_score, 20)

    def overall(self):
        return self.offensive_overall() + self.defensive_overall()

ducks_players = [
    Skater("Leo Carlsson", 50, 20, 45, 60, 65, powerplay=55, role="3rd Line"),
    Skater("Trevor Zegras", 60, 65, 60, 20, 30, powerplay=50, role="2nd Line"),
    Skater("Robby Fabbri", 60, 30, 40, 20, 40, powerplay=35, role="2nd Line"),
    Skater("Alex Killorn", 65, 50, 45, 60, 20, powerplay=30, penaltykill=60, role="2nd Line"),
    Skater("Troy Terry", 55, 60, 60, 40, 80, powerplay=60, role="1st Line"),
    Skater("Mason McTavish", 40, 60, 60, 30, 35, powerplay=45, role="3rd Line"),
    Skater("Frank Vatrano", 60, 30, 40, 20, 35, powerplay=30, role="2nd Line"),
    Skater("Cutter Gauthier", 40, 80, 60, 55, 50, 50,role="3rd Line"),
    Skater("Ryan Strome", 40, 55, 50, 20, 20, powerplay=20, role="2nd Line"),
    Skater("Isac Lundestrom", 30, 30, 30, 65, 60, penaltykill=30, role="4th Line"),
    Skater("Brett Leason", 50, 35, 30, 30, 35, penaltykill=40, role="4th Line"),
    Skater("Brock McGinn", 55, 30, 35, 55, 70, penaltykill=40, role="4th Line"),
    Skater("Jansen Harkins", 30, 40, 30, 60, 55, role="4th Line"),
    Skater("Sam Colangelo", role="Depth"),
    Skater("Ross Johnston", 30, 30, 20, 40, 20, role="4th Line"),
    Skater("Pavel Mintyukov", 45, 50, 60, 30, 65, powerplay=40,penaltykill=50, role="2nd Pair", position="defense"),
    Skater("Olen Zellweger", 60, 40, 40, 30, 70, powerplay=35, role="2nd Pair", position="defense"),
    Skater("Brian Dumoulin", 35, 40, 50, 60, 80,penaltykill=35, role="2nd Pair", position="defense"),
    Skater("Radko Gudas", 55, 60, 50, 60, 30, penaltykill=30, role="3rd Pair", position="defense"),
    Skater("Jacob Trouba", 20, 60, 55, 30, 45, penaltykill=35, role="2nd Pair", position="defense"),
    Skater("Jackson LaCombe", 60, 60, 50, 55, 50, penaltykill=60, role="2nd Pair", position="defense"),]
    # Skater("Tristan Luneau", 60, 20, 60, 20, 30, role="3rd Pair", position="defense"),]


bruins_players = [
    Skater("Brad Marchand", 50, 60, 70, 35, 70, powerplay=65, penaltykill=60, role="2nd Line"),
    Skater("David Pastrnak", 80, 80, 80, 40, 70, powerplay=70, role="1st Line"),
    Skater("Elias Lindholm", 30, 40, 30, 40, 60, powerplay=60, penaltykill=45, role="2nd Line"),
    Skater("Charlie Coyle", 60, 40, 50, 30, 60, powerplay=45, penaltykill=45, role="2nd Line"),
    Skater("Pavel Zacha", 55, 60, 40, 40, 50, powerplay=60, penaltykill=60, role="1st Line"),
    Skater("Trent Frederic", 60, 50, 50, 45, 30, 40, role="3rd Line"),
    Skater("Morgan Geekie", 60, 50, 45, 50, 40, powerplay=30, role="3rd Line"),
    Skater("John Beecher", 50, 45, 30, 60, 40, penaltykill=30, role="4th Line"),
    Skater("Mark Kastelic", 40, 35, 30, 60, 30, role="4th Line"),
    Skater("Oliver Wahlstrom", 40, 30, 35, 35, 40, role="4th Line"),
    Skater("Justin Brazeau", 60, 50, 60, 60, 60, powerplay=40, role="4th Line"),
    Skater("Cole Koepke", 50, 60, 40, 60, 40, role="4th Line"),
    Skater("Cole Koepke", 50, 60, 40, 60, 40, role="4th Line"),
    # Skater("Matthew Poitras", 50, 35, 55, 55, 80, role="4th Line"),
    # Skater("Max Jones", 20, 50, 50, 45, 60,role="Depth"),
    Skater("Charlie McAvoy", 60, 60, 70, 60, 50, powerplay=30, penaltykill=80, role="Number 1", position="defense"),
    Skater("Hampus Lindholm", 45, 50, 65, 60, 55, powerplay=20, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("Brandon Carlo", 40, 40, 30, 50, 40, penaltykill=70, role="3rd Pair", position="defense"),
    Skater("Nikita Zadorov", 70, 60, 40, 40, 20, penaltykill=55,role="2nd Pair", position="defense"),
    Skater("Andrew Peeke", 60, 70, 30, 60, 60, penaltykill=30, role="3rd Pair", position="defense"),
    Skater("Mason Lohrei", 60, 30, 30, 20, 60, 35,role="3rd Pair", position="defense"),
    Skater("Parker Wotherspoon", 30, 30, 60, 65, 60, role="3rd Pair", position="defense")
]

sabres_players = [
    Skater("Tage Thompson", 80, 60, 70, 55, 60, powerplay=60, role="2nd Line"),
    Skater("Alex Tuch", 65, 60, 60, 40, 35, powerplay=30, penaltykill=30, role="1st Line"),
    Skater("Dylan Cozens", 60, 65, 60, 30, 50, powerplay=40, role="2nd Line"),
    Skater("Jordan Greenway", 30, 45, 35, 60, 50, penaltykill=50, role="3rd Line"),
    Skater("JJ Peterka", 60, 60, 60, 40, 60, powerplay=20, role="2nd Line"),
    Skater("Zach Benson", 40, 60, 60, 60, 40, role="3rd Line"),
    Skater("Jack Quinn", 55, 40, 50, 30, 60, powerplay=40, role="3rd Line"),
    Skater("Jason Zucker", 55, 60, 70, 30, 50, powerplay=50, role="3rd Line"),
    Skater("Ryan McLeod", 50, 60, 60, 60, 50, penaltykill=80, role="3rd Line"),
    Skater("Sam Lafferty", 60, 30, 20, 50, 40, role="4th Line"),
    # Skater("Nicolas Aube-Kubel", 40, 45, 35, 80, 30, role="4th Line"),
    Skater("Beck Malenstyn", 30, 55, 30, 40, 60, penaltykill=35, role="4th Line"),
    Skater("Peyton Krebs", 40, 50, 30, 50, 40, role="4th Line"),
    Skater("Jiri Kulich", 60, 20, 60, 40, 65, 35,role="4th Line"),
    Skater("Rasmus Dahlin", 70, 70, 70, 65, 60, powerplay=60, role="Number 1", position="defense"),
    Skater("Owen Power", 30, 55, 50, 35, 60, powerplay=20, penaltykill=50,role="Top Pair", position="defense"),
    Skater("Bowen Byram", 80, 60, 30, 30, 35, 50, 40,role="Top Pair", position="defense"),
    Skater("Henri Jokijarju", 50, 40, 40, 40, 35, role="3rd Pair", position="defense"),
    Skater("Connor Clifton", 30, 60, 50, 40, 35, penaltykill=60, role="Depth", position="defense"),
    Skater("Mattias Samuelsson", 40, 30, 40, 55, 50, penaltykill=35, role="3rd Pair", position="defense"),
    Skater("Jacob Bryson", 40, 65, 30, 60, 50, role="Depth", position="defense"),
    Skater("Dennis Gilbert", 50, 30, 50, 55, 65, role="Depth", position="defense")
]

flames_players = [
    Skater("Mikael Backlund", 30, 40, 60, 70, 30, powerplay=50, penaltykill=30, role="1st Line"),
    Skater("Nazem Kadri", 60, 60, 60, 55, 80, powerplay=60,role="1st Line"),
    Skater("Yegor Sharangovich", 60, 40, 40, 40, 60, role="2nd Line"),
    Skater("Jonathan Huberdeau", 60, 60, 50, 40, 60, powerplay=60, role="1st Line"),
    Skater("Blake Coleman", 40, 50, 65, 60, 30, powerplay=40, penaltykill=70, role="2nd Line"),
    Skater("Connor Zary", 60, 40, 35, 65, 70, powerplay=35, role="3rd Line"),
    Skater("Martin Pospisil", 20, 40, 60, 60, 30,40, role="3rd Line"),
    Skater("Andrei Kuzmenko", 70, 50, 50, 50, 60, powerplay=35, role="3rd Line"),
    Skater("Matt Coronato", 40, 40, 40, 40, 45, powerplay=40, role="2nd Line"),
    Skater("Ryan Lomberg", 40, 30, 30, 50, 30, role="4th Line"),
    Skater("Kevin Rooney", 40, 20, 30, 50, 60, penaltykill=60, role="4th Line"),
    Skater("Justin Kirkland", 60, 60,40, 50, 40,role="4th Line"),
    # Skater("Anthony Mantha", 65, 60, 60, 80, 40, powerplay=20, role="3rd Line"),
    # Skater("Dryden Hunt", 30, 30, 20, 60, role="bench"),
    # Skater("Walker Dueher", 50, 65, 50, 30, role="bench"),
    Skater("MacKenzie Weegar", 70, 50, 60, 65, 50, powerplay=30, penaltykill=80, role="Top Pair", position="defense"),
    Skater("Rasmus Andersson", 65, 55, 60, 30, 60, powerplay=60, penaltykill=35, role="Number 1", position="defense"),
    Skater("Kevin Bahl", 40, 60, 30, 60, 30, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Danill Miromanov", 60, 60, 45, 60, 55, role="2nd Pair", position="defense"),
    # Skater("Tyson Barrie", 60, 60, 45, 20, 50, powerplay=30,role="3rd Pair", position="defense"),
    Skater("Jake Bean", 60, 40, 50, 40, 35, role="Depth", position="defense"),
    Skater("Brayden Pachal", 50, 30, 30, 50, 30, penaltykill=60, role="Depth", position="defense"),
    Skater("Joel Hanley", 30, 30, 30, 70, 30, role="Depth", position="defense")
]

hurricanes_players = [
    Skater("Sebastian Aho", 60, 70, 70, 50, 50, powerplay=60, penaltykill=80, role="1st Line"),
    Skater("Andrei Svechnikov", 40, 60, 70, 30, 30, powerplay=65, role="2nd Line"),
    Skater("Seth Jarvis", 40, 60, 55, 80,  70, powerplay=60, penaltykill=50, role="1st Line"),
    Skater("Jesperi Kotkaniemi", 40, 45, 45, 40, 20, powerplay=30, role="4th Line"),
    Skater("Martin Necas", 60, 70, 60, 30, 70, powerplay=40,  role="2nd Line"),
    # Skater("Jesper Fast", 30, 40, 60, 70, 60, penaltykill=80,role="4th Line"),
    Skater("Jack Drury", 20, 40, 35, 65, 40, 40, 50,role="4th Line"),
    Skater("Jordan Staal", 40, 50, 55, 80, 30, penaltykill=30, role="3rd Line"),
    Skater("Jack Roslovic", 50, 50, 40, 35, 60, 30, role="3rd Line"),
    # Skater("Tyson Jost", 30, 40, 30, 40, 60, role="Depth"),
    Skater("William Carrier", 40, 30, 70, 70, 50, role="4th Line"),
    Skater("Jordan Martinook", 30, 55, 60, 70, 30, penaltykill=65, role="3rd Line"),
    Skater("Eric Robinson", 35, 65, 60, 30, 50, role="4th Line"),
    # Skater("Brendan Lemieux", 40, 50, 35, 30, 20, role="bench"),
    # Skater("Ryan Suzuki", 30, 40, 35, 35, role="bench"),
    Skater("Jaccob Slavin", 45, 60, 65, 65, 80, penaltykill=80, role="2nd Pair", position="defense"),
    Skater("Dimitry Orlov", 40, 50, 60, 60, 70, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Brent Burns", 70, 60, 65, 45, 50, powerplay=60, penaltykill=65, role= "2nd Pair", position="defense"),
    Skater("Sean Walker", 55, 45, 65, 50, 30,role="3rd Pair", position="defense"),
    Skater("Shayne Gostisbehere", 70, 55, 60, 45, 80, powerplay=65, role="3rd Pair", position="defense"),
    Skater("Jalen Chatfield", 65, 30, 60, 70, 30, penaltykill=60, role="2nd Pair", position="defense")
]

blackhawks_players = [
    Skater("Connor Bedard", 60, 65, 40, 20, 60, powerplay=60, role="1st Line"),
    Skater("Nick Foligno", 60, 40, 50, 60, 40, penaltykill=40, role="2nd Line"),
    Skater("Teuvo Teravainen", 60, 60, 35, 60, 40, powerplay=60, penaltykill=80, role="3rd Line"),
    Skater("Tyler Bertuzzi", 45, 50, 60, 40, 60, powerplay=50, role="3rd Line"),
    Skater("Philip Kurashev", 45, 35, 30, 30, 60, penaltykill=60, role="3rd Line"),
    Skater("Taylor Hall", 40, 60, 60, 40, 45, powerplay=40, role="3rd Line"),
    Skater("Jason Dickinson", 60, 30, 20,70, 50, penaltykill=30, role="3rd Line"),
    Skater("Ilya Mikheyev", 50, 60, 40, 70, 65, penaltykill=70,role="3rd Line"),
    Skater("Joey Anderson", 50, 55, 30, 60, 60, penaltykill=60, role="4th Line"),
    Skater("Craig Smith", 50, 45, 60, 40, 30, 40, role="4th Line"),
    Skater("Ryan Donato", 60, 50, 50, 40, 50, 30, role="3rd Line"),
    Skater("Lukas Reichel", 40, 55, 30, 35, 40, powerplay=20, role="4th Line"),
    Skater("Frank Nazar", 20, 35, 40, 40, 60, 30, role="4th Line"),
    # Skater("Andreas Athanasiou", 45, 40, 40, 20, 80,role="bench"),
    Skater("Patrick Maroon", 30, 60, 40, 35, 20, 40,role="4th Line"),
    Skater("Seth Jones", 60, 40, 60, 30, 50, powerplay=60, penaltykill=70, role="Number 1", position="defense"),
    Skater("Alex Vlassic", 30, 30, 45, 65, 65, 50, 65, role="Number 1", position="defense"),
    Skater("Connor Murphy", 60, 35, 55, 70, 55, penaltykill=55, role="2nd Pair", position="defense"),
    Skater("Alec Martinez", 50, 30, 40, 40, 55, 40, 55, role="2nd Pair", position="defense"),
    Skater("Wyatt Kaiser", 30, 20, 50, 60, 50, penaltykill= 40,role="3rd Pair", position="defense"),
    Skater("TJ Brodie", 30, 30, 45,60, 60, role="3rd Pair", position="defense"),
    Skater("Nolan Allan", 50, 60, 30, 30, 20, role="Depth", position="defense"),
    Skater("Kevin Korchinski", 60, 20, 50, 20, 50, powerplay=35, role="bench", position="defense"),
]

avalanche_players = [
    Skater("Nathan MacKinnon", 80, 80, 80, 40, 80, powerplay=80,role="1st Line"),
    Skater("Mikko Rantanen", 80, 65, 60,20, 50, powerplay=80, role="1st Line"),
    Skater("Jonathan Drouin", 45, 60, 60, 50, 50, powerplay=45,role="1st Line"),
    Skater("Valeri Nichushkin", 60, 65, 60, 30, 60, 60, 60,role="1st Line"),
    Skater("Casey Mittelstadt", 60, 65, 40, 40, 40, powerplay=50, role="2nd Line"),
    Skater("Artturi Lehkonen", 60, 40, 65, 45, 30, powerplay=60, penaltykill=60, role="1st Line"),
    Skater("Logan O'Connor", 40, 35, 60, 80, 50, penaltykill=70, role="3rd Line"),
    Skater("Miles Wood", 20, 65, 55, 20, 40, penaltykill=45,role="4th Line"),
    Skater("Ross Colton", 45, 45, 60, 60, 60, powerplay=20, role="2nd Line"),
    Skater("Parker Kelly", 30, 30, 20, 60, 60, penaltykill=60, role="4th Line"),
    # Skater("Chris Wagner", 35, 30, 40, 40, 40,role="Depth"),
    Skater("Joel Kiviranta", 40, 30, 40, 65, 40, penaltykill=60, role="4th Line"),
    Skater("Ivan Ivan", 50, 20, 35, 70, 30, 30, role="4th Line"),
    Skater("Juuso Parssinen", 40, 30, 20, 30, 60,role="4th Line"),
    # Skater("Givani Smith", 30, 50, 40, 35, 20, role="Depth"),
    # Skater("Callum Ritchie",  role="bench"),
    # Skater("Matthew Stienburg", offense=55, defense=55, role="Depth"),
    # Skater("Gabriel Landeskog", 60, 60, 60, 60, role="1st Line"),
    Skater("Cale Makar", 80, 80, 60, 70, 80, powerplay=60, penaltykill=30, role="Number 1", position="defense"),
    Skater("Devon Toews", 60, 45, 50, 60, 70, powerplay=30, penaltykill=40, role="Number 1", position="defense"),
    Skater("Samuel Girard", 50, 65, 65, 40, 70, penaltykill=50, role="2nd Pair", position="defense"),
    Skater("Josh Manson", 60, 70, 45, 40, 30, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Calvin deHaan", 40, 60, 60, 60, 40, role="3rd Pair", position="defense"),
    Skater("Sam Malinski", 50, 35, 60, 50, 65, role="3rd Pair", position="defense"),
    Skater("Oliver Kylington", 60, 30, 60, 30, 50, role="Depth", position="defense"),
    Skater("John Ludvig", 50, 30, 45, 40, 35,role="Depth", position="defense")
]

bluejackets_players = [
    # Skater("Johnny Gaudreau", 40, 80, 80, 20), RIP Johnny Gaudreau </3
    Skater("Yegor Chinakhov", 65, 50, 50, 60, 60, 30, role="2nd Line"),
    Skater("Kirill Marchenko", 70, 60, 50, 60, 60, powerplay=60,role="1st Line"),
    Skater("Sean Monahan", 55, 80, 70, 40, 35, 60, 45, role="1st Line"),
    Skater("Adam Fantilli", 60, 60, 20, 30, 70, powerplay=30, role="2nd Line"),
    Skater("Cole Sillinger", 20, 60, 30, 20, 30, powerplay=40, penaltykill=30,role="2nd Line"),
    Skater("Kent Johnson", 60, 50, 30, 55, 45, powerplay=60, role="2nd Line"),
    Skater("Dmitri Voronkov", 60, 60, 65, 30, 20, powerplay=60, role="2nd Line"),
    Skater("Mikael Pyyhtia", 45, 40, 20, 30, 50, penaltykill=35, role="4th Line"),
    Skater("Sean Kuraly", 45, 50, 35, 40, 30, role="4th Line"),
    Skater("James van Riemsdyk", 20, 70, 65, 60, 30,role="4th Line"),
    Skater("Kevin Labanc", 40, 30, 40, 60, 20,role="4th Line"),
    Skater("Mathieu Olivier", 30, 30, 50, 55, 20, role="4th Line"),
    Skater("Zach Aston-Reese", 40, 30, 40, 50, 40,role="4th Line"),
    Skater("Justin Danforth", 30, 40, 50, 60, 30, penaltykill=30, role="3rd Line"),
    # Skater("Gavin Brindley", 30, 30, 30, 30, role="bench"),
    # Skater("Boone Jenner", 60, 30, 50, 50, 50, powerplay=60, penaltykill=30,role="bench"),
    Skater("Zach Werenski", 65, 80, 70, 30, 50, powerplay=60, penaltykill=50,role="Number 1", position="defense"),
    Skater("Ivan Provorov", 50, 40, 40, 30, 65, powerplay=30, penaltykill=30,role="Top Pair", position="defense"),
    Skater("Damon Severson", 60, 60, 70, 60, 40, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Dante Fabbro", 40, 40, 60, 50, 30, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("Jordan Harris", 60, 50, 50, 40, 60,role="3rd Pair", position="defense"),
    # Skater("Erik Gudbranson", 50, 35, 20, 30, 45, penaltykill=30, role="bench", position="defense"),
    Skater("Jack Johnson", 40, 30, 30, 30, 60,role="Depth", position="defense"),
    Skater("Jake Christansen", 30, 60, 50, 30, 60,role="Depth", position="defense")
]

stars_players = [
    Skater("Jason Robertson", 70, 65, 60, 80, 60, powerplay=60, role="2nd Line"),
    Skater("Roope Hintz", 70, 60, 65, 50, 60, powerplay=70, penaltykill=60,role="2nd Line"),
    Skater("Wyatt Johnston", 60, 70, 60, 60, 40, 50, 50, role="1st Line"),
    Skater("Jamie Benn", 65, 60, 65, 30, 40, powerplay=60,role="3rd Line"),
    Skater("Logan Stankoven", 20, 60, 60, 60, 80, powerplay=60,role="3rd Line"),
    Skater("Matt Duchene", 60, 60, 60, 30,50, powerplay=60, role="2nd Line"),
    # Skater("Tyler Seguin", 65, 50, 70, 30, 40, powerplay=50, penaltykill=60,role="2nd Line"),
    Skater("Mason Marchment", 50, 70, 60,60, 35, powerplay=60,role="3rd Line"),
    Skater("Evgeni Dadonov", 45, 30,35, 50, 50, 50,role="4th Line"),
    Skater("Sam Steel", 40, 60, 45, 50, 50, penaltykill=80,role="3rd Line"),
    Skater("Colin Blackwell", 30, 40, 30, 50, 70, penaltykill=50,role="4th Line"),
    Skater("Mavrik Bourque", 30, 30, 40, 45, 60,role="4th Line"),
    Skater("Oskar Back", 20, 60, 30, 60, 60, penaltykill=50,role="4th Line"),
    Skater("Miro Heiskanen", 40, 60, 65,60, 80, powerplay=80,role="Number 1", position="defense"),
    Skater("Esa Lindell", 50, 50, 60, 70, 65, penaltykill=65,role="2nd Pair", position="defense"),
    Skater("Thomas Harley", 80, 60, 70, 45, 60, powerplay=60, penaltykill=65,role="Top Pair", position="defense"),
    Skater("Ilya Lyubushkin", 30, 45, 40, 50, 35, penaltykill=20,role="3rd Pair", position="defense"),
    Skater("Matt Dumba", 30, 35, 30, 40, 30, role="Depth", position="defense"),
    Skater("Nils Lundkvist", 40, 70, 60, 30, 30,role="Depth", position="defense"),
    Skater("Brendan Smith", 30, 40, 35, 40, 30, penaltykill=70,role="Depth", position="defense")
]

redwings_players = [
    Skater("Dylan Larkin", 70, 70, 65, 60, 60, powerplay=65, penaltykill=40,role="1st Line"),
    Skater("Lucas Raymond", 65, 60, 40, 60, 80, 60, 65, role="1st Line"),
    Skater("Alex DeBrincat", 60, 50, 60, 35, 70, powerplay=65,role="2nd Line"),
    Skater("Patrick Kane", 70, 55, 30, 30, 50,powerplay=65,role="2nd Line"),
    Skater("JT Compher", 50, 60, 35, 60, 55, powerplay=60, penaltykill=20,role="2nd Line"),
    Skater("Vladimir Tarasenko", 60, 65, 60, 20, 60, 50,role="3rd Line"),
    Skater("Andrew Copp", 40, 60, 40, 45, 45, penaltykill=30,role="3rd Line"),
    Skater("Michael Rasmussen", 35, 50, 35, 60, 50, 40,role="4th Line"),
    Skater("Jonatan Berggren", 60, 40, 35, 50, 60,role="4th Line"),
    Skater("Joe Veleno", 55, 30, 30,50, 50,role="4th Line"),
    Skater("Christian Fischer", 40, 40, 40, 60, 55,role="4th Line"),
    Skater("Tyler Motte", 30, 30, 30, 60, 80, penaltykill=70,role="4th Line"),
    Skater("Marco Kasper", 30, 20, 45, 60, 30, 30,role="4th Line"),
    # Skater("Austin Watson", 30, 20, 20, 50, 20, role="bench"),
    Skater("Moritz Seider", 60, 60, 30, 55, 65, powerplay=50, penaltykill=20,role="Number 1", position="defense"),
    Skater("Simon Edvinsson", 50, 50, 60, 60, 50, penaltykill=45,role="2nd Pair", position="defense"),
    Skater("Ben Chiarot", 40, 60, 30, 30, 30, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Erik Gustafsson", 60, 60, 55, 60, 50, powerplay=45,role="3rd Pair", position="defense"),
    Skater("Jeff Petry", 40, 60, 60, 60, 40, penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Justin Holl", 35, 40, 40, 50, 30, penaltykill=50,role="Depth", position="defense"),
    # Skater("William Lagesson", 30, 20, 40, 55, 35, penaltykill=50, role="Depth", position="defense"),
    Skater("Albert Johansson", 60,20,30,50,65,role="Depth", position="defense"),
]

oilers_players = [
    Skater("Connor McDavid", 80, 80, 80, 60, 80, powerplay=80,role="1st Line"),
    Skater("Leon Draisaitl", 80, 80, 80,35, 60, powerplay=80, role="1st Line"),
    Skater("Ryan Nugent-Hopkins", 60, 60, 50, 55, 30, powerplay=70, penaltykill=30,role="1st Line"),
    Skater("Zach Hyman", 60, 50, 80, 50, 50, powerplay=70, role="1st Line"),
    Skater("Jeff Skinner", 60, 60, 60, 20, 60,role="4th Line"),
    Skater("Viktor Arvidsson", 50, 50, 60, 50, 50, role="3rd Line"),
    Skater("Adam Henrique", 60, 40, 50, 35, 35, penaltykill=35, role="3rd Line"),
    Skater("Connor Brown", 20, 45, 40, 60, 40, penaltykill=60,role="4th Line"),
    Skater("Derek Ryan", 50, 30, 40, 65, 45, role="4th Line"),
    Skater("Mattias Janmark", 30, 50, 20, 60, 40, penaltykill=60,role="4th Line"),
    Skater("Corey Perry", 50, 30, 40, 55, 55, 40, role="4th Line"),
    Skater("Vasaily Podkolzin", 30, 35, 50, 70, 40, role="4th Line"),
    Skater("Kasperi Kapanen", 50, 50, 35, 40, 60, role="4th Line"),
    # Skater("Evander Kane", 45, 30, 30, 20, 20, powerplay=45,role="bench"),
    Skater("Evan Bouchard", 65, 50, 70, 60, 65, powerplay=65,role="Top Pair", position="defense"),
    Skater("Mattias Ekholm", 60, 80, 70, 70, 60, penaltykill=40,role="Top Pair", position="defense"),
    Skater("Brett Kulak", 50, 30, 60, 60, 40, penaltykill=70,role="2nd Pair", position="defense"),
    Skater("Darnell Nurse", 60, 65, 60, 50,40, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Troy Stecher", 40, 40, 40, 50, 30, role="Depth", position="defense"),
    Skater("Ty Emberson", 30, 50, 30, 60, 60, penaltykill=60, role="Depth", position="defense"),
    # Skater("Josh Brown", 40, 30, 40, 30, 35, penaltykill=35,role="bench", position="defense")
]

panthers_players = [
    Skater("Matthew Tkachuk", 30, 80, 80, 35, 70, 80,role="2nd Line"),
    Skater("Aleksander Barkov", 55, 80, 65, 80, 60, 80, 60,role="1st Line"),
    Skater("Sam Reinhart", 80, 60, 50, 80, 50, 70, 50,role="1st Line"),
    Skater("Sam Bennett", 40, 60, 60, 50, 20, 55,role="2nd Line"),
    Skater("Carter Verhaeghe", 70, 60, 70, 35, 30, 60,role="2nd Line"),
    Skater("Evan Rodrigues", 35, 40, 60, 60, 55, 50,role="3rd Line"),
    Skater("Eetu Luostarainen", 40, 35, 40, 70, 60, penaltykill=60,role="3rd Line"),
    Skater("Jonah Gadjovich", 20, 30, 45, 40, 40, role="Depth"),
    Skater("Anton Lundell", 35, 60, 40, 50, 40, 45, 70,role="2nd Line"),
    Skater("Jesper Boqvist", 60, 50, 40, 60, 60, penaltykill=60, role="4th Line"),
    Skater("Mackie Samoskevich", 55, 20, 60, 55, 60, role="4th Line"),
    Skater("AJ Greer", 35, 45, 40, 60, 30,role="4th Line"),
    Skater("Tomas Nosek", 30, 50, 40, 50, 40,role="4th Line"),
    Skater("Aaron Ekblad", 30, 50, 60, 35, 30, 50,65,role="Number 1", position="defense"),
    Skater("Gustav Forsling", 70, 70, 60, 80, 55, penaltykill=30,role="Top Pair", position="defense"),
    Skater("Dimitry Kulikov", 40,60, 45, 40, 50, penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Niko Mikkola", 40, 40, 40, 60, 30, penaltykill=70,role="2nd Pair", position="defense"),
    Skater("Nate Schmidt", 50, 35, 45, 70, 65,role="3rd Pair", position="defense"),
    Skater("Adam Boqvist", 55, 40, 60, 20, 60, 45,role="Depth", position="defense"),
    Skater("Uvis Balinskis", 30, 30, 30, 40, 60, 30,role="Depth", position="defense"),
    # Skater("Tobias Bjornfoot", 30, 30, 30, 30, role="bench", position="defense")
]

kings_players = [
    Skater("Anze Kopitar", 70, 60, 50, 60, 60, 50, 40,role="1st Line"),
    Skater("Adrian Kempe", 80, 55, 60, 50, 40,55,65,role="1st Line"),
    Skater("Kevin Fiala", 60, 50, 70, 60, 30, 50,role="2nd Line"),
    Skater("Quinton Byfield", 30, 60, 60, 70, 35, 55, 65,role="2nd Line"),
    Skater("Phillip Danault", 50, 60, 60, 60, 60,45,60,role="2nd Line"),
    Skater("Trevor Moore", 45, 60, 40, 60, 65, 35, 55,role="2nd Line"),
    Skater("Alex Lafferiere", 50, 60, 50, 40, 40, 30,role="2nd Line"),
    Skater("Warren Foegle", 50, 65, 70, 65, 60, penaltykill=70,role="3rd Line"),
    Skater("Tanner Jeannot", 30, 30, 30, 60, 30,role="4th Line"),
    Skater("Trevor Lewis", 35, 30, 20, 65, 30,role="4th Line"),
    Skater("Alex Turcotte", 40, 40, 55, 70, 40, 35,role="4th Line"),
    Skater("Mikey Anderson", 40, 30, 20, 80, 60, penaltykill=35,role="Top Pair", position="defense"),
    Skater("Vladislav Gavrikov", 55, 40, 60, 65, 60, penaltykill=60,role="Number 1", position="defense"),
    Skater("Jordan Spence", 30, 70, 60, 60, 40, 40,role="3rd Pair", position="defense"),
    Skater("Joel Edmundson", 50, 35, 35, 30, 50, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Kyle Burroughs", 35, 30, 45, 55, 35, role="Depth", position="defense"),
    Skater("Brandt Clarke", 35, 80, 70, 30, 40, 55,role="3rd Pair", position="defense"),
    Skater("Drew Doughty", 65, 50, 55, 80, 55, 45, 50,role="Depth", position="defense"),
    Skater("Andreas Englund", 35, 30, 30, 60, 60,role="Depth", position="defense"),
    Skater("Jacob Moverare", 60, 20, 60, 60, 35, role="Depth", position="defense"),
    Skater("Caleb Jones", 50, 45, 60, 60, 40, role="Depth", position="defense"),
]

wild_players = [
    Skater("Kirill Kaprizov", 80, 80, 80, 60, 80, 80,role="1st Line"),
    Skater("Matthew Boldy", 60, 50, 70, 60, 30, 80,role="1st Line"),
    Skater("Mats Zuccarello", 60, 80, 60, 40, 65, 70,role="1st Line"),
    Skater("Marco Rossi", 55, 55, 60, 45, 65, 30,role="2nd Line"),
    Skater("Joel Eriksson-Ek", 30, 50, 60, 70, 60, 80, 20,role="1st Line"),
    Skater("Marcus Johansson", 50, 40, 40, 60, 60, 50,role="3rd Line"),
    Skater("Ryan Hartman", 40, 50, 55, 30, 50, 40,role="3rd Line"),
    Skater("Marcus Foligno", 35, 40, 60, 80, 40, penaltykill=50,role="4th Line"),
    Skater("Frederick Gaudreau", 50, 40, 30, 40, 45, 50, 40,role="3rd Line"),
    Skater("Marat Kushnutdinov", 30, 20, 20, 45, 30, penaltykill=60,role="4th Line"),
    Skater("Yakov Trenin", 30, 30, 50, 65, 30, penaltykill=80,role="4th Line"),
    Skater("Jakub Lauko", 35, 30, 30, 60, 60, penaltykill=40,role="4th Line"),
    Skater("Devin Shore", 30, 60, 45, 40, 45,role="Depth"),
    # Skater("Liam Ohgren", offense=40, defense=55,role="Depth"),
    Skater("Brock Faber", 60, 50, 45, 40, 70, 50, 30,role="Number 1", position="defense"),
    Skater("Jonas Brodin", 60, 40, 35, 80, 60, penaltykill=40,role="Top Pair", position="defense"),
    Skater("Jared Spurgeon", 60, 50, 65, 65, 70, 60, role="2nd Pair", position="defense"),
    Skater("Jake Middleton", 60, 60, 30, 40, 60, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Zach Bogosian", 55, 55, 50,40, 30, penaltykill=40,role="3rd Pair", position="defense"),
    Skater("Declan Chisholm", 60, 60, 60, 60, 40,role="3rd Pair", position="defense"),
    Skater("Travis Dermott", 50, 20, 40, 35, 40, role="Depth", position="defense"),
    # Skater("David Jiricek", 35, 65, 50, 45, 30, role="Depth", position="defense"),
    Skater("Jon Merrill", 60, 50, 20, 60, 30,role="Depth", position="defense")
]

canadiens_players = [
    Skater("Nick Suzuki", 70, 60, 60, 50, 65, 60,role="1st Line"),
    Skater("Cole Caufield", 70, 60, 60, 20, 70, 35,role="2nd Line"),
    Skater("Juraj Slafkovsky", 40, 60, 60, 30, 30, 40,role="2nd Line"),
    Skater("Kriby Dach", 40, 20, 50, 30, 45, 50,role="3rd Line"),
    Skater("Brendan Gallagher", 40, 45, 70, 50, 40,20,role="4th Line"),
    Skater("Joel Armia", 60, 50, 50, 60, 30, 40, 65,role="3rd Line"),
    Skater("Alex Newhook", 50, 35, 60, 30,  40, 40,role="3rd Line"),
    Skater("Josh Anderson", 30, 40, 60, 20, 30, penaltykill=60,role="3rd Line"),
    Skater("Patrik Laine", 80, 30, 40, 30, 70, 60,role="3rd Line"),
    Skater("Jake Evans", 30, 65, 50, 60, 60, penaltykill=20, role="3rd Line"),
    Skater("Christian Dvorak", 30, 50, 35, 40, 50, penaltykill=30, role="3rd Line"),
    Skater("Joshua Roy", 50, 60, 60, 60, 55,role="Depth"),
    Skater("Emil Heineman", 70, 30, 30, 80, 30, 40, role="4th Line"),
    # Skater("Michael Pezzetta", 45, 55, 30, 45, 20,role="bench"),
    Skater("Lane Hutson", 40, 80, 80, 20, 50, 70,role="Top Pair", position="defense"),
    Skater("Mike Matheson", 50, 70, 50,40, 60, 30,30,role="Number 1", position="defense"),
    Skater("Kaiden Guhle", 60, 60, 30, 60, 40, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Alexandre Carrier", 35, 45, 40, 50, 55, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("David Savard", 60, 50, 35, 30, 60, penaltykill=20, role="3rd Pair", position="defense"),
    Skater("Jayden Struble", 60, 30, 40, 30, 20, role="Depth", position="defense"),
    Skater("Arber Xhekaj", 60, 60, 50, 35, 20,role="Depth", position="defense")
]

predators_players = [
    Skater("Filip Forsberg", 65, 50, 70, 50, 70, 60, role="2nd Line"),
    Skater("Ryan O'Reilly", 60, 40, 65, 70, 50, 60,role="1st Line"),
    Skater("Steven Stamkos", 65, 60, 35, 30, 30, 60,role="2nd Line"),
    Skater("Jonathan Marchessault", 65, 50, 55, 40, 30, 65,role="2nd Line"),
    Skater("Gustav Nyquist", 50, 60, 55, 30, 60, 30, 50,role="2nd Line"),
    Skater("Tommy Novak", 65, 40, 65, 30, 65, 60,role="4th Line"),
    Skater("Colton Sissons", 30, 40, 50, 50, 40,  penaltykill=20,role="4th Line"),
    Skater("Luke Evangelista", 40, 60, 50, 50, 65, 35,role="4th Line"),
    Skater("Cole Smith", 20, 30, 30, 60, 50, penaltykill=60,role="4th Line"),
    Skater("Michael McCarron", 35, 30, 40, 35, 30, penaltykill=60,role="4th Line"),
    Skater("Mark Jankowski", 40, 40, 60, 80, 30, penaltykill=60,role="4th Line"),
    Skater("Zachary L'Heureux", 30, 30, 55, 45, 40, role="4th Line"),
    Skater("Roman Josi", 80, 80, 80, 40, 60, 70, 60,role="Number 1", position="defense"),
    Skater("Brady Skjei", 80, 45, 40, 30, 50, 40, 55, role="2nd Pair", position="defense"),
    Skater("Jeremy Lauzon", 40, 30, 40, 60, 30, penaltykill=30, role="3rd Pair", position="defense"),
    Skater("Justin Barron", 70, 30, 60, 30, 40, role="Depth", position="defense"),
    Skater("Luke Schenn", 35, 30, 40, 60, 30, penaltykill=50,role="Depth", position="defense"),
    Skater("Nick Blankenburg", 60, 20, 60, 55, 50, penaltykill=60, role="3rd Pair", position="defense"),
    Skater("Adam Wilsby", 40, 20, 50, 70, 80, penaltykill=60, role="3rd Pair", position="defense"),
    Skater("Marc Del Gaizo", 20, 35, 40, 40, 20,role="Depth", position="defense"),
    Skater("Spencer Stastney", 60, 35, 65, 50, 60, penaltykill=45,role="bench", position="defense")
]

devils_players = [
    Skater("Jack Hughes", 60, 70, 80, 60, 80, 70,role="1st Line"),
    Skater("Nico Hischier", 60, 65, 80, 40, 80, 65, 30,role="1st Line"),
    Skater("Jesper Bratt", 60, 80, 80, 40, 60, 65, 60,role="2nd Line"),
    Skater("Timo Meier", 65, 40, 65, 35, 50, 50,role="2nd Line"),
    Skater("Dawson Mercer", 60, 50, 60, 60, 40, 30, 60,role="2nd Line"),
    Skater("Erik Haula", 30, 40, 50, 65, 20,  penaltykill=60,role="4th Line"),
    Skater("Ondrej Palat", 50, 50, 60, 40, 60, role="4th Line"),
    Skater("Tomas Tatar", 30, 30, 50, 60, 40,role="4th Line"),
    Skater("Stefan Noesen", 30, 60, 60, 60, 35, 65,role="3rd Line"),
    Skater("Curtis Lazar", 30, 35, 40, 60, 50, penaltykill=65,role="Depth"),
    Skater("Nathan Bastian", 20, 40, 40, 60, 30,role="4th Line"),
    Skater("Paul Cotter", 50, 40, 40, 50, 30,role="4th Line"),
    Skater("Dougie Hamilton", 80, 60, 80, 35, 20, 60,role="2nd Pair", position="defense"),
    Skater("Jonas Siegenthaler", 40, 30, 20, 70, 55, penaltykill=55, role="2nd Pair", position="defense"),
    Skater("Brett Pesce", 30, 40, 60, 50, 70, penaltykill= 60,role="2nd Pair", position="defense"),
    Skater("Brenden Dillon", 60, 30, 50, 60, 30, penaltykill=30,role="3rd Pair", position="defense"),
    Skater("Johnathan Kovacevic", 50, 60, 50, 65, 45, penaltykill=70,role="2nd Pair", position="defense"),
    Skater("Simon Nemec", 30, 70, 70, 30, 55, 50,role="Depth", position="defense"),
    Skater("Luke Hughes", 40, 65, 60, 45, 80, 40, role="2nd Pair", position="defense"),
    Skater("Kurtis MacDermid", 40, 60, 40, 40, 20, role="Depth", position="defense"),
]

islanders_players = [
    Skater("Mat Barzal", 60, 80, 80, 50, 60, 60,role="1st Line"),
    Skater("Bo Horvat", 65, 60, 65, 40, 60, 60,role="1st Line"),
    Skater("Brock Nelson", 65, 60, 50, 30, 65, 60,role="1st Line"),
    Skater("Kyle Palmieri", 60, 45, 60, 30, 60, 60,role="2nd Line"),
    Skater("Anthony Duclair", 60, 65, 60, 35, 60, 30,role="3rd Line"),
    Skater("Maxim Tsyplakov", 30, 40, 65, 60, 20, 20, role="3rd Line"),
    Skater("Anders Lee", 40, 35, 70, 70, 35, 50,role="2nd Line"),
    Skater("JG Pageau", 35, 50, 50, 50, 60, 30, 40,role="2nd Line"),
    Skater("Simon Holmstrom", 60, 60, 20, 60, 60, 35, 50,role="2nd Line"),
    Skater("Casey Cizikas", 30, 30, 20, 60, 60, role="4th Line"),
    Skater("Kyle MacLean", 50, 35, 30, 60, 50, role="4th Line"),
    Skater("Matt Martin", 30, 40, 30, 60, 40, role="Depth"),
    Skater("Hudson Fasching", 50, 55, 50, 60, 55, role="Depth"),
    Skater("Julien Gauthier", 50, 30, 35, 30, 60,role="bench"),
    Skater("Pierre Engvall", 50, 40, 60, 60, 20, role="4th Line"),
    Skater("Noah Dobson", 65, 65, 60, 60, 60, 45, role="Number 1", position="defense"),
    Skater("Ryan Pulock", 60, 50, 30, 55, 60, penaltykill=60,role="Top Pair", position="defense"),
    Skater("Adam Pelech", 30, 50, 30, 80, 60, penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Alexander Romanov", 50, 60, 55, 30, 40, penaltykill=50,role="2nd Pair", position="defense"),
    Skater("Scott Mayfield", 50, 40, 40, 50, 50, penaltykill=30,role="3rd Pair", position="defense"),
    Skater("Isaiah George", 60, 20, 50, 50, 45, role="3rd Pair", position="defense"),
    Skater("Mike Reilly", 35, 60, 60, 60, 30, 50,role="Depth", position="defense"),
    Skater("Dennis Cholowski", 80, 60, 50, 40, 40, 35, role="Depth", position="defense"),
    Skater("Samuel Bolduc", 55, 20, 40, 35, 50,role="Depth", position="defense")
]

rangers_players = [
    Skater("Artemi Panarin", 80, 60, 70, 40, 60, 70,role="1st Line"),
    Skater("Mika Zibanejad", 60, 60, 40, 30, 65, 60, 35,role="2nd Line"),
    Skater("Vincent Trocheck", 30, 70, 65, 40, 40, 65, 40,role="1st Line"),
    Skater("Chris Kreider", 60, 30, 60, 40, 30,65, 45,role="2nd Line"),
    Skater("Alexis Lafreniere", 60, 60, 60, 30, 55, 50, role="2nd Line"),
    Skater("Reilly Smith", 45, 60, 60, 50, 40, penaltykill=60,role="3rd Line"),
    Skater("Filip Chytil", 60, 65, 60, 35, 50, 40,role="4th Line"),
    Skater("Will Cuylle", 60, 50, 50, 40, 40, penaltykill=50,role="3rd Line"),
    Skater("Jimmy Vesey", 30, 30, 45, 70, 60, role="4th Line"),
    Skater("Sam Carrick", 40, 30, 40, 50, 30, penaltykill=20, role="4th Line"),
    Skater("Adam Edstrom", 20, 20, 40, 50, 60, role="4th Line"),
    Skater("Jonny Brodzinski", 45, 35, 30, 60, 50,role="4th Line"),
    Skater("Matt Rempe", role="bench"),
    Skater("Arthur Kaliyev", 35, 50, 60, 45, 35, 40, role="4th Line"),
    Skater("Adam Fox", 65, 80, 80, 65, 60, 80,65,role="Top Pair", position="defense"),
    Skater("K'Andre Miller", 60, 50, 60, 50, 40, penaltykill=80,role="2nd Pair", position="defense"),
    Skater("Ryan Lindgren", 30, 30, 20, 35, 50, penaltykill=50, role="2nd Pair", position="defense"),
    Skater("Braden Schneider", 60, 40, 50, 30, 60, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("William Borgen", 45, 55, 50, 40, 60, penaltykill=45, role="Depth", position="defense"),
    Skater("Zachary Jones", 50, 50, 40, 40, 40, 40,role="3rd Pair", position="defense"),
    Skater("Victor Mancini", 60, 45, 40, 20, 45, role="Depth", position="defense"),
    Skater("Urho Vaakanainen", 20, 50, 30, 60, 60, penaltykill=30, role="3rd Pair", position="defense"),
    Skater("Chad Ruhwedel", 35, 20, 40, 60, 60, penaltykill=65,role="bench", position="defense")
]

senators_players = [
    Skater("Tim Stutzle", 60, 60, 60, 50, 80, 40,role="1st Line"),
    Skater("Claude Giroux", 65, 60, 60, 60, 60, 60, 30,role="2nd Line"),
    Skater("Brady Tkachuk", 40, 70, 80, 40, 50, 70,role="2nd Line"),
    Skater("Drake Batherson", 60, 60, 40, 40, 60, 80,role="2nd Line"),
    Skater("Josh Norris", 70, 20, 30, 40, 60, 30, 50,role="2nd Line"),
    Skater("Shane Pinto", 30, 35, 50, 80, 60, 50, 40,role="2nd Line"),
    Skater("Ridley Greig", 40, 50, 50, 55, 20, 35, 50,role="3rd Line"),
    Skater("David Perron", 60, 55, 45, 55, 30, 60,role="Depth"),
    Skater("Michael Amadio", 60, 60, 40, 65, 55,role="4th Line"),
    Skater("Zack MacEwen", 30, 30,30,30, 20,role="Depth"),
    Skater("Noah Gregor", 20, 40, 30, 30, 50,role="4th Line"),
    Skater("Nick Cousins", 35, 35, 50, 30, 60,role="4th Line"),
    Skater("Adam Gaudette", 80, 20, 50, 60, 30, 40,role="4th Line"),
    Skater("Zack Ostapchuk", 30, 20, 30, 50, 40,  role="4th Line"),
    Skater("Jake Sanderson", 40, 40, 60, 60, 80,50, 40,role="Number 1", position="defense"),
    Skater("Thomas Chabot", 60, 60, 80, 60, 60, 30, 50,role="Top Pair", position="defense"),
    Skater("Artem Zub", 40, 50, 45, 70, 40, penaltykill=70,role="2nd Pair", position="defense"),
    Skater("Nick Jensen", 35, 60, 40, 50, 80, penaltykill=20,role="2nd Pair", position="defense"),
    Skater("Travis Hamonic", 40, 30, 35, 20, 30, penaltykill=40,role="3rd Pair", position="defense"),
    Skater("Tyler Kleven", 60, 60, 30, 60, 70,role="3rd Pair", position="defense"),
    Skater("Jacob Bernard-Docker", 60, 40, 20, 55, 35, role="Depth", position="defense")
]

flyers_players = [
    Skater("Travis Konecny", 70, 70, 80, 30, 55, 55, 35,role="1st Line"),
    Skater("Owen Tippett", 60, 50, 60, 40, 60, 50,role="3rd Line"),
    Skater("Matvei Michkov", 60, 55, 60, 35, 30, 40,role="3rd Line"),
    Skater("Joel Farabee", 40, 60, 60, 30, 50, 20,role="3rd Line"),
    Skater("Tyson Foerster", 50, 30, 60, 80, 50, 50,role="3rd Line"),
    Skater("Morgan Frost", 40, 60, 55, 65, 60, 50,role="3rd Line"),
    Skater("Sean Couturier", 20, 60, 50, 60, 50, 30,role="2nd Line"),
    Skater("Scott Laughton", 50, 60, 50, 30, 40, penaltykill=20, role="3rd Line"),
    Skater("Ryan Poehling", 40, 70, 50, 60, 60, penaltykill=50, role="4th Line"),
    Skater("Noah Cates", 30, 40, 60, 80, 60, penaltykill=65,role="4th Line"),
    Skater("Garnet Hathaway", 40, 40, 45, 70, 60, penaltykill=60,role="4th Line"),
    Skater("Bobby Brink", 35, 80, 45, 40, 60, 30,role="4th Line"),
    Skater("Nicolas Deslauriers", 35, 20, 20, 50, 30, role="Depth"),
    Skater("Travis Sanheim", 40, 50, 65, 35, 60, penaltykill= 60,role="Number 1", position="defense"),
    Skater("Cam York", 45, 30, 60, 65, 50,  penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Nick Seeler", 50, 60, 50, 60, 60, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Jamie Drysdale", 60, 40, 40, 20, 60, 60,role="2nd Pair", position="defense"),
    Skater("Erik Johnson", 50, 30, 55, 30, 55, penaltykill=30,role="Depth", position="defense"),
    Skater("Rasmus Ristolainen", 20, 35, 60, 60, 60, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Egor Zamula", 65, 50, 30, 50, 50, 50,role="3rd Pair", position="defense"),
    Skater("Emil Andrae", 20, 35, 70, 65, 30, 35, role="2nd Pair", position="defense"),
]

penguins_players = [
    Skater("Sidney Crosby", 60, 80, 80, 30, 60, 80,role="1st Line"),
    Skater("Evgeni Malkin", 60, 70, 60, 30, 45, 60,role="1st Line"),
    Skater("Bryan Rust", 50, 60, 70, 30, 40, 50, 35,role="1st Line"),
    Skater("Rickard Rakell", 50, 30, 60, 70, 50, 60,role="1st Line"),
    Skater("Michael Bunting", 50, 65, 60, 30, 60, 30,role="3rd Line"),
    Skater("Drew O'Connor", 30, 45, 50, 30, 50, penaltykill=70,role="3rd Line"),
    Skater("Kevin Hayes", 50, 35, 50, 50, 60, 30,role="4th Line"),
    Skater("Cody Glass", 20, 50, 30, 60, 50, penaltykill=50,role="4th Line"),
    Skater("Noel Acciari", 30, 20, 30, 60, 65, penaltykill=40,role="4th Line"),
    Skater("Blake Lizotte", 50, 50, 30, 70, 35, penaltykill=60,role="4th Line"),
    Skater("Anthony Beauvilier", 35, 30, 30, 50, 60,role="4th Line"),
    Skater("Jesse Puljujarvi", 20, 35, 50, 50, 30,role="4th Line"),
    Skater("Valtteri Puustinen", 30, 80, 50, 65, 35, role="Depth"),
    Skater("Phil Tomasino", 40, 40, 50, 40, 70, 50, role="4th Line"),
    Skater("Erik Karlsson", 70, 70, 80, 20, 60, 80,role="Top Pair", position="defense"),
    Skater("Kris Letang", 70, 45, 50, 30, 60, 30, 80,role="Number 1", position="defense"),
    Skater("Marcus Pettersson", 30, 70, 70, 60, 40, penaltykill=80, role="Top Pair", position="defense"),
    Skater("Ryan Graves", 60, 30, 60, 50, 60, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Matt Grzelyck", 35, 60, 30, 20, 40, 70,role="2nd Pair", position="defense"),
    Skater("Sebastian Aho", 55, 35, 55, 50, 80,role="Depth", position="defense"),
    Skater("Pierre-Olivier Joseph", 50, 50, 60, 30, 40, role="Depth", position="defense"),
    Skater("Ryan Shea", 50, 30, 50, 35, 50, penaltykill=60, role="Depth", position="defense"),
    Skater("Jack St. Ivany", 30, 35, 35, 50, 40, penaltykill=40, role="3rd Pair", position="defense"),
]

sharks_players = [
    Skater("William Eklund", 40, 60, 50, 65, 70, 55, 55,role="1st Line"),
    Skater("Tyler Toffoli", 65, 40, 65, 40, 60, 60,role="3rd Line"),
    Skater("Mikael Granlund", 30, 60, 60, 20, 50, 60, 20,role="1st Line"),
    Skater("Fabian Zetterlund", 40, 60, 45, 30, 60, 40,role="2nd Line"),
    Skater("Alexander Wennberg", 40, 50, 30, 65, 60, 55, 20,role="2nd Line"),
    Skater("Macklin Celebrini", 80, 60, 60, 40, 80, 35,role="1st Line"),
    Skater("Will Smith", 60, 50, 50, 20, 30, 20,  role="4th Line"),
    Skater("Luke Kunin", 40, 30, 30, 30, 30, penaltykill=30,role="3rd Line"),
    Skater("Barclay Goodrow", 40, 30, 20, 30, 20, penaltykill=70,role="3rd Line"),
    Skater("Nico Sturm", 50, 45, 40, 30, 50, penaltykill=30,role="4th Line"),
    Skater("Carl Grundstrom", 50, 40, 60, 60, 35,role="4th Line"),
    Skater("Nikolai Kovalenko", 40, 50, 55, 55, 60, role="4th Line"),
    Skater("Ty Dellandrea", 30, 40, 30, 60, 45, penaltykill=40, role="4th Line"),
    Skater("Klim Kostin", 60, 40, 30, 40, 30, role="4th Line"),
    Skater("Thomas Bordeleau", 60, 35, 50, 40, 30, 55,role="Depth"),
    Skater("Cody Ceci", 35, 30, 40, 20, 60, penaltykill=35,role="Top Pair", position="defense"),
    Skater("Jake Walman", 80, 40, 60, 45, 55, 60, 50,role="Top Pair", position="defense"),
    Skater("Mario Ferraro", 30, 40, 60, 20, 50, penaltykill=20,role="2nd Pair", position="defense"),
    Skater("Jan Rutta", 50, 30, 20, 40, 30, penaltykill=30,role="3rd Pair", position="defense"),
    Skater("Timothy Liljgren", 60, 30, 60, 60, 40, 40, role="3rd Pair", position="defense"),
    Skater("Henry Thrun", 40, 30, 35, 30, 50,role="3rd Pair", position="defense"),
    Skater("Jack Thompson", 80, 20, 40, 55, 30, 20, role="Depth", position="defense"),
    Skater("Marc-Eduoard Vlassic", 50, 30, 50, 45, 60, penaltykill=65,role="Depth", position="defense")
]

kraken_players = [
    Skater("Chandler Stephenson", 50, 60, 20, 20, 60, 50, 30,role="1st Line"),
    Skater("Jordan Eberle", 50, 70, 80, 50, 40, 60,role="3rd Line"),
    Skater("Matty Beniers", 55, 50, 30, 80, 70, 20,role="2nd Line"),
    Skater("Andre Burakovsky", 50, 50, 40, 30, 55, 30,role="3rd Line"),
    Skater("Kaapo Kakko", 60, 60, 40, 50, 40, 50, role="4th Line"),
    Skater("Jared McCann", 80, 60, 55, 50, 80, 60, 40,role="2nd Line"),
    Skater("Jaden Schwartz", 40, 50, 40, 60, 40, 30,role="2nd Line"),
    Skater("Oliver Bjorkstrand", 60, 60, 60, 60, 60, 40,role="3rd Line"),
    Skater("Yanni Gourde", 30, 55, 60, 60, 40, penaltykill=80,role="3rd Line"),
    Skater("Eeli Tolvanen", 60, 40, 30, 50, 35, 50,role="4th Line"),
    Skater("Brandon Tanev", 30, 30, 30, 35, 70, penaltykill=30,role="3rd Line"),
    Skater("Shane Wright", 60, 40, 60, 35, 60, 30,role="4th Line"),
    Skater("Tye Kartye", 40, 30, 40, 45, 60,role="4th Line"),
    Skater("Daniel Sprong", 60, 80, 60, 35, 45, 45, role="Depth"),
    Skater("Mitchell Stephens", 40, 50, 30, 40, 40, role="Depth"),
    Skater("Vince Dunn", 80, 70, 80, 50, 60, 50,role="2nd Pair", position="defense"),
    Skater("Brandon Montour", 60, 40, 60, 40, 40, 60,role="Top Pair", position="defense"),
    Skater("Adam Larsson", 30, 40, 35, 40, 40, penaltykill=20,role="2nd Pair", position="defense"),
    Skater("Jamie Oleksiak", 50, 35, 60, 45, 40, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Ryker Evans", 50, 50, 30, 70, 40, 40,role="2nd Pair", position="defense"),
    Skater("Josh Mahura", 20, 50, 55, 30, 30,role="Depth", position="defense")
]

blues_players = [
    Skater("Robert Thomas", 65, 70, 80, 40, 50, 40, 40,role="1st Line"),
    Skater("Jordan Kyrou", 80, 65, 60, 60, 60, 45,role="2nd Line"),
    Skater("Pavel Buchnevich", 60, 60, 70, 60, 40, 50, role="2nd Line"),
    Skater("Brayden Schenn", 55, 60, 40, 40, 30, 55,role="2nd Line"),
    Skater("Jake Neighbours", 60, 30, 30, 30, 50, 40,role="3rd Line"),
    Skater("Brandon Saad", 60, 40, 55, 30, 50, 30,role="3rd Line"),
    Skater("Dylan Holloway", 50, 30, 60, 65, 50, 30,role="3rd Line"),
    Skater("Mathieu Joseph", 20, 60, 40, 60, 65, role="4th Line"),
    Skater("Radek Faksa", 40, 60, 30, 65, 30, penaltykill=30,role="4th Line"),
    Skater("Alexey Toropchenko", 45, 30, 20, 55, 50, penaltykill=55,role="4th Line"),
    Skater("Alexandre Texier", 50, 55, 40, 30, 30, role="3rd Line"),
    Skater("Nathan Walker", 50, 30, 20, 60, 55, role="4th Line"),
    Skater("Zack Bolduc", 60, 30, 30,60, 30, 40,role="4th Line"),
    Skater("Oskar Sundqvist", 40, 50, 30, 45, 50, penaltykill=40,role="4th Line"),
    Skater("Colton Parayko", 60, 35, 20, 70, 60, penaltykill=30, role="Number 1", position="defense"),
    Skater("Cam Fowler", 60, 60, 60, 30, 50, penaltykill=20, role="2nd Pair", position="defense"),
    Skater("Justin Faulk", 20, 60, 30, 40, 40, 55, 50,role="Top Pair", position="defense"),
    Skater("Nick Leddy", 30, 60, 55, 30, 70, penaltykill=30,role="Depth", position="defense"),
    Skater("Philip Broberg", 50, 60, 60, 50, 65, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("Ryan Suter", 30, 40, 40, 60, 40, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Scott Perunovich", 40, 60, 60, 40, 70, 50,role="Depth", position="defense"),
    Skater("Matthew Kessel", 30, 50, 35, 50, 40, role="Depth", position="defense"),
]

lightning_players = [
    Skater("Nikita Kucherov", 65, 80, 80, 40, 70, 70,role="1st Line"),
    Skater("Brayden Point", 80, 65, 60, 30, 70, 60,role="1st Line"),
    Skater("Jake Guentzel", 50, 70, 70, 45, 70, 60,role="1st Line"),
    Skater("Brandon Hagel", 60, 70, 70, 70, 60, 40, 60,role="1st Line"),
    Skater("Anthony Cirelli", 60, 50, 60, 80, 65, 50, 30,role="2nd Line"),
    Skater("Nicholas Paul", 60, 60, 30, 70, 40, 60,role="3rd Line"),
    Skater("Connor Geekie", 50, 50, 30, 50, 60,  role="4th Line"),
    Skater("Zemgus Girgensons", 30, 30, 35, 60, 60, penaltykill=50,role="4th Line"),
    Skater("Luke Glendening", 40, 20, 20, 60, 50, penaltykill=60,role="4th Line"),
    Skater("Conor Sheary", 50, 60, 50, 35, 55,role="Depth"),
    Skater("Mikey Eyssimont", 30, 30, 60, 60, 40,role="4th Line"),
    Skater("Cam Atkinson", 30, 45, 40, 30, 50, 40, 60,role="Depth"),
    Skater("Mitchell Chaffee", 60, 20, 20, 30, 70, role="4th Line"),
    Skater("Gage Goncalves", 30, 20, 30, 60, 65, role="4th Line"),
    Skater("Victor Hedman", 60, 80, 65, 40, 45, 60, 40,role="Top Pair", position="defense"),
    Skater("JJ Moser", 60, 50, 50, 55, 50, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Erik Cernak", 30, 50, 30, 60,  40, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Ryan McDonagh", 30, 60, 70, 70, 50, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("Darren Raddysh", 50, 65, 40, 50, 60, 30, role="3rd Pair", position="defense"),
    Skater("Emil Lilleberg", 20, 60, 30, 30, 30, role="Depth", position="defense"),
    Skater("Nick Perbix", 60, 65, 55, 60, 60,role="Depth", position="defense")
]

leafs_players = [
    Skater("Auston Matthews", 80, 70, 80, 40, 70, 65,role="1st Line"),
    Skater("Mitch Marner", 70, 80, 60, 60, 60, 80, 60, role="1st Line"),
    Skater("William Nylander", 70, 60, 80, 20, 60, 70,role="1st Line"),
    Skater("John Tavares", 30, 65, 65, 65, 40, 80,role="2nd Line"),
    Skater("Matthew Knies", 60, 35, 50, 50, 40, 30, 50,role="2nd Line"),
    Skater("Max Domi", 35, 80, 60, 30, 20, 30,role="3rd Line"),
    Skater("Nicholas Robertson", 65, 50, 35, 45, 65, 30,role="4th Line"),
    Skater("Pontus Holmberg", 50, 45, 30, 60, 60, penaltykill=35,role="4th Line"),
    Skater("Bobby McMann", 70, 35, 40, 60, 30, 35,role="4th Line"),
    Skater("David Kampf", 35, 35, 30, 60, 50, penaltykill=40,role="4th Line"),
    Skater("Max Pacioretty", 20, 50, 50, 30, 30, 50,role="4th Line"),
    Skater("Ryan Reaves", 40, 30, 30, 50, 35,role="4th Line"),
    Skater("Steven Lorentz", 30, 30, 40, 60, 40, penaltykill=65,role="4th Line"),
    Skater("Connor Dewar", 35, 30, 30, 65, 50, penaltykill=70,role="4th Line"),
    # Skater("Calle Jarnkrok", 60, 45, 50, 50, 60, 35, 40,role="Depth"),
    # Skater("Alex Nylander", 60, 30, 60, 30, 45, 45, role="bench"),
    Skater("Morgan Rielly", 30, 70, 60, 30, 60, 65,role="2nd Pair", position="defense"),
    Skater("Oliver Ekman-Larsson", 50, 55, 55, 40, 40, 60, 70,role="2nd Pair", position="defense"),
    Skater("Jake McCabe", 55, 60, 70, 60, 55, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Chris Tanev", 40, 50, 50, 80, 60, penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Simon Benoit", 30, 30, 20, 35, 30, penaltykill=40,role="3rd Pair", position="defense"),
    Skater("Conor Timmins", 50, 70, 65, 40, 30, penaltykill=40,role="3rd Pair", position="defense"),
    Skater("Jani Hakanpaa", 55, 40, 30, 40, 40, penaltykill=65, role="Depth", position="defense"),
    Skater("Philippe Myers", 20, 20, 60, 60, 80, penaltykill=40, role="3rd Pair", position="defense"),
]

utah_players = [
    Skater("Clayton Keller", 70, 60, 60, 40, 65, 30, role="1st Line"),
    Skater("Barrett Hayton", 30, 30, 70, 65, 70,60,role="3rd Line"),
    Skater("Nick Schmaltz", 60, 60, 60, 40, 60, 60,role="1st Line"),
    Skater("Logan Cooley", 60, 60, 45, 45, 60, 20, 45,role="2nd Line"),
    Skater("Dylan Guenther", 70, 50, 45, 40, 30, 50,role="3rd Line"),
    Skater("Alex Kerfoot", 30, 60, 40, 65, 60, penaltykill=30,role="3rd Line"),
    Skater("Lawson Crouse", 60, 40, 50, 50, 35, 30, 40,role="4th Line"),
    Skater("Matias Maccelli", 50, 60, 50, 50, 60, 30,role="4th Line"),
    Skater("Nick Bjugstad", 55, 60, 60, 35, 35,role="4th Line"),
    Skater("Jack McBain", 50, 60, 60, 40, 20, penaltykill=60,role="4th Line"),
    Skater("Kevin Stenlund", 40, 30, 20, 60, 20, penaltykill=50,role="3rd Line"),
    Skater("Liam O'Brien", 35, 40, 30, 70, 20, role="Depth"),
    Skater("Kailer Yamamoto", 45, 30, 55, 60, 60, 50,role="Depth"),
    Skater("Michael Carcone", 65, 30, 50, 30, 30,role="4th Line"),
    Skater("Josh Doan", 70, 30, 65, 70, 55, role="Depth"),
    Skater("Mikhail Sergachev", 70, 60, 60, 40, 45, 60,50,role="Number 1", position="defense"),
    Skater("Ian Cole", 35, 50, 50, 60, 30, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Juuso Valimaki", 20, 40, 60, 50, 60, penaltykill=55, role="3rd Pair", position="defense"),
    Skater("Michael Kesselring", 60, 70, 60, 40, 30,role="2nd Pair", position="defense"),
    Skater("Robert Bortuzzo", 30, 20, 45, 45, 20,role="Depth", position="defense"),
    Skater("Olli Maatta", 55, 40, 20, 80, 65, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Vladislav Kolyachonok", 70, 80, 65, 50, 40,role="Depth", position="defense"),
    Skater("Maveric Lamoureux", 60, 40, 50, 70, 20, role="3rd Pair", position="defense"),
    # Skater("Sean Durzi", 55, 50, 50, 45, 45, 70, 60,role="Depth", position="defense"),
    # Skater("John Marino", 30, 60, 30, 65, 70, penaltykill=45,role="Depth", position="defense"),
]

canucks_players = [
    Skater("Elias Pettersson", 70, 80, 60, 60, 80, 70, role="1st Line"),
    Skater("JT Miller", 65, 80, 60, 55, 55, 60,role="2nd Line"),
    Skater("Brock Boeser", 60, 60, 50, 30, 35, 60,role="2nd Line"),
    Skater("Jake DeBrusk", 60, 35, 60, 60, 50, 60, role="2nd Line"),
    Skater("Conor Garland", 60, 60, 65, 80, 80, 40,role="1st Line"),
    Skater("Nils Hoglander", 60, 50, 50, 60, 40,role="4th Line"),
    Skater("Dakota Joshua", 55, 40, 40, 50, 45, role="4th Line"),
    Skater("Teddy Blueger", 20, 70, 50, 50, 40, penaltykill=40,role="3rd Line"),
    Skater("Danton Heinen", 50, 60, 45, 50, 30, penaltykill=70,role="4th Line"),
    Skater("Pius Suter", 60, 40, 40, 80, 55, penaltykill= 60,role="3rd Line"),
    Skater("Kiefer Sherwood", 60, 60, 40, 70, 35, penaltykill=60,role="4th Line"),
    Skater("Nils Aman", 30, 40, 20, 60, 40, penaltykill=70,role="Depth"),
    Skater("Arshdeep Bains",  35, 20, 30, 40, 45,role="Depth"),
    Skater("Quinn Hughes", 70, 80, 80, 70, 80, 80,role="Number 1", position="defense"),
    Skater("Filip Hronek", 45, 60, 40, 50, 35, 60, 60,role="Top Pair", position="defense"),
    Skater("Carson Soucy", 40, 30, 30, 60, 35, penaltykill=40,role="2nd Pair", position="defense"),
    Skater("Tyler Myers", 30, 60, 40, 50, 20, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Derek Forbort", 60, 40, 35, 80, 40, penaltykill=70,role="3rd Pair", position="defense"),
    Skater("Vincent Desharnais", 35, 30, 30, 60, 30, penaltykill=80,role="Depth", position="defense"),
    Skater("Noah Juulsen", 30, 30, 30, 40, 40, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Erik Brannstrom", 35, 60, 60, 60, 50,role="Depth", position="defense")
]

knights_players = [
    Skater("Jack Eichel", 70, 70, 60, 70, 80, 50, 40,role="1st Line"),
    Skater("Mark Stone", 60, 70, 70, 80, 65, 60, 60,role="1st Line"),
    Skater("Tomas Hertl", 30, 60, 60, 40, 40, 60, role="2nd Line"),
    Skater("William Karlsson", 50, 60, 65, 80, 70, 60, 50,role="2nd Line"),
    Skater("Ivan Barbashev", 60, 70, 50, 20, 60, role="2nd Line"),
    Skater("Victor Olofsson", 70, 55, 30, 50, 45, 50,role="3rd Line"),
    Skater("Brett Howden", 50, 40, 35, 30, 30, penaltykill=30,role="3rd Line"),
    Skater("Alexander Holtz", 50, 40, 30, 40, 40,  role="4th Line"),
    Skater("Pavel Dorofeyev", 65, 40, 60, 60, 40, 40,role="3rd Line"),
    Skater("Keegan Kolesar", 50, 40, 50, 50, 40,role="4th Line"),
    Skater("Tanner Pearson", 30, 40, 40, 30, 60,role="4th Line"),
    Skater("Brendan Brisson", 35, 60, 50, 40, 40,role="Depth"),
    Skater("Jonas Rondbjerg", 20, 50, 20, 60, 45,role="Depth"),
    Skater("Cole Schwindt", 20, 30, 40, 50, 80, role="4th Line"),
    Skater("Nicolas Roy", 35, 55, 60, 55, 20, 50, role="3rd Line"),
    Skater("Alex Pietrangelo", 40, 65, 80, 30, 70, penaltykill= 45,role="Top Pair", position="defense"),
    Skater("Shea Theodore", 60, 80, 60, 30, 60, 60,role="2nd Pair", position="defense"),
    Skater("Noah Hanafin", 65, 65, 70, 30, 60, 35,35,role="2nd Pair", position="defense"),
    Skater("Brayden McNabb", 30, 40, 50, 80, 45, penaltykill=45,role="2nd Pair", position="defense"),
    Skater("Nick Hague", 40, 30, 60, 35, 60, role="3rd Pair", position="defense"),
    Skater("Kaeden Korczak", 30, 65, 60, 60, 35,role="Depth", position="defense"),
    Skater("Ben Hutton", 50, 50, 35, 60, 60, role="Depth", position="defense"),
    Skater("Zach Whitecloud", 60, 40, 50, 60, 50,role="3rd Pair", position="defense")
]

capitals_players = [
    Skater("Alexander Ovechkin", 80, 60, 40, 20, 30, 70,role="2nd Line"),
    Skater("Tom Wilson", 60, 35, 50, 70, 40, 60, 50,role="1st Line"),
    Skater("Dylan Strome", 60, 60, 70, 40, 40, 60,role="2nd Line"),
    Skater("Pierre-Luc Dubois", 30, 70, 70, 60, 50,60,role="2nd Line"),
    Skater("Connor McMichael", 60, 40, 60, 30, 30, 40, role="2nd Line"),
    Skater("Nic Dowd", 60, 40, 40, 70, 30, penaltykill=50, role="3rd Line"),
    Skater("Lars Eller", 40, 35, 30, 60, 30,  penaltykill=40, role="3rd Line"),
    Skater("Sonny Milano", 50, 50, 60, 65, 40,role="4th Line"),
    Skater("Aliaksi Protas", 40, 60, 50, 50, 60, penaltykill=60,role="3rd Line"),
    Skater("Andrew Mangiapane", 30, 60, 60, 60, 50, 40,role="4th Line"),
    Skater("Brandon Duhaime", 30, 40, 50, 40, 60, penaltykill=35,role="4th Line"),
    Skater("Hendrix Lapierre", 50, 50, 30, 30, 65, role="4th Line"),
    Skater("Taylor Raddysh", 35, 30, 60, 60, 40, role="4th Line"),
    Skater("Jakub Vrana", 70, 55, 40, 30, 30, role="4th Line"),
    Skater("John Carlson", 40, 60, 80, 35, 70, 70, 30,role="Number 1", position="defense"),
    Skater("Jakob Chychrun", 70, 55, 40, 30, 30, 60,role="2nd Pair", position="defense"),
    Skater("Matt Roy", 45, 60, 55, 60, 40, penaltykill=70,role="2nd Pair", position="defense"),
    Skater("Martin Fehervary", 40, 40, 50, 60, 70, penaltykill=60,role="2nd Pair", position="defense"),
    Skater("Trevor Van Riemsdyk", 40, 65, 50, 80, 60, penaltykill=60,role="3rd Pair", position="defense"),
    Skater("Rasmus Sandin", 60, 60, 60, 40, 60, role="2nd Pair", position="defense"),
]

jets_players = [
    Skater("Kyle Connor", 70, 50, 60, 35, 60, 60,role="1st Line"),
    Skater("Mark Scheifele", 70, 65, 65, 20, 70, 60,role="1st Line"),
    Skater("Gabriel Vilardi", 80, 50, 50, 40, 80, 60,role="2nd Line"),
    Skater("Nikolai Ehlers", 60, 70, 70, 45, 80, 60,role="3rd Line"),
    Skater("Adam Lowry", 30, 35, 65, 80, 50, penaltykill=30,role="3rd Line"),
    Skater("Nino Niederreiter", 50, 40, 60, 60, 60, 20,role="3rd Line"),
    Skater("Mason Appleton", 40, 50, 60, 40, 60, role="3rd Line"),
    Skater("Cole Perfetti", 50, 60, 30, 50, 40, 40,role="3rd Line"),
    Skater("Vladislav Namestnikov", 35, 40, 40, 50, 45, 30, role="3rd Line"),
    Skater("Alex Iafallo", 50, 40, 35, 70, 55, 40, 60,role="4th Line"),
    Skater("Morgan Barron", 30, 30, 35, 55, 40, penaltykill=50,role="4th Line"),
    Skater("Rasmus Kupari", 30, 30, 30, 65, 60, penaltykill=45,role="4th Line"),
    Skater("Josh Morrissey", 65, 70, 80, 60, 65, 50,role="Number 1", position="defense"),
    Skater("Dylan DeMelo", 50, 60, 30, 60, 50, penaltykill=30,role="2nd Pair", position="defense"),
    Skater("Neal Pionk", 60, 60, 35, 30, 40, 20, 50,role="Top Pair", position="defense"),
    Skater("Dylan Samberg", 50, 60, 60, 60, 50, penaltykill=60, role="2nd Pair", position="defense"),
    Skater("Logan Stanley", 60, 40, 40, 40, 20, penaltykill=50,role="3rd Pair", position="defense"),
    Skater("Haydn Fleury", 20, 60, 20, 50, 60, penaltykill=40, role="Depth", position="defense"),
    Skater("Colin Miller", 60, 60, 40, 60, 60, role="Depth", position="defense")
]