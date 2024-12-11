class Goalie:
    def __init__(self, name, rating, role=None, games=0, shots_against=0, saves=0, goals_allowed=0, wins=0, losses=0, shutouts=0):
        self.name = name
        self.rating = rating
        self.role = role or "Third"
        self.games = games
        self.shots_against = shots_against
        self.saves = saves
        self.goals_allowed = goals_allowed
        self.wins = wins
        self.losses = losses
        self.shutouts = shutouts


goalies = {
    # Ducks
    "gibson": Goalie("John Gibson", 40, "1A"),
    "dostal": Goalie("Lukas Dostal", 55, "1B"),
    "reimer": Goalie("James Reimer", 40, "Third"),
    # Bruins
    "swayman": Goalie("Jeremy Swayman", 60, "Starter"),
    "korp": Goalie("Joonas Korpisalo", 30, "Backup"),
    # Sabres
    "luukkonen": Goalie("Ukko-Pekka Luukkonen", 55, "Starter"),
    "levi": Goalie("Devon Levi", 40, "Backup"),
    # Flames
    "wolf": Goalie("Dustin Wolf", 55, "1A"),
    "vladar": Goalie("Dan Vladar", 45, "1B"),
    "cooley": Goalie("Devin Cooley", 30, "Third"),
    # Hurricanes
    "andersen": Goalie("Frederik Andersen", 60, "1A"),
    "kochetkov": Goalie("Pyotr Kochetkov", 50, "1B"),
    "martin": Goalie("Spencer Martin", 30, "Third"),
    # Blackhawks
    "mrazek": Goalie("Petr Mrazek", 55, "1A"),
    "brossoit": Goalie("Laurent Brossoit", 55, "1B"),
    "soderblom": Goalie("Arvid Soderblom", 30, "Third"),
    # Avalanche
    "georgiev": Goalie("Alexandar Georgiev", 55, "Starter"),
    "annunen": Goalie("Justus Annunen", 50, "Backup"),
    # "blackwoodcol": Goalie("Mackenzie Blackwood", 55, "Third"),
    "kahkonen": Goalie("Kaapo Kahkonen", 40, "Third"),
    # "wedgewoodcol": Goalie("Scott Wedgewood", 40, "Third"),
    # Blue Jackets
    "merzlikins": Goalie("Elvis Merzlikins", 45, "Starter"),
    "tarasov": Goalie("Daniil Tarasov", 40, "Backup"),
    # Stars
    "oettinger": Goalie("Jake Oettinger", 60, "Starter"),
    "desmith": Goalie("Casey DeSmith", 50, "Backup"),
    # Red Wings
    "talbot": Goalie("Cam Talbot", 60, "1A"),
    "husso": Goalie("Ville Husso", 40, "1B"),
    "lyon": Goalie("Alex Lyon", 50, "Backup"),
    "campbell": Goalie("Jack Campbell", 40),
    # Oilers
    "skinner": Goalie("Stuart Skinner", 55, "Starter"),
    "pickard": Goalie("Calvin Pickard", 45, "Backup"),
    # Panthers
    "bobrovsky": Goalie("Sergei Bobrovsky", 65, "Starter"),
    "knight": Goalie("Spencer Knight", 50, "1B"),
    # Kings
    "kuemper": Goalie("Darcy Kuemper", 60, "Starter"),
    "rittich": Goalie("David Rittich", 45, "Backup"),
    "copley": Goalie("Erik Portillo", 40, "Third"),
    # Wild
    "fleury": Goalie("Marc-Andre Fleury", 50, "Backup"),
    "gustavsson": Goalie("Filip Gustavsson", 60, "Starter"),
    # Canadiens
    "primeau": Goalie("Cayden Primeau", 45, "Backup"),
    "montembeault": Goalie("Sam Montembeault", 55, "Starter"),
    # Predators
    "saros": Goalie("Juuse Saros", 70, "Starter"),
    # "annunennsh": Goalie("Justus Annunen", 45, "Third"),
    "wedgewood": Goalie("Scott Wedgewood", 40, "Backup"),
    # Devils
    "markstrom": Goalie("Jacob Markstrom", 60, "Starter"),
    "allen": Goalie("Jake Allen", 50, "1B"),
    # Islanders
    "sorokin": Goalie("Ilya Sorokin", 70, "Starter"),
    "varlamov": Goalie("Semyon Varlamov", 55, "1B"),
    # Rangers
    "shesterkin": Goalie("Igor Shesterkin", 80, "Starter"),
    "quick": Goalie("Jonathan Quick", 50, "Backup"),
    # Senators
    "ullmark": Goalie("Linus Ullmark", 65, "Starter"),
    "forsberg": Goalie("Anton Forsberg", 40, "Backup"),
    "sogaard": Goalie("Mads Sogaard", 30, "Third"),
    # Flyers
    "fedotov": Goalie("Ivan Fedotov", 40, "1B"),
    "ersson": Goalie("Samuel Ersson", 50, "1A"),
    "kolosov": Goalie("Aleksei Kolosov", 30, "Third"),
    # Penguins
    "jarry": Goalie("Tristan Jarry", 55, "Starter"),
    "ned": Goalie("Alex Nedeljkovic", 40, "Backup"),
    "blomqvist": Goalie("Joel Blomqvist", 50, "Third"),
    # Sharks
    "askarov": Goalie("Yaroslav Askarov", 40, "Third"),
    "blackwood": Goalie("Mackenzie Blackwood", 50, "1A"),
    "vanacek": Goalie("Vitek Vanecek", 50, "1B"),
    # "georgievsj": Goalie("Alexandar Georgiev", 45, "Third"),
    # Kraken
    "daccord": Goalie("Joey Daccord", 55, "Starter"),
    "grubauer": Goalie("Philipp Grubauer", 40, "Backup"),
    # Blues
    "binner": Goalie("Jordan Binnington", 60, "Starter"),
    "hofer": Goalie("Joel Hofer", 50, "Backup"),
    # Lightning
    "vasy": Goalie("Andrei Vasilevskiy", 70, "Starter"),
    "johansson": Goalie("Jonas Johansson", 30, "Backup"),
    # Leafs
    "stolarz": Goalie("Anthony Stolarz", 60, "1A"),
    "woll": Goalie("Joseph Woll", 60, "1A"),
    "hildeby": Goalie("Dennis Hildeby", 30, "Third"),
    # Utah
    "vemelka": Goalie("Karel Vejmelka", 45, "1B"),
    "ingram": Goalie("Connor Ingram", 55, "1A"),
    "stauber": Goalie("Jaxson Stauber", 40, "Third"),
    # Canucks
    "demko": Goalie("Thatcher Demko", 60, "Starter"),
    "silvos": Goalie("Arturs Silovs", 30, "Third"),
    "lankinen": Goalie("Kevin Lankinen", 55, "1B"),
    # Golden Knights
    "hill": Goalie("Adin Hill", 55, "Starter"),
    "samsonov": Goalie("Ilya Samsonov", 45, "1B"),
    "schmid": Goalie("Akira Schmid", 20, "Third"),
    # Capitals
    "thompson": Goalie("Logan Thompson", 60, "1A"),
    "lindgren": Goalie("Charlie Lindgren", 55, "1B"),
    # Jets
    "hellebuyck": Goalie("Connor Hellebuyck", 80, "Starter"),
    "comrie": Goalie("Eric Comrie", 40, "Backup")
}