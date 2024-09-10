class Goalie:
    def __init__(self, name, rating, games=0, shots_against=0, saves=0, goals_allowed=0, wins=0, losses=0, shutouts=0):
        self.name = name
        self.rating = rating
        self.games = games
        self.shots_against = shots_against
        self.saves = saves
        self.goals_allowed = goals_allowed
        self.wins = wins
        self.losses = losses
        self.shutouts = shutouts


goalies = {
    # Ducks
    "gibson": Goalie("John Gibson", 45),
    "dostal": Goalie("Lukas Dostal", 40),
    # Bruins
    "swayman": Goalie("Jeremy Swayman", 70),
    "korp": Goalie("Joonas Korpisalo", 30),
    # Sabres
    "luukkonen": Goalie("Ukko-Pekka Luukkonen", 55),
    "levi": Goalie("Devon Levi", 40),
    # Flames
    "wolf": Goalie("Dustin Wolf", 30),
    "vladar": Goalie("Dan Vladar", 30),
    "cooley": Goalie("Devin Cooley", 30),
    # Hurricanes
    "andersen": Goalie("Frederik Andersen", 60),
    "kochetkov": Goalie("Pyotr Kochetkov", 50),
    # Blackhawks
    "mrazek": Goalie("Petr Mrazek", 40),
    "brossoit": Goalie("Laurent Brossoit", 55),
    "soderblom": Goalie("Arvid Soderblom", 20),
    # Avalanche
    "georgiev": Goalie("Alexandar Georgiev", 55),
    "annunen": Goalie("Justus Annunen", 50),
    # Blue Jackets
    "merzlikins": Goalie("Elvis Merzlikins", 40),
    "tarasov": Goalie("Daniil Tarasov", 30),
    # Stars
    "oettinger": Goalie("Jake Oettinger", 60),
    "desmith": Goalie("Casey DeSmith", 50),
    # Red Wings
    "talbot": Goalie("Cam Talbot", 55),
    "husso": Goalie("Ville Husso", 45),
    "lyon": Goalie("Alex Lyon", 40),
    "campbell": Goalie("Jack Campbell", 40),
    # Oilers
    "skinner": Goalie("Stuart Skinner", 60),
    "pickard": Goalie("Calvin Pickard", 40),
    "delia": Goalie("Collin Delia", 40),
    # Panthers
    "bobrovsky": Goalie("Sergei Bobrovsky", 70),
    "knight": Goalie("Spencer Knight", 50),
    # Kings
    "kuemper": Goalie("Darcy Kuemper", 60),
    "rittich": Goalie("David Rittich", 40),
    "copley": Goalie("Phoenix Copley", 40),
    # Wild
    "fleury": Goalie("Marc-Andre Fleury", 50),
    "gustavsson": Goalie("Filip Gustavsson", 50),
    # Canadiens
    "primeau": Goalie("Caiden Primeau", 50),
    "montembeault": Goalie("Sam Montembeault", 50),
    # Predators
    "saros": Goalie("Juuse Saros", 70),
    "wedgewood": Goalie("Scott Wedgewood", 40),
    # Devils
    "markstrom": Goalie("Jacob Markstrom", 60),
    "allen": Goalie("Jake Allen", 50),
    # Islanders
    "sorokin": Goalie("Ilya Sorokin", 70),
    "varlamov": Goalie("Semyon Varlamov", 60),
    # Rangers
    "shesterkin": Goalie("Igor Shesterkin", 80),
    "quick": Goalie("Jonathan Quick", 50),
    # Senators
    "ullmark": Goalie("Linus Ullmark", 70),
    "forsberg": Goalie("Anton Forsberg", 40),
    # Flyers
    "fedotov": Goalie("Ivan Fedotov", 50),
    "ersson": Goalie("Samuel Ersson", 40),
    # Penguins
    "jarry": Goalie("Tristan Jarry", 60),
    "ned": Goalie("Alex Nedelkovich", 45),
    # Sharks
    "askarov": Goalie("Yaroslav Askarov", 40),
    "blackwood": Goalie("Mackenzie Blackwood", 40),
    "vanacek": Goalie("Vitek Vanecek", 40),
    # Kraken
    "daccord": Goalie("Joey Daccord", 55),
    "grubauer": Goalie("Philipp Grubauer", 40),
    # Blues
    "binner": Goalie("Jordan Binnington", 60),
    "hofer": Goalie("Joel Hofer", 30),
    # Lightning
    "vasy": Goalie("Andrei Vasilevskiy", 70),
    "johansson": Goalie("Jonas Johansson", 20),
    # Leafs
    "stolarz": Goalie("Anthony Stolarz", 55),
    "woll": Goalie("Joeseph Woll", 40),
    # Utah
    "vemelka": Goalie("Karel Vejmelka", 40),
    "ingram": Goalie("Connor Ingram", 55),
    # Canucks
    "demko": Goalie("Thatcher Demko", 60),
    "silvos": Goalie("Arturs Silovs", 40),
    # Golden Knights
    "hill": Goalie("Adin Hill", 55),
    "samsonov": Goalie("Ilya Samsonov", 45),
    "schmid": Goalie("Akira Schmid", 20),
    # Capitals
    "thompson": Goalie("Logan Thompson", 55),
    "lindgren": Goalie("Charlie Lindgren", 55),
    # Jets
    "hellebuyck": Goalie("Connor Hellebuyck", 90),
    "kahkonen": Goalie("Kaapo Kahkonen", 40),
    "comrie": Goalie("Eric Comrie", 40),

    # Free Agents
    "lankinen": Goalie("Kevin Lankinen", 40),
    "halak": Goalie("Jaroslav Halak", 50),
    "hart": Goalie("Carter Hart", 50),
    "elliott": Goalie("Brian Elliott", 30),
    "jones": Goalie("Martin Jones", 40)
}