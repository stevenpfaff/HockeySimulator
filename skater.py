class Skater:
    role_weights = {
        '1st Line': 1.2,
        '2nd Line': 1.0,
        '3rd Line': 0.8,
        '4th Line': 0.6,
        'Number 1': 1.5,
        'Top Pair': 1.3,
        'Second Pair': 1.0,
        'Third Pair': 0.8,
        'bench': 0.2
    }
    def __init__(self, name, shooting=None, passing=None, offense=None, defense=None, role="bench", goals=0, assists=0, points=0,):
        self.name = name
        self.shooting = shooting or 50
        self.passing = passing or 50
        self.offense = offense or 50
        self.defense = defense or 50
        self.goals = goals
        self.assists = assists
        self.points = points
        self.role = role

    def overall(self):
        weights = {'shooting': 0.2, 'passing': 0.1, 'offense': 0.35, 'defense': 0.35}
        return (self.shooting * weights['shooting'] +
                self.passing * weights['passing'] +
                self.offense * weights['offense'] +
                self.defense * weights['defense'])
    def update_stats(self, goals=0, assists=0):
        self.goals += goals
        self.assists += assists
        self.points += goals + assists

ducks_players = [
    Skater("Troy Terry", 60, 60, 55, 50, role="1st Line"),
    Skater("Alex Killorn", 60, 55, 50, 45, role="1st Line"),
    Skater("Leo Carlsson", 50, 30, 60, 60, role="1st Line"),
    Skater("Frank Vatrano", 70, 40, 30, 20, role="2nd Line"),
    Skater("Trevor Zegras", 55, 60, 60, 30, role="2nd Line"),
    Skater("Cutter Gauthier", 55, 40, 55, 40, role="2nd Line"),
    Skater("Ryan Strome", 45, 50, 50, 20, role="3rd Line"),
    Skater("Robby Fabbri", 60, 20, 40, 30, role="3rd Line"),
    Skater("Mason McTavish", 55, 60, 60, 30, role="3rd Line"),
    Skater("Brett Leason", 50, 30, 20, 30, role="4th Line"),
    Skater("Brock McGinn", 30, 20, 30, 50, role="4th Line"),
    Skater("Isac Lundestrom", 30, 30, 20, 60, role="4th Line"),
    Skater("Sam Colangelo", 50, 40, 50, 50, role="bench"),
    Skater("Ross Johnston", 20, 20, 20, 40, role="bench"),
    Skater("Cam Fowler", 55, 50, 50, 50, role="Top Pair"),
    Skater("Pavel Mintyukov", 50, 40, 65, 30, role="Top Pair"),
    Skater("Radko Gudas", 50, 50, 55, 70, role="2nd Pair"),
    Skater("Brian Dumoulin", 50, 55, 40, 60, role="2nd Pair"),
    Skater("Olen Zellweger", 50, 50, 50, 30, role="3rd Pair"),
    Skater("Gustav Lindstrom", 30, 60, 30, 45, role="3rd Pair")
]

bruins_players = [
    Skater("Brad Marchand", 60, 65, 65, 50, role="1st Line"),
    Skater("David Pastrnak", 90, 80, 85, 50, role="1st Line"),
    Skater("Elias Lindholm", 55, 60, 50, 45, role="1st Line"),
    Skater("Charlie Coyle", 65, 55, 45, 40, role="2nd Line"),
    Skater("Pavel Zacha", 60, 60, 45, 40, role="2nd Line"),
    Skater("Trent Frederic", 60, 55, 60, 55, role="2nd Line"),
    Skater("Morgan Geekie", 55, 60, 50, 30, role="3rd Line"),
    Skater("John Beecher", 60, 30, 20, 40, role="3rd Line"),
    Skater("Mark Kastelic", 40, 20, 40, 60, role="3rd Line"),
    Skater("Patrick Brown", 30, 30, 30, 50, role="4th Line"),
    Skater("Justin Brazeau", 55, 30, 50, 60, role="4th Line"),
    Skater("Max Jones", 20, 50, 50, 45, role="4th Line"),
    Skater("Charlie McAvoy", 60, 65, 80, 60, role="Number 1"),
    Skater("Hampus Lindholm", 35, 60, 65, 70, role="Top Pair"),
    Skater("Brandon Carlo", 50, 55, 30, 65, role="2nd Pair"),
    Skater("Nikita Zadorov", 60, 55, 40, 60, role="2nd Pair"),
    Skater("Andrew Peeke", 40, 50, 20, 60, role="3rd Pair"),
    Skater("Mason Lohrei", 60, 30, 20, 20, role="3rd Pair"),
    Skater("Parker Wotherspoon", 20, 20, 60, 60, role="bench")
]

sabres_players = [
    Skater("Tage Thompson", 80, 65, 65, 30, role="1st Line"),
    Skater("Alex Tuch", 55, 80, 70, 45, role="1st Line"),
    Skater("JJ Peterka", 60, 55, 60, 30, role="1st Line"),
    Skater("Dylan Cozens", 50, 60, 60, 30, role="2nd Line"),
    Skater("Jack Quinn", 60, 60, 60, 50, role="2nd Line"),
    Skater("Jason Zucker", 55, 50, 70, 30, role="2nd Line"),
    Skater("Jordan Greenway", 30, 30, 30, 65, role="3rd Line"),
    Skater("Zach Benson", 40, 60, 60, 60, role="3rd Line"),
    Skater("Ryan McLeod", 50, 60, 60, 65, role="3rd Line"),
    Skater("Sam Lafferty", 55, 35, 20, 50, role="4th Line"),
    Skater("Nicolas Aube-Kubel", 35, 45, 30, 70, role="4th Line"),
    Skater("Beck Malenstyn", 30, 30, 30, 30, role="4th Line"),
    Skater("Peyton Krebs", 30, 30, 20, 55, role="bench"),
    Skater("Rasmus Dahlin", 70, 70, 80, 65, role="Number 1"),
    Skater("Owen Power", 30, 50, 60, 40, role="Top Pair"),
    Skater("Bowen Byram", 80, 60, 30, 20, role="2nd Pair"),
    Skater("Henri Jokijarju", 30, 50, 35, 35, role="2nd Pair"),
    Skater("Connor Clifton", 30, 60, 50, 35, role="3rd Pair"),
    Skater("Mattias Samuelsson", 20, 30, 40, 50, role="3rd Pair"),
    Skater("Jacob Bryson", 35, 55, 30, 60, role="bench")
]

