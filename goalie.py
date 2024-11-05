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
    "gibson": Goalie("John Gibson", 40, "1B"),
    "dostal": Goalie("Lukas Dostal", 55, "1A"),
    "reimer": Goalie("James Reimer", 45, "Third"),
    # Bruins
    "swayman": Goalie("Jeremy Swayman", 70, "Starter"),
    "korp": Goalie("Joonas Korpisalo", 30, "Backup"),
    # Sabres
    "luukkonen": Goalie("Ukko-Pekka Luukkonen", 55, "1A"),
    "levi": Goalie("Devon Levi", 45, "1B"),
    # Flames
    "wolf": Goalie("Dustin Wolf", 50, "1B"),
    "vladar": Goalie("Dan Vladar", 40, "1A"),
    "cooley": Goalie("Devin Cooley", 30, "Third"),
    # Hurricanes
    "andersen": Goalie("Frederik Andersen", 60, "1A"),
    "kochetkov": Goalie("Pyotr Kochetkov", 50, "1B"),
    "martin": Goalie("Spencer Martin", 30, "Third"),
    # Blackhawks
    "mrazek": Goalie("Petr Mrazek", 40, "1B"),
    "brossoit": Goalie("Laurent Brossoit", 55, "1A"),
    "soderblom": Goalie("Arvid Soderblom", 20, "Third"),
    # Avalanche
    "georgiev": Goalie("Alexandar Georgiev", 50, "Starter"),
    "annunen": Goalie("Justus Annunen", 45, "Backup"),
    "kahkonen": Goalie("Kaapo Kahkonen", 40, "Third"),
    # Blue Jackets
    "merzlikins": Goalie("Elvis Merzlikins", 40, "1B"),
    "tarasov": Goalie("Daniil Tarasov", 45, "1A"),
    # Stars
    "oettinger": Goalie("Jake Oettinger", 60, "Starter"),
    "desmith": Goalie("Casey DeSmith", 50, "Backup"),
    # Red Wings
    "talbot": Goalie("Cam Talbot", 60, "1A"),
    "husso": Goalie("Ville Husso", 40, "Third"),
    "lyon": Goalie("Alex Lyon", 50, "1B"),
    "campbell": Goalie("Jack Campbell", 40),
    # Oilers
    "skinner": Goalie("Stuart Skinner", 55, "Starter"),
    "pickard": Goalie("Calvin Pickard", 40, "Backup"),
    # Panthers
    "bobrovsky": Goalie("Sergei Bobrovsky", 70, "Starter"),
    "knight": Goalie("Spencer Knight", 50, "1B"),
    # Kings
    "kuemper": Goalie("Darcy Kuemper", 60, "Starter"),
    "rittich": Goalie("David Rittich", 40, "Backup"),
    "copley": Goalie("Phoenix Copley", 40, "Backup"),
    # Wild
    "fleury": Goalie("Marc-Andre Fleury", 50, "1B"),
    "gustavsson": Goalie("Filip Gustavsson", 55, "1A"),
    # Canadiens
    "primeau": Goalie("Cayden Primeau", 50, "1B"),
    "montembeault": Goalie("Sam Montembeault", 55, "1A"),
    # Predators
    "saros": Goalie("Juuse Saros", 70, "Starter"),
    "wedgewood": Goalie("Scott Wedgewood", 40, "Backup"),
    # Devils
    "markstrom": Goalie("Jacob Markstrom", 60, "Starter"),
    "allen": Goalie("Jake Allen", 50, "1B"),
    # Islanders
    "sorokin": Goalie("Ilya Sorokin", 70, "Starter"),
    "varlamov": Goalie("Semyon Varlamov", 60, "1A"),
    # Rangers
    "shesterkin": Goalie("Igor Shesterkin", 80, "Starter"),
    "quick": Goalie("Jonathan Quick", 50, "Backup"),
    # Senators
    "ullmark": Goalie("Linus Ullmark", 70, "Starter"),
    "forsberg": Goalie("Anton Forsberg", 40, "Backup"),
    "sogaard": Goalie("Mads Sogaard", 30, "Third"),
    # Flyers
    "fedotov": Goalie("Ivan Fedotov", 40, "1B"),
    "ersson": Goalie("Samuel Ersson", 45, "1A"),
    "kolosov": Goalie("Aleksei Kolosov", 30, "Third"),
    # Penguins
    "jarry": Goalie("Tristan Jarry", 60, "Starter"),
    "ned": Goalie("Alex Nedeljkovic", 45, "Backup"),
    "blomqvist": Goalie("Joel Blomqvist", 45, "Backup"),
    # Sharks
    "askarov": Goalie("Yaroslav Askarov", 30, "Third"),
    "blackwood": Goalie("Mackenzie Blackwood", 40, "1A"),
    "vanacek": Goalie("Vitek Vanecek", 40, "1B"),
    # Kraken
    "daccord": Goalie("Joey Daccord", 55, "Starter"),
    "grubauer": Goalie("Philipp Grubauer", 40, "1B"),
    # Blues
    "binner": Goalie("Jordan Binnington", 60, "Starter"),
    "hofer": Goalie("Joel Hofer", 50, "Backup"),
    # Lightning
    "vasy": Goalie("Andrei Vasilevskiy", 70, "Starter"),
    "johansson": Goalie("Jonas Johansson", 20, "Backup"),
    # Leafs
    "stolarz": Goalie("Anthony Stolarz", 60, "1A"),
    "woll": Goalie("Joseph Woll", 55, "1B"),
    "hildeby": Goalie("Dennis Hildeby", 30, "Third"),
    # Utah
    "vemelka": Goalie("Karel Vejmelka", 40, "1B"),
    "ingram": Goalie("Connor Ingram", 55, "1A"),
    # Canucks
    "demko": Goalie("Thatcher Demko", 60, "Starter"),
    "silvos": Goalie("Arturs Silovs", 30, "Third"),
    "lankinen": Goalie("Kevin Lankinen", 50, "Backup"),
    # Golden Knights
    "hill": Goalie("Adin Hill", 55, "1A"),
    "samsonov": Goalie("Ilya Samsonov", 45, "1B"),
    "schmid": Goalie("Akira Schmid", 20, "Third"),
    # Capitals
    "thompson": Goalie("Logan Thompson", 55, "1B"),
    "lindgren": Goalie("Charlie Lindgren", 55, "1A"),
    # Jets
    "hellebuyck": Goalie("Connor Hellebuyck", 80, "Starter"),
    "comrie": Goalie("Eric Comrie", 40, "Backup")
}