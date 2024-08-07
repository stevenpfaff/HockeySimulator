class Goalie:
    def __init__(self, name, rating, games=0, shots_against=0, saves=0, goals_allowed=0, wins=0, losses=0, shutouts=0):
        self.name = name
        self.rating = rating
        self.games = games
        self.shots = shots_against
        self.saves = saves
        self.goals = goals_allowed
        self.wins = wins
        self.losses = losses
        self.shutouts = shutouts

goalies = {
    "gibson": Goalie("John Gibson", 40),
    "pickard": Goalie("Calvin Pickard", 30),
    "brossoit": Goalie("Laurent Brossoit", 50),
    "desmith": Goalie("Casey DeSmith", 50),
    "dostal": Goalie("Lukas Dostal", 30),
    "stolarz": Goalie("Anthony Stolarz", 40),
    "ullmark": Goalie("Linus Ullmark", 60),
    "swayman": Goalie("Jeremy Swayman", 70),
    "luukkonen": Goalie("Ukko-Pekka Luukkonen", 50),
    "comrie": Goalie("Eric Comrie", 40),
    "markstrom": Goalie("Jacob Markstrom", 50),
    "vladar": Goalie("Dan Vladar", 30),
    "andersen": Goalie("Frederik Andersen", 60),
    "kochetkov": Goalie("Pyotr Kochetkov", 50),
    "mrazek": Goalie("Petr Mrazek", 40),
    "soderblom": Goalie("Arvid Soderblom", 20),
    "georgiev": Goalie("Alexandar Georgiev", 50),
    "annunen": Goalie("Justus Annunen", 50),
    "merzlikins": Goalie("Elvis Merzlikins", 40),
    "tarasov": Goalie("Daniil Tarasov", 30),
    "oettinger": Goalie("Jake Oettinger", 60),
    "wedgewood": Goalie("Scott Wedgewood", 40),
    "husso": Goalie("Ville Husso", 50),
    "lyon": Goalie("Alex Lyon", 40),
    "skinner": Goalie("Stuart Skinner", 50),
    "campbell": Goalie("Jack Campbell", 40),
    "bobrovsky": Goalie("Sergei Bobrovsky", 70),
    "knight": Goalie("Spencer Knight", 50),
    "talbot": Goalie("Cam Talbot", 60),
    "copley": Goalie("Phoenix Copley", 40),
    "gustavsson": Goalie("Filip Gustavsson", 40),
    "fleury": Goalie("Marc-Andre Fleury", 40),
    "allen": Goalie("Jake Allen", 40),
    "primeau": Goalie("Caiden Primeau", 30),
    "montembeault": Goalie("Sam Montembeault", 30),
    "saros": Goalie("Juuse Saros", 60),
    "askarov": Goalie("Yaroslav Askarov", 50),
    "lankinen": Goalie("Kevin Lankinen", 40),
    "vanacek": Goalie("Vitek Vanecek", 30),
    "schmid": Goalie("Akira Schmid", 20),
    "sorokin": Goalie("Ilya Sorokin", 60),
    "varlamov": Goalie("Semyon Varlamov", 50),
    "shesterkin": Goalie("Igor Shesterkin", 80),
    "halak": Goalie("Jaroslav Halak", 50),
    "korp": Goalie("Joonas Korpisalo", 30),
    "forsberg": Goalie("Anton Forsberg", 30),
    "hart": Goalie("Carter Hart", 50),
    "ersson": Goalie("Samuel Ersson", 20),
    "fedotov": Goalie("Ivan Fedotov", 30),
    "jarry": Goalie("Tristan Jarry", 50),
    "ned": Goalie("Alex Nedelkovich", 30),
    "kahkonen": Goalie("Kaapo Kahkonen", 20),
    "blackwood": Goalie("Mackenzie Blackwood", 30),
    "grubauer": Goalie("Philipp Grubauer", 40),
    "daccord": Goalie("Joey Daccord", 50),
    "binner": Goalie("Jordan Binnington", 60),
    "hofer": Goalie("Joel Hofer", 30),
    "vasy": Goalie("Andrei Vasilevskiy", 60),
    "elliott": Goalie("Brian Elliott", 30),
    "samsonov": Goalie("Ilya Samsonov", 40),
    "woll": Goalie("Joeseph Woll", 50),
    "vemelka": Goalie("Karel Vejmelka", 50),
    "ingram": Goalie("Connor Ingram", 40),
    "demko": Goalie("Thatcher Demko", 60),
    "delia": Goalie("Collin Delia", 40),
    "thompson": Goalie("Logan Thompson", 50),
    "hill": Goalie("Adin Hill", 60),
    "kuemper": Goalie("Darcy Kuemper", 40),
    "lindgren": Goalie("Charlie Lindgren", 50),
    "hellebuyck": Goalie("Connor Hellebuyck", 80),
    "rittich": Goalie("David Rittich", 40),
    "quick": Goalie("Jonathan Quick", 40),
    "cooley": Goalie("Devin Cooley", 30),
    "johansson": Goalie("Jonas Johansson", 30),
    "jones": Goalie("Martin Jones", 40),
    "silvos": Goalie("Arturs Silovs", 40),
    "levi": Goalie("Devon Levi", 50),
    "wolf": Goalie("Dustin Wolf", 40)
}