flames_players = [
    Skater("Blake Coleman", 55, 50, 60, 65, role="1st Line"),
    Skater("Mikael Backlund", 30, 60, 60, 65, role="1st Line"),
    Skater("Jonathan Huberdeau", 40, 70, 60, 35, role="1st Line"),
    Skater("Andrei Kuzmenko", 80, 60, 55, 50, role="2nd Line"),
    Skater("Nazem Kadri", 55, 80, 60, 50, role="2nd Line"),
    Skater("Connor Zary", 65, 60, 30, 65, role="2nd Line"),
    Skater("Yegor Sharangovich", 65, 40, 45, 30, role="3rd Line"),
    Skater("Martin Pospisil", 30, 50, 60, 45, role="3rd Line"),
    Skater("Anthony Mantha", 65, 60, 60, 70, role="3rd Line"),
    Skater("Kevin Rooney", 30, 20, 30, 55, role="4th Line"),
    Skater("Ryan Lomberg", 40, 30, 50, 45, role="4th Line"),
    Skater("Walker Dueher", 50, 65, 50, 30, role="4th Line"),
    Skater("Dryden Hunt", 30, 30, 20, 60, role="bench"),
    Skater("MacKenzie Weegar", 65, 55, 60, 70, role="Top Pair"),
    Skater("Rasmus Andersson", 50, 65, 65, 30, role="Top Pair"),
    Skater("Kevin Bahl", 40, 35, 30, 60, role="2nd Pair"),
    Skater("Danill Miromanov", 65, 60, 50, 50, role="2nd Pair"),
    Skater("Tyson Barrie", 60, 60, 45, 20, role="3rd Pair"),
    Skater("Jake Bean", 60, 50, 35, 30, role="3rd Pair"),
    Skater("Brayden Pachal", 35, 30, 20, 50, role="bench"),
    Skater("Joel Hanley", 35, 30, 30, 60, role="bench")
]

hurricanes_players = [
    Skater("Sebastian Aho", 70, 70, 70, 60, role="1st Line"),
    Skater("Andrei Svechnikov", 50, 65, 80, 40, role="1st Line"),
    Skater("Seth Jarvis", 60, 50, 60, 80, role="1st Line"),
    Skater("Jesperi Kotkaniemi", 50, 40, 50, 50, role="2nd Line"),
    Skater("Martin Necas", 60, 60, 60, 20, role="2nd Line"),
    Skater("Jesper Fast", 30, 40, 60, 70, role="2nd Line"),
    Skater("Jack Drury", 20, 50, 35, 70, role="3rd Line"),
    Skater("Jordan Staal", 30, 30, 50, 80, role="3rd Line"),
    Skater("Jack Roslovic", 40, 65, 50, 30, role="3rd Line"),
    Skater("Tyson Jost", 30, 40, 30, 40, role="4th Line"),
    Skater("William Carrier", 30, 35, 60, 60, role="4th Line"),
    Skater("Jordan Martinook", 30, 60, 55, 60, role="4th Line"),
    Skater("Brendan Lemieux", 40, 50, 35, 30, role="bench"),
    Skater("Eric Robinson", 20, 45, 50, 20, role="bench"),
    Skater("Ryan Suzuki", 30, 40, 35, 35, role="bench"),
    Skater("Jaccob Slavin", 30, 60, 70, 80, role="Top Pair"),
    Skater("Brent Burns", 70, 60, 70, 55, role="Top Pair"),
    Skater("Sean Walker", 60, 55, 65, 50, role="2nd Pair"),
    Skater("Dimitry Orlov", 60, 40, 60, 60, role="2nd Pair"),
    Skater("Shayne Gostisbehere", 80, 60, 55, 30, role="3rd Pair"),
    Skater("Jalen Chatfield", 60, 35, 60, 60, role="3rd Pair")
]

blackhawks_players = [
    Skater("Connor Bedard", 60, 60, 55, 20, role="1st Line"),
    Skater("Tyler Bertuzzi", 50, 60, 80, 30, role="1st Line"),
    Skater("Teuvo Teravainen", 60, 60, 30, 60, role="1st Line"),
    Skater("Andreas Athanasiou", 45, 45, 40, 20, role="2nd Line"),
    Skater("Philip Kurashev", 50, 30, 30, 20, role="2nd Line"),
    Skater("Taylor Hall", 50, 50, 50, 20, role="2nd Line"),
    Skater("Jason Dickinson", 60, 30, 30,70, role="3rd Line"),
    Skater("Nick Foligno", 35, 55, 40, 60, role="3rd Line"),
    Skater("Ilya Mikheyev", 55, 60, 55, 60, role="3rd Line"),
    Skater("Craig Smith", 50, 30, 60, 45, role="4th Line"),
    Skater("Ryan Donato", 50, 55, 50, 40, role="4th Line"),
    Skater("Lukas Reichel", 30, 50, 30, 30, role="4th Line"),
    Skater("Joey Anderson", 50, 60, 30, 65, role="bench"),
    Skater("Patrick Maroon", 30, 40, 40, 40, role="bench"),
    Skater("Frank Nazar", 50, 50, 50, 20, role="bench"),
    Skater("Nolan Slaggert", 50, 50, 50, 20, role="bench"),
    Skater("Seth Jones", 40, 55, 60, 55, role="Number 1"),
    Skater("Alex Vlassic", 35, 30, 50, 70, role="Top Pair"),
    Skater("Connor Murphy", 60, 20, 50, 70, role="2nd Pair"),
    Skater("Kevin Korchinski", 60, 20, 50, 20, role="2nd Pair"),
    Skater("Alec Martinez", 60, 30, 40, 55, role="3rd Pair"),
    Skater("TJ Brodie", 30, 50, 35,65, role="3rd Pair")
]

avalanche_players = [
    Skater("Nathan MacKinnon", 85, 90, 85, 30, role="1st Line"),
    Skater("Mikko Rantanen", 80, 60, 70,20, role="1st Line"),
    Skater("Jonathan Drouin", 55, 60, 60, 40, role="1st Line"),
    Skater("Casey Mittelstadt", 60, 70, 55, 55, role="2nd Line"),
    Skater("Artturi Lehkonen", 60, 60, 65, 80, role="2nd Line"),
    Skater("Nikolai Kovalenko", 50, 50, 50, 30, role="2nd Line"),
    Skater("Ross Colton", 45, 55, 60, 40, role="3rd Line"),
    Skater("Miles Wood", 20, 65, 55, 20, role="3rd Line"),
    Skater("Logan O'Connor", 40, 50, 60, 80, role="3rd Line"),
    Skater("Parker Kelly", 20, 20, 20, 60, role="4th Line"),
    Skater("Chris Wagner", 30, 30, 30, 30, role="4th Line"),
    Skater("Joel Kiviranta", 20, 20, 35, 60, role="4th Line"),
    Skater("Gabriel Landeskog", 60, 60, 60, 60, role="bench"),
    Skater("Cale Makar", 80, 70, 70, 65, role="Number 1"),
    Skater("Devon Toews", 65, 65, 60, 70, role="Top Pair"),
    Skater("Samuel Girard", 55, 60, 60, 40, role="2nd Pair"),
    Skater("Josh Manson", 60, 70, 50, 50, role="2nd Pair"),
    Skater("Oliver Kylington", 60, 30, 60, 30, role="3rd Pair"),
    Skater("Calvin deHaan", 40, 40, 55, 60, role="3rd Pair"),
    Skater("Keaton Middleton", 30, 30, 30, 50, role="bench")
]

bluejackets_players = [
    # Skater("Johnny Gaudreau", 40, 80, 80, 20), RIP Johnny Gaudreau </3
    Skater("Boone Jenner", 60, 30, 55, 55, role="1st Line"),
    Skater("Kirill Marchenko", 60, 30, 30, 50, role="1st Line"),
    Skater("Sean Monahan", 55, 65, 60, 30, role="1st Line"),
    Skater("Adam Fantilli", 60, 60, 30, 30, role="2nd Line"),
    Skater("Kent Johnson", 55, 60, 20, 40, role="2nd Line"),
    Skater("Yegor Chinakhov", 60, 30, 30, 60, role="2nd Line"),
    Skater("Cole Sillinger", 20, 40, 40, 30, role="3rd Line"),
    Skater("James van Riemsdyk", 30, 60, 70, 55, role="3rd Line"),
    Skater("Dimitri Voronkov", 50, 60, 65, 30, role="3rd Line"),
    Skater("Sean Kuraly", 50, 30, 35, 40, role="4th Line"),
    Skater("Mathieu Olivier", 30, 30, 50, 55, role="4th Line"),
    Skater("Justin Danforth", 40, 30, 60, 60, role="4th Line"),
    Skater("Gavin Brindley", 30, 30, 30, 30, role="bench"),
    Skater("Zach Werenski", 60, 80, 70, 40, role="Number 1"),
    Skater("Ivan Provorov", 55, 35, 50, 30, role="Top Pair"),
    Skater("Jordan Harris", 55, 60, 60, 55, role="2nd Pair"),
    Skater("Damon Severson", 60, 60, 80, 55, role="2nd Pair"),
    Skater("Erik Gudbranson", 50, 35, 20, 30, role="3rd Pair"),
    Skater("Jack Johnson", 35, 35, 20, 30, role="3rd Pair")
]

stars_players = [
    Skater("Jason Robertson", 80, 70, 80, 80, role="1st Line"),
    Skater("Roope Hintz", 80, 65, 70, 60, role="1st Line"),
    Skater("Wyatt Johnston", 65, 60, 60, 55, role="1st Line"),
    Skater("Jamie Benn", 60, 60, 70, 30, role="2nd Line"),
    Skater("Tyler Seguin", 65, 50, 70,20, role="2nd Line"),
    Skater("Matt Duchene", 65, 65, 60, 20, role="2nd Line"),
    Skater("Mason Marchment", 60, 65, 60,60, role="3rd Line"),
    Skater("Evgeni Dadonov", 55, 30,50, 40, role="3rd Line"),
    Skater("Logan Stankoven", 40, 65, 65, 60, role="3rd Line"),
    Skater("Sam Steel", 35, 50, 50, 60, role="4th Line"),
    Skater("Colin Blackwell", 30, 45, 35, 50, role="4th Line"),
    Skater("Mavrik Bourque", 50, 50, 50, 30, role="4th Line"),
    Skater("Miro Heiskanen", 40, 60, 70,70, role="Number 1"),
    Skater("Esa Lindell", 50, 55, 60, 70, role="Top Pair"),
    Skater("Thomas Harley", 80, 55, 70, 45, role="2nd Pair"),
    Skater("Ilya Lyubushkin", 30, 40, 30, 45, role="2nd Pair"),
    Skater("Matt Dumba", 40, 30, 30, 30, role="3rd Pair"),
    Skater("Nils Lundkvist", 45, 50, 50, 30, role="3rd Pair"),
    Skater("Brendan Smith", 50, 20, 30, 50, role="bench")
]

redwings_players = [
    Skater("Dylan Larkin", 70, 70, 70, 55, role="1st Line"),
    Skater("Lucas Raymond", 65, 50, 30, 30, role="1st Line"),
    Skater("Alex DeBrincat", 60, 60, 65, 30, role="1st Line"),
    Skater("Patrick Kane", 70, 60, 50, 20, role="2nd Line"),
    Skater("JT Compher", 60, 55, 50, 70, role="2nd Line"),
    Skater("Vladimir Tarasenko", 65, 60, 60, 20, role="2nd Line"),
    Skater("Andrew Copp", 40, 50, 30, 50, role="3rd Line"),
    Skater("Michael Rasmussen", 45, 60, 50, 55, role="3rd Line"),
    Skater("Jonatan Berggren", 60, 50, 50, 40, role="3rd Line"),
    Skater("Joe Veleno", 50, 30, 30,45, role="4th Line"),
    Skater("Christian Fischer", 30, 40, 50, 45, role="4th Line"),
    Skater("Tyler Motte", 30, 40, 35, 60, role="4th Line"),
    Skater("Austin Watson", 30, 20, 20, 50, role="4th Line"),
    Skater("Moritz Seider", 50, 60, 35, 55, role="Number 1"),
    Skater("Ben Chiarot", 50, 55, 30, 40, role="Top Pair"),
    Skater("Jeff Petry", 50, 55, 50, 55, role="2nd Pair"),
    Skater("Simon Edvinsson", 60, 35, 55, 55, role="2nd Pair"),
    Skater("Erik Gustafsson", 55, 65, 60, 65, role="3rd Pair"),
    Skater("Olli Maatta", 55, 45, 30, 70, role="3rd Pair"),
    Skater("Justin Holl", 30, 20, 40, 40, role="bench")
]

oilers_players = [
    Skater("Connor McDavid", 80, 90, 90, 60, role="1st Line"),
    Skater("Leon Draisaitl", 90, 85, 80,20, role="1st Line"),
    Skater("Ryan Nugent-Hopkins", 40, 60, 60, 60, role="1st Line"),
    Skater("Zach Hyman", 70, 60, 85, 40, role="2nd Line"),
    Skater("Jeff Skinner", 65, 70, 80, 20, role="2nd Line"),
    Skater("Viktor Arvidsson", 50, 50, 65, 40, role="2nd Line"),
    Skater("Mattias Janmark", 30, 40, 30, 60, role="3rd Line"),
    Skater("Connor Brown", 20, 50, 50, 50, role="3rd Line"),
    Skater("Adam Henrique", 60, 45, 60, 45, role="3rd Line"),
    Skater("Derek Ryan", 40, 30, 55, 70, role="4th Line"),
    Skater("Corey Perry", 40, 40, 50, 60, role="4th Line"),
    Skater("Vasaily Podkolzin", 35, 30, 40, 45, role="4th Line"),
    Skater("Evander Kane", 45, 30, 30, 20, role="bench"),
    Skater("Darnell Nurse", 60, 60, 70,50, role="Top Pair"),
    Skater("Evan Bouchard", 70, 60, 80, 50, role="Top Pair"),
    Skater("Mattias Ekholm", 55, 80, 80, 65, role="2nd Pair"),
    Skater("Brett Kulak", 50, 30, 40, 50, role="2nd Pair"),
    Skater("Troy Stecher", 30, 40, 30, 40, role="3rd Pair"),
    Skater("Ty Emberson", 35, 55, 20, 60, role="3rd Pair"),
    Skater("Josh Brown", 40, 30, 40, 30, role="bench")
]

panthers_players = [
    Skater("Matthew Tkachuk", 50, 80, 90, 35, role="1st Line"),
    Skater("Aleksander Barkov", 60, 80, 70, 85, role="1st Line"),
    Skater("Sam Reinhart", 85, 65, 60, 85, role="1st Line"),
    Skater("Sam Bennett", 50, 60, 65, 60, role="2nd Line"),
    Skater("Carter Verhaeghe", 70, 60, 70, 30, role="2nd Line"),
    Skater("Evan Rodrigues", 20, 50, 65, 80, role="2nd Line"),
    Skater("Eetu Luostarainen", 40, 40, 60, 70, role="3rd Line"),
    Skater("Jonah Gadjovich", 20, 30, 45, 40, role="3rd Line"),
    Skater("Anton Lundell", 30, 40, 45, 40, role="3rd Line"),
    Skater("Jesper Boqvist", 55, 45, 40, 60, role="4th Line"),
    Skater("AJ Greer", 30, 30, 45, 55, role="4th Line"),
    Skater("Tomas Nosek", 20, 45, 30, 45, role="4th Line"),
    Skater("Aaron Ekblad", 70, 60, 60, 55, role="Top Pair"),
    Skater("Gustav Forsling", 70, 80, 60, 65, role="Top Pair"),
    Skater("Dimitry Kulikov", 30,60, 40, 40, role="2nd Pair"),
    Skater("Niko Mikkola", 30, 30, 30, 60, role="2nd Pair"),
    Skater("Nate Schmidt", 40, 35, 50, 55, role="3rd Pair"),
    Skater("Adam Boqvist", 60, 40, 60, 20, role="3rd Pair"),
    Skater("Uvis Balinskis", 35, 30, 30, 40, role="bench"),
    Skater("Tobias Bjornfoot", 30, 30, 30, 30, role="bench"),
    Skater("John Ludvig", 50, 30, 45, 40, role="bench")
]

kings_players = [
    Skater("Anze Kopitar", 65, 60, 60, 60, role="1st Line"),
    Skater("Adrian Kempe", 70, 40, 60, 50, role="1st Line"),
    Skater("Kevin Fiala", 60, 80, 80, 55, role="1st Line"),
    Skater("Quinton Byfield", 35, 65, 60, 80, role="2nd Line"),
    Skater("Phillip Danault", 60, 55, 60, 60, role="2nd Line"),
    Skater("Arthur Kaliyev", 35, 50, 60, 45, role="2nd Line"),
    Skater("Trevor Moore", 55, 60, 55, 70, role="3rd Line"),
    Skater("Alexis Lafferiere", 30, 20, 35, 30, role="3rd Line"),
    Skater("Warren Foegle", 30, 60, 70, 50, role="3rd Line"),
    Skater("Tanner Jeannot", 50, 30, 45, 50, role="4th Line"),
    Skater("Trevor Lewis", 30, 35, 20, 60, role="4th Line"),
    Skater("Alex Turcotte", 35, 35, 35, 35, role="4th Line"),
    Skater("Drew Doughty", 65, 50, 55,80, role="bench"),
    Skater("Mikey Anderson", 30, 35, 20, 65, role="Top Pair"),
    Skater("Vladislav Gavrikov", 50, 50, 55, 50, role="2nd Pair"),
    Skater("Brandt Clarke", 55, 50, 60, 30, role="2nd Pair"),
    Skater("Jordan Spence", 30, 60, 60, 35, role="Top Pair"),
    Skater("Kyle Burroughs", 35, 30, 45, 55, role="3rd Pair"),
    Skater("Joel Edmundson", 40, 20, 55, 20, role="3rd Pair"),
    Skater("Andreas Englund", 30, 30, 30, 60, role="bench"),
    Skater("Jacob Moverare", 20, 20, 50, 50, role="bench")
]

wild_players = [
    Skater("Kirill Kaprizov", 85, 65, 80, 60, role="1st Line"),
    Skater("Matthew Boldy", 60, 55, 70, 70, role="1st Line"),
    Skater("Joel Eriksson-Ek", 30, 60, 60, 65, role="1st Line"),
    Skater("Mats Zuccarello", 60, 80, 55, 40, role="2nd Line"),
    Skater("Marcus Foligno", 55, 50, 60, 70, role="2nd Line"),
    Skater("Ryan Hartman", 60, 60, 60, 30, role="2nd Line"),
    Skater("Frederick Gaudreau", 40, 30, 20, 35, role="3rd Line"),
    Skater("Marcus Johansson", 45, 35, 55, 60, role="3rd Line"),
    Skater("Marco Rossi", 55, 30, 40, 40, role="3rd Line"),
    Skater("Marat Kushnutdinov", 50, 50, 45, 30, role="4th Line"),
    Skater("Yakov Trenin", 30, 20, 50, 70, role="4th Line"),
    Skater("Jakub Lauko", 20, 50, 30, 55, role="4th Line"),
    Skater("Liam Ohgren", 35, 35, 35, 35, role="bench"),
    Skater("Brock Faber", 45, 70, 40, 50, role="Top Pair"),
    Skater("Jonas Brodin", 55, 30, 50, 70, role="Top Pair"),
    Skater("Jared Spurgeon", 60, 50, 65, 85, role="2nd Pair"),
    Skater("Jake Middleton", 40, 40, 20, 40, role="2nd Pair"),
    Skater("Zach Bogosian", 30, 45, 45,45, role="3rd Pair"),
    Skater("Jon Merrill", 45, 40, 20, 50, role="3rd Pair")
]

canadiens_players = [
    Skater("Nick Suzuki", 70, 60, 55, 50, role="1st Line"),
    Skater("Cole Caufield", 65, 45, 60, 20, role="1st Line"),
    Skater("Juraj Slafkovsky", 55, 30, 55, 40, role="1st Line"),
    Skater("Patrik Laine", 80, 50, 50, 40, role="bench"),
    Skater("Kriby Dach", 50, 30, 35, 35, role="2nd Line"),
    Skater("Alex Newhook", 60, 50, 50, 30, role="2nd Line"),
    Skater("Josh Anderson", 20, 30, 60, 20, role="3rd Line"),
    Skater("Christian Dvorak", 35, 35, 35, 20, role="3rd Line"),
    Skater("Rafael Harvey-Pinard", 35, 50, 45, 65, role="3rd Line"),
    Skater("Brendan Gallagher", 20, 55, 60, 40, role="4th Line"),
    Skater("Joel Armia", 60, 30, 55, 60, role="2nd Line"),
    Skater("Jake Evans", 30, 60, 50, 60, role="4th Line"),
    Skater("Joshua Roy", 50, 60, 60, 60, role="4th Line"),
    Skater("Michael Pezzetta", 45, 55, 30, 45, role="bench"),
    Skater("Mike Matheson", 65, 70, 45,45, role="Number 1"),
    Skater("David Savard", 40, 50, 60, 20, role="Top Pair"),
    Skater("Kaiden Guhle", 60, 70, 20, 65, role="2nd Pair"),
    Skater("Justin Barron", 60, 55, 50, 30, role="2nd Pair"),
    Skater("Lane Hutson", 50, 40, 40, 45, role="3rd Pair"),
    Skater("Arber Xhekaj", 50, 50, 35, 30, role="3rd Pair")
]

predators_players = [
    Skater("Filip Forsberg", 85, 60, 70, 55, role="1st Line"),
    Skater("Ryan O'Reilly", 60, 45, 65, 65, role="1st Line"),
    Skater("Jonathan Marchessault", 70, 60, 65, 50, role="1st Line"),
    Skater("Gustav Nyquist", 60, 70, 45, 20, role="2nd Line"),
    Skater("Steven Stamkos", 80, 70, 45, 30, role="2nd Line"),
    Skater("Tommy Novak", 65, 55, 65, 20, role="2nd Line"),
    Skater("Colton Sissons", 30, 40, 55, 40, role="3rd Line"),
    Skater("Mark Jankowski", 50, 20, 40, 60, role="3rd Line"),
    Skater("Luke Evangelista", 50, 70, 60, 40, role="3rd Line"),
    Skater("Cole Smith", 20, 45, 40, 60, role="4th Line"),
    Skater("Michael McCarron", 45, 30, 45, 40, role="4th Line"),
    Skater("Phil Tomasino", 40, 60, 50, 40, role="4th Line"),
    Skater("Juuso Parssinen", 30, 30, 45, 35, role="bench"),
    Skater("Roman Josi", 85, 90, 80, 40, role="Number 1"),
    Skater("Brady Skjei", 70, 60, 40, 65, role="Top Pair"),
    Skater("Dante Fabbro", 35, 55, 50, 60, role="2nd Pair"),
    Skater("Alexandre Carrier", 20, 45, 50, 65, role="2nd Pair"),
    Skater("Jeremy Lauzon", 40, 20, 45, 50, role="3rd Pair"),
    Skater("Spencer Stastney", 60, 35, 65, 50, role="3rd Pair"),
    Skater("Luke Schenn", 40, 55, 30, 35, role="bench")
]

devils_players = [
    Skater("Jack Hughes", 70, 65, 80, 45, role="1st Line"),
    Skater("Nico Hischier", 55, 80, 80, 35, role="1st Line"),
    Skater("Jesper Bratt", 60, 80, 85, 30, role="1st Line"),
    Skater("Timo Meier", 70, 50, 70, 30, role="2nd Line"),
    Skater("Dawson Mercer", 60, 50, 60, 35, role="2nd Line"),
    Skater("Erik Haula", 40, 60, 60, 70, role="2nd Line"),
    Skater("Ondrej Palat", 50, 60, 65, 70, role="3rd Line"),
    Skater("Tomas Tatar", 50, 35, 60, 55, role="3rd Line"),
    Skater("Stefan Noesen", 20, 60, 65, 55, role="3rd Line"),
    Skater("Curtis Lazar", 30, 35, 40, 60, role="4th Line"),
    Skater("Nathan Bastian", 30, 30, 40, 40, role="4th Line"),
    Skater("Paul Cotter", 35, 35, 30, 20, role="4th Line"),
    Skater("Dougie Hamilton", 80, 60, 85, 35, role="Top Pair"),
    Skater("Jonas Siegenthaler", 30, 35, 20, 65, role="Top Pair"),
    Skater("Brett Pesce", 45, 40, 65, 55, role="2nd Pair"),
    Skater("Brenden Dillon", 50, 45, 45, 70, role="2nd Pair"),
    Skater("Johnathan Kovacevic", 60, 40, 55, 50, role="3rd Pair"),
    Skater("Simon Nemec", 20, 70, 70, 30, role="3rd Pair"),
    Skater("Luke Hughes", 65, 35, 60, 30, role="bench"),
    Skater("Kurtis MacDermid", 40, 40, 35, 30, role="bench"),
    Skater("Nick DeSimone", 50, 20, 50, 20, role="bench")
]

islanders_players = [
    Skater("Mat Barzal", 50, 85, 65, 30, role="1st Line"),
    Skater("Bo Horvat", 70, 60, 65, 50, role="1st Line"),
    Skater("Brock Nelson", 80, 60, 60, 30, role="1st Line"),
    Skater("Kyle Palmieri", 60, 50, 65, 35, role="2nd Line"),
    Skater("Anthony Duclair", 70, 70, 65, 20, role="2nd Line"),
    Skater("Maxim Tsyplakov", 50, 50, 40, 40, role="2nd Line"),
    Skater("Anders Lee", 55, 20, 70, 55, role="3rd Line"),
    Skater("JG Pageau", 35, 60, 55, 60, role="3rd Line"),
    Skater("Simon Holmstrom", 65, 30, 20, 65, role="3rd Line"),
    Skater("Casey Cizikas", 35, 30, 30, 60, role="4th Line"),
    Skater("Kyle MacLean", 50, 50, 30, 60, role="4th Line"),
    Skater("Oliver Wahlstrom", 35, 30, 35, 35, role="4th Line"),
    Skater("Hudson Fasching", 50, 55, 50, 60, role="bench"),
    Skater("Julien Gauthier", 50, 30, 35, 30, role="bench"),
    Skater("Pierre Engvall", 50, 50, 70, 70, role="bench"),
    Skater("Noah Dobson", 65, 80, 60, 35, role="Top Pair"),
    Skater("Ryan Pulock", 40, 40, 45, 55, role="Top Pair"),
    Skater("Adam Pelech", 35, 60, 35, 85, role="2nd Pair"),
    Skater("Alexander Romanov", 50, 50, 50, 35, role="2nd Pair"),
    Skater("Scott Mayfield", 40, 50, 30, 60, role="3rd Pair"),
    Skater("Mike Reilly", 35, 60, 60, 60, role="3rd Pair"),
    Skater("Samuel Bolduc", 55, 20, 40, 35, role="bench")
]

rangers_players = [
    Skater("Artemi Panarin", 85, 70, 80, 40, role="1st Line"),
    Skater("Mika Zibanejad", 70, 70, 40, 55, role="1st Line"),
    Skater("Vincent Trocheck", 50, 80, 70, 50, role="1st Line"),
    Skater("Chris Kreider", 70, 35, 70, 55, role="2nd Line"),
    Skater("Filip Chytil", 55, 50, 60, 45, role="2nd Line"),
    Skater("Alexis Lafreniere", 60, 50, 50, 30, role="2nd Line"),
    Skater("Kaapo Kakko", 60, 40, 45, 50, role="3rd Line"),
    Skater("Reilly Smith", 50, 65, 55, 50, role="3rd Line"),
    Skater("Will Cuylle", 50, 20, 40, 60, role="3rd Line"),
    Skater("Matt Rempe", 20, 20, 20, 40, role="4th Line"),
    Skater("Jimmy Vesey", 30, 30, 60, 70, role="4th Line"),
    Skater("Sam Carrick", 40, 30, 20, 30, role="4th Line"),
    Skater("Adam Edstrom", 40, 40, 40, 40, role="bench"),
    Skater("Adam Fox", 80, 80, 85, 70, role="Number 1"),
    Skater("K'Andre Miller", 60, 45, 35, 60, role="Top Pair"),
    Skater("Ryan Lindgren", 20, 60, 20, 60, role="2nd Pair"),
    Skater("Jacob Trouba", 30, 60, 55,35, role="2nd Pair"),
    Skater("Zachary Jones", 45, 40, 35, 30, role="3rd Pair"),
    Skater("Braden Schneider", 55, 40, 35, 40, role="3rd Pair"),
    Skater("Chad Ruhwedel", 35, 20, 40, 60, role="bench")
]

senators_players = [
    Skater("Tim Stuetzle", 50, 60, 60, 35, role="1st Line"),
    Skater("Claude Giroux", 65, 60, 70, 50, role="1st Line"),
    Skater("Brady Tkachuk", 50, 80, 85, 30, role="1st Line"),
    Skater("Drake Batherson", 60, 60, 50, 35, role="2nd Line"),
    Skater("Shane Pinto", 20, 40, 50, 70, role="2nd Line"),
    Skater("Josh Norris", 80, 20, 30, 40, role="2nd Line"),
    Skater("David Perron", 60, 55, 45, 50, role="3rd Line"),
    Skater("Ridley Greig", 50, 60, 65,60, role="3rd Line"),
    Skater("Michael Amadio", 60, 40, 45, 60, role="3rd Line"),
    Skater("Zack MacEwen", 30, 30,30,30, role="4th Line"),
    Skater("Noah Gregor", 20, 40, 45, 20, role="4th Line"),
    Skater("Nick Cousins", 30, 30, 50, 30, role="4th Line"),
    Skater("Jake Sanderson", 50, 50, 60, 65, role="Top Pair"),
    Skater("Thomas Chabot", 60, 40, 80, 35, role="Top Pair"),
    Skater("Artem Zub", 45, 50, 30, 70, role="2nd Pair"),
    Skater("Nick Jensen", 40, 65, 45, 60, role="2nd Pair"),
    Skater("Travis Hamonic", 55, 35, 35, 20, role="3rd Pair"),
    Skater("Jacob Bernard-Docker", 45, 30, 20, 55, role="3rd Pair")
]

flyers_players = [
    Skater("Travis Konecny", 60, 70, 70, 20, role="1st Line"),
    Skater("Owen Tippett", 60, 60, 70, 30, role="1st Line"),
    Skater("Tyson Foerster", 50, 20, 50, 80, role="1st Line"),
    Skater("Matvei Michkov", 60, 50, 60, 30, role="2nd Line"),
    Skater("Sean Couturier", 20, 50, 60, 60, role="2nd Line"),
    Skater("Joel Farabee", 60, 60, 60, 30, role="2nd Line"),
    Skater("Scott Laughton", 40, 30,55,20, role="3rd Line"),
    Skater("Morgan Frost", 30, 60, 60, 60, role="3rd Line"),
    Skater("Noah Cates", 30, 40, 60, 70, role="3rd Line"),
    Skater("Garnet Hathaway", 40, 30, 50, 70, role="4th Line"),
    Skater("Ryan Poehling", 40, 50, 60, 40, role="4th Line"),
    Skater("Bobby Brink", 50, 60, 30, 40, role="4th Line"),
    Skater("Nicolas Deslauriers", 30, 20, 20, 45, role="bench"),
    Skater("Travis Sanheim", 40, 60, 60, 45, role="Number 1"),
    Skater("Cam York", 50, 50, 60, 60, role="Top Pair"),
    Skater("Nick Seeler", 35, 50, 50, 60, role="2nd Pair"),
    Skater("Jamie Drysdale", 45, 40, 30, 20, role="2nd Pair"),
    Skater("Erik Johnson", 50, 30, 55, 30, role="3rd Pair"),
    Skater("Rasmus Ristolainen", 20, 30, 60, 60, role="3rd Pair")
]

penguins_players = [
    Skater("Sidney Crosby", 65, 80, 85, 45, role="1st Line"),
    Skater("Evgeni Malkin", 65, 70, 70, 35, role="1st Line"),
    Skater("Bryan Rust", 55, 50, 60, 40, role="1st Line"),
    Skater("Rickard Rakell", 40, 30, 60, 50, role="2nd Line"),
    Skater("Michael Bunting", 45, 70, 60, 20, role="2nd Line"),
    Skater("Drew O'Connor", 35, 40, 55, 35, role="2nd Line"),
    Skater("Lars Eller", 40, 35, 35, 70, role="3rd Line"),
    Skater("Kevin Hayes", 50, 55, 55, 40, role="3rd Line"),
    Skater("Cody Glass", 20, 30, 30, 50, role="3rd Line"),
    Skater("Noel Acciari", 30, 20, 45, 60, role="4th Line"),
    Skater("Blake Lizotte", 40, 60, 45, 60, role="4th Line"),
    Skater("Anthony Beauvilier", 20, 45, 40, 30, role="4th Line"),
    Skater("Jesse Puljujarvi", 20, 30, 45, 60, role="bench"),
    Skater("Erik Karlsson", 60, 90, 90, 20, role="Number 1"),
    Skater("Kris Letang", 70, 60, 60, 35, role="Top Pair"),
    Skater("Marcus Pettersson", 20, 70, 65, 70, role="2nd Pair"),
    Skater("Ryan Graves", 55, 35, 55, 40, role="2nd Pair"),
    Skater("Matt Grzelyck", 45, 60, 35, 30, role="3rd Pair"),
    Skater("Sebastian Aho", 55, 30, 50, 45, role="3rd Pair")
]

sharks_players = [
    Skater("Macklin Celebrini", 50, 50, 40, 30, role="1st Line"),
    Skater("William Eklund", 45, 40, 45, 50, role="1st Line"),
    Skater("Tyler Toffoli", 65, 50, 65, 50, role="1st Line"),
    Skater("Mikael Granlund", 30, 50, 50, 20, role="2nd Line"),
    Skater("Fabian Zetterlund", 50, 55, 50, 20, role="2nd Line"),
    Skater("Alexander Wennberg", 40, 50, 30, 65, role="2nd Line"),
    Skater("Will Smith", 50, 30, 40, 30, role="3rd Line"),
    Skater("Thomas Bordeleau", 50, 35, 45, 30, role="3rd Line"),
    Skater("Luke Kunin", 35, 30, 20, 20, role="3rd Line"),
    Skater("Nico Sturm", 40, 40, 45, 35, role="4th Line"),
    Skater("Barclay Goodrow", 40, 45, 30, 35, role="4th Line"),
    Skater("Ty Dellandrea", 20, 50, 30, 60, role="4th Line"),
    Skater("Klim Kostin", 60, 45, 20, 45, role="bench"),
    Skater("Logan Couture", 40, 50, 50, 30, role="bench"),
    Skater("Carl Grundstrom", 55, 30, 55, 50, role="bench"),
    Skater("Mario Ferraro", 20, 35, 40, 35, role="Top Pair"),
    Skater("Cody Ceci", 45, 30, 35, 30, role="Top Pair"),
    Skater("Jan Rutta", 45, 20, 20, 50, role="2nd Pair"),
    Skater("Jake Walman", 65, 20, 55, 55, role="2nd Pair"),
    Skater("Matt Benning", 20, 60, 30, 45, role="3rd Pair"),
    Skater("Marc-Eduoard Vlassic", 50, 30, 55, 40, role="3rd Pair")
]

kraken_players = [
    Skater("Jared McCann", 80, 60, 60, 55, role="1st Line"),
    Skater("Matty Beniers", 60, 55, 20, 80, role="1st Line"),
    Skater("Jordan Eberle", 50, 70, 80, 45, role="1st Line"),
    Skater("Yanni Gourde", 30, 60, 60, 60, role="2nd Line"),
    Skater("Oliver Bjorkstrand", 55, 55, 60, 50, role="2nd Line"),
    Skater("Chandler Stephenson", 55, 70, 35, 30, role="2nd Line"),
    Skater("Eeli Tolvanen", 55, 45, 30, 60, role="3rd Line"),
    Skater("Andre Burakovsky", 60, 60, 50, 20, role="3rd Line"),
    Skater("Jaden Schwartz", 30, 50, 50, 65, role="3rd Line"),
    Skater("Brandon Tanev", 35, 40, 30, 60, role="4th Line"),
    Skater("Shane Wright", 30, 50,40,40, role="4th Line"),
    Skater("Tye Kartye", 50, 30, 45, 40, role="4th Line"),
    Skater("Vince Dunn", 80, 65, 80, 40, role="Top Pair"),
    Skater("Adam Larsson", 55, 50, 20, 45, role="Top Pair"),
    Skater("Jamie Oleksiak", 40, 45, 70, 55, role="2nd Pair"),
    Skater("Brandon Montour", 65, 50, 60, 35, role="2nd Pair"),
    Skater("William Borgen", 40, 60, 45, 50, role="3rd Pair"),
    Skater("Ryker Evans", 20, 50, 20, 80, role="3rd Pair"),
    Skater("Josh Mahura", 35, 55, 30, 50, role="3rd Pair")
]

blues_players = [
    Skater("Robert Thomas", 65, 85, 70, 30, role="1st Line"),
    Skater("Jordan Kyrou", 80, 65, 60, 50, role="1st Line"),
    Skater("Pavel Buchnevich", 70, 60, 70, 65, role="1st Line"),
    Skater("Brayden Schenn", 60, 60, 35, 30, role="2nd Line"),
    Skater("Jake Neighbours", 70, 20, 35, 30, role="2nd Line"),
    Skater("Brandon Saad", 65, 50, 60, 30, role="2nd Line"),
    Skater("Radek Faksa", 30, 40, 20, 65, role="3rd Line"),
    Skater("Mathieu Joseph", 45, 65, 35, 60, role="3rd Line"),
    Skater("Dylan Holloway", 40, 20, 30, 50, role="3rd Line"),
    Skater("Alexey Toropchenko", 55, 30, 30, 50, role="4th Line"),
    Skater("Oskar Sundqvist", 35, 45, 30, 30, role="4th Line"),
    Skater("Alexandre Texier", 55, 50, 50, 30, role="4th Line"),
    Skater("Kasperi Kapanen", 35, 55, 40, 30, role="bench"),
    Skater("Colton Parayko", 60, 35, 20, 70, role="Top Pair"),
    Skater("Nick Leddy", 35, 60, 60, 35, role="Top Pair"),
    Skater("Justin Faulk", 60, 70, 50, 35, role="2nd Pair"),
    Skater("Philip Broberg", 30, 55, 55, 40, role="2nd Pair"),
    Skater("Ryan Suter", 35, 40, 45, 60, role="3rd Pair"),
    Skater("Scott Perunovich", 20, 60, 50, 35, role="3rd Pair"),
    Skater("Torey Krug", 30, 60, 55, 20, role="bench")
]

lightning_players = [
    Skater("Nikita Kucherov", 70, 85, 85, 30, role="1st Line"),
    Skater("Brayden Point", 90, 60, 80, 30, role="1st Line"),
    Skater("Jake Guentzel", 40, 70, 85, 20, role="1st Line"),
    Skater("Brandon Hagel", 60, 65, 65, 65, role="2nd Line"),
    Skater("Anthony Cirelli", 50, 55, 60, 80, role="2nd Line"),
    Skater("Nicholas Paul", 60, 35, 30, 80, role="2nd Line"),
    Skater("Conor Sheary", 45, 60, 50, 30, role="3rd Line"),
    Skater("Mikey Eyssimont", 30, 40, 60, 60, role="3rd Line"),
    Skater("Cam Atkinson", 30, 45, 40, 20, role="3rd Line"),
    Skater("Zemgus Girgensons", 45, 20, 40, 50, role="4th Line"),
    Skater("Luke Glendening", 35, 20, 20, 55, role="4th Line"),
    Skater("Mitchell Chaffee", 50, 20, 35, 35, role="4th Line"),
    Skater("Victor Hedman", 65, 80, 70, 35, role="Number 1"),
    Skater("Erik Cernak", 35, 50, 35, 60, role="Top Pair"),
    Skater("Ryan McDonagh", 30, 60, 70, 60, role="2nd Pair"),
    Skater("Darren Raddysh", 55, 35, 35, 60, role="2nd Pair"),
    Skater("JJ Moser", 55, 60, 50, 40, role="3rd Pair"),
    Skater("Nick Perbix", 45, 60, 40, 60, role="3rd Pair")
]

leafs_players = [
    Skater("Auston Matthews", 90, 70, 90, 60, role="1st Line"),
    Skater("William Nylander", 70, 65, 80,20, role="1st Line"),
    Skater("Mitch Marner", 70, 90, 60, 60, role="1st Line"),
    Skater("John Tavares", 55, 55, 70, 55, role="2nd Line"),
    Skater("Matthew Knies", 55, 60, 40, 60, role="2nd Line"),
    Skater("Max Domi", 35, 85, 65, 20, role="2nd Line"),
    Skater("Nicholas Robertson", 65, 55, 45, 40, role="3rd Line"),
    Skater("Max Pacioretty", 50, 50, 60, 30, role="3rd Line"),
    Skater("Pontus Holmberg", 50, 60, 35, 60, role="3rd Line"),
    Skater("David Kampf", 40, 30, 20, 55, role="4th Line"),
    Skater("Connor Dewar", 35, 35, 35, 70, role="4th Line"),
    Skater("Bobby McMann", 55, 30, 45, 60, role="4th Line"),
    Skater("Ryan Reaves", 35, 30, 30, 40, role="bench"),
    Skater("Steven Lorentz", 30, 20, 50, 50, role="bench"),
    Skater("Calle Jarnkrok", 60, 45, 50, 45, role="bench"),
    Skater("Morgan Rielly", 40, 85, 60, 20, role="Number 1"),
    Skater("Chris Tanev", 40, 50, 60, 90, role="Top Pair"),
    Skater("Oliver Ekman-Larsson", 60, 60, 55, 35, role="2nd Pair"),
    Skater("Jake McCabe", 55, 60, 60, 60, role="2nd Pair"),
    Skater("Simon Benoit", 30, 20, 20, 45, role="3rd Pair"),
    Skater("Timothy Liljgren", 60, 35, 60, 60, role="3rd Pair"),
    Skater("Conor Timmins", 45, 65, 60, 50, role="bench")
]

utah_players = [
    Skater("Clayton Keller", 80, 70, 60, 30, role="1st Line"),
    Skater("Barrett Hayton", 20, 30, 60, 65, role="1st Line"),
    Skater("Nick Schmaltz", 65, 65, 60, 40, role="1st Line"),
    Skater("Lawson Crouse", 60, 50, 60, 45, role="2nd Line"),
    Skater("Logan Cooley", 60, 55, 50, 50, role="2nd Line"),
    Skater("Dylan Guenther", 70, 45, 35, 40, role="2nd Line"),
    Skater("Mattias Maccelli", 50, 60, 60, 55, role="3rd Line"),
    Skater("Josh Doan", 40, 40, 40, 40, role="3rd Line"),
    Skater("Nick Bjugstad", 60, 35, 60, 45, role="3rd Line"),
    Skater("Alex Kerfoot", 30, 65, 30, 60, role="4th Line"),
    Skater("Jack McBain", 45, 60, 55, 30, role="4th Line"),
    Skater("Kevin Stenlund", 35, 30, 30, 60, role="4th Line"),
    Skater("Michael Carcone", 70, 20, 45, 20, role="bench"),
    Skater("Mikhail Sergachev", 50, 65, 60, 50, role="Number 1"),
    Skater("Sean Durzi", 55, 50, 50, 40, role="Top Pair"),
    Skater("John Marino", 30, 60, 30, 65, role="2nd Pair"),
    Skater("Juuso Valimaki", 20, 50, 65, 70, role="2nd Pair"),
    Skater("Ian Cole", 35, 40, 55, 70, role="3rd Pair"),
    Skater("Michael Kesselring", 50, 50, 50, 30, role="3rd Pair")
]

canucks_players = [
    Skater("Elias Pettersson", 70, 80, 70, 60, role="1st Line"),
    Skater("JT Miller", 80, 65, 60, 50, role="1st Line"),
    Skater("Jake DeBrusk", 60, 50, 70, 60, role="1st Line"),
    Skater("Brock Boeser", 60, 60, 40, 30, role="2nd Line"),
    Skater("Conor Garland", 60, 60, 60, 70, role="2nd Line"),
    Skater("Daniel Sprong", 60, 60, 60, 30, role="2nd Line"),
    Skater("Pius Suter", 55, 40, 50, 80, role="3rd Line"),
    Skater("Nils Hoglander", 65, 55, 60, 60, role="3rd Line"),
    Skater("Dakota Joshua", 60, 45, 60, 45, role="3rd Line"),
    Skater("Teddy Blueger", 20, 60, 60, 60, role="4th Line"),
    Skater("Danton Heinen", 55, 60, 60, 55, role="4th Line"),
    Skater("Kieffer Sherwood", 55, 55, 45, 50, role="4th Line"),
    Skater("Nils Aman", 30, 40, 20, 60, role="bench"),
    Skater("Phil Di Gisueppe", 45, 30, 45, 50, role="bench"),
    Skater("Quinn Hughes", 60, 70, 70, 60, role="Number 1"),
    Skater("Filip Hronek", 30, 60, 45, 40, role="Top Pair"),
    Skater("Carson Soucy", 60, 30, 35, 60, role="2nd Pair"),
    Skater("Tyler Myers", 30, 60, 50, 50, role="2nd Pair"),
    Skater("Derek Forbort", 45, 40, 30, 60, role="3rd Pair"),
    Skater("Vincent Desharnais", 30, 35, 45, 55, role="3rd Pair"),
    Skater("Mark Friedman", 20, 20, 50, 50, role="bench"),
    Skater("Erik Brannstrom", 20, 50, 60, 60, role="bench")
]

knights_players = [
    Skater("Jack Eichel", 80, 60, 60, 70, role="1st Line"),
    Skater("Mark Stone", 60, 70, 80, 80, role="1st Line"),
    Skater("Tomas Hertl", 50, 60, 65, 35, role="1st Line"),
    Skater("William Karlsson", 60, 60, 65, 70, role="2nd Line"),
    Skater("Ivan Barbashev", 60, 65, 60, 20, role="2nd Line"),
    Skater("Victor Olofsson", 60, 35, 30, 30, role="2nd Line"),
    Skater("Brett Howden", 40, 40, 35, 35, role="3rd Line"),
    Skater("Alexander Holtz", 55, 40, 40, 30, role="3rd Line"),
    Skater("Pavel Dorofeyev", 60, 40, 50, 60, role="3rd Line"),
    Skater("Keegan Kolesar", 40, 50, 40, 50, role="4th Line"),
    Skater("Jonas Rondbjerg", 20, 45, 20, 60, role="4th Line"),
    Skater("Nicolas Roy", 35, 60, 55, 60, role="4th Line"),
    Skater("Alex Pietrangelo", 60, 60, 80, 35, role="Top Pair"),
    Skater("Noah Hanafin", 60, 60, 65, 50, role="Top Pair"),
    Skater("Shea Theodore", 60, 85, 70, 20, role="Top Pair"),
    Skater("Brayden McNabb", 30, 45, 50, 80, role="2nd Pair"),
    Skater("Nick Hague", 30, 35, 50, 50, role="3rd Pair"),
    Skater("Zach Whitecloud", 55, 45, 40, 60, role="3rd Pair")
]

capitals_players = [
    Skater("Alexander Ovechkin", 70, 55, 60, 20, role="1st Line"),
    Skater("Tom Wilson", 45, 35, 45, 65, role="1st Line"),
    Skater("Dylan Strome", 55, 60, 70, 60, role="1st Line"),
    Skater("Pierre-Luc Dubois", 30, 55, 65, 35, role="2nd Line"),
    Skater("Andrew Mangiapane", 45, 60, 70, 35, role="2nd Line"),
    Skater("Connor McMichael", 45, 50, 45, 35, role="2nd Line"),
    Skater("Sonny Milano", 50, 50, 60, 65, role="3rd Line"),
    Skater("Hendrix Lapierre", 60, 30, 35, 35, role="3rd Line"),
    Skater("Taylor Raddysh", 30, 20, 40, 60, role="3rd Line"),
    Skater("Nic Dowd", 60, 50, 40, 70, role="4th Line"),
    Skater("Aliaksi Protas", 20, 55, 55, 60, role="4th Line"),
    Skater("Brandon Duhaime", 35, 35, 50, 40, role="4th Line"),
    Skater("TJ Oshie", 45, 30, 30, 30, role="bench"),
    Skater("John Carlson", 60, 60, 85, 35, role="Number 1"),
    Skater("Jakob Chychrun", 65, 55, 50, 40, role="Top Pair"),
    Skater("Matt Roy", 35, 55, 65, 80, role="2nd Pair"),
    Skater("Rasmus Sandin", 50, 55, 50, 30, role="2nd Pair"),
    Skater("Trevor Van Riemsdyk", 30, 45, 55, 70, role="3rd Pair"),
    Skater("Martin Fehervary", 45, 35, 35, 60, role="3rd Pair"),
    Skater("Ethan Bear", 35, 30, 35, 45, role="bench")
]

jets_players = [
    Skater("Kyle Connor", 80, 45, 60, 20, role="1st Line"),
    Skater("Mark Scheifele", 70, 60, 65, 20, role="1st Line"),
    Skater("Gabriel Vilardi", 70, 50, 45, 50, role="1st Line"),
    Skater("Cole Perfetti", 50, 65, 30, 60, role="2nd Line"),
    Skater("Nikolai Ehlers", 60, 80, 80, 40, role="2nd Line"),
    Skater("Alex Iafallo", 35, 50, 45, 80, role="2nd Line"),
    Skater("Nino Niederreiter", 60, 40, 60, 60, role="3rd Line"),
    Skater("Mason Appleton", 45, 40, 60, 35, role="3rd Line"),
    Skater("Adam Lowry", 30, 40, 65, 70, role="3rd Line"),
    Skater("Vladislav Namestnikov", 35, 50, 50, 60, role="4th Line"),
    Skater("Morgan Barron", 35, 30, 45, 45, role="4th Line"),
    Skater("Rasmus Kupari", 20, 45, 30, 55, role="4th Line"),
    Skater("Josh Morrissey", 65, 80, 85, 40, role="Number 1"),
    Skater("Dylan DeMelo", 30, 60, 30, 80, role="Top Pair"),
    Skater("Neal Pionk", 45, 45, 35, 30, role="2nd Pair"),
    Skater("Dylan Samberg", 35, 55, 45, 55, role="2nd Pair"),
    Skater("Logan Stanley", 35, 30, 45, 35, role="3rd Pair"),
    Skater("Colin Miller", 60, 50, 30, 45, role="3rd Pair")
]
