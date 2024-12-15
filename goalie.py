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
    "dostal": Goalie("Lukas Dostal", 60, "1B"),
    "reimer": Goalie("James Reimer", 40, "Inactive"),
    # Bruins
    "swayman": Goalie("Jeremy Swayman", 60, "Starter"),
    "korp": Goalie("Joonas Korpisalo", 30, "Backup"),
    # Sabres
    "luukkonen": Goalie("Ukko-Pekka Luukkonen", 55, "Starter"),
    "levi": Goalie("Devon Levi", 40, "Third"),
    "reimerbuf": Goalie("James Reimer", 40, "Backup"),
    # Flames
    "wolf": Goalie("Dustin Wolf", 55, "1A"),
    "vladar": Goalie("Dan Vladar", 45, "1B"),
    "cooley": Goalie("Devin Cooley", 30, "Inactive"),
    # Hurricanes
    "andersen": Goalie("Frederik Andersen", 60, "Third"),
    "kochetkov": Goalie("Pyotr Kochetkov", 50, "1A"),
    "martin": Goalie("Spencer Martin", 30, "Backup"),
    # Blackhawks
    "mrazek": Goalie("Petr Mrazek", 55, "1A"),
    "brossoit": Goalie("Laurent Brossoit", 55, "1B"),
    "soderblom": Goalie("Arvid Soderblom", 40, "Third"),
    "commesso": Goalie("Drew Commesso", 40, "Third"),
    # Avalanche
    "georgiev": Goalie("Alexandar Georgiev", 50, "Inactive"),
    "annunen": Goalie("Justus Annunen", 50, "Inactive"),
    "kahkonen": Goalie("Kaapo Kahkonen", 40, "Inactive"),
    "blackwoodcol": Goalie("Mackenzie Blackwood", 55, "Starter"),
    "wedgewoodcol": Goalie("Scott Wedgewood", 40, "Backup"),
    # Blue Jackets
    "merzlikins": Goalie("Elvis Merzlikins", 45, "Starter"),
    "tarasov": Goalie("Daniil Tarasov", 40, "Backup"),
    "greaves": Goalie("Jet Greaves", 40, "Third"),
    # Stars
    "oettinger": Goalie("Jake Oettinger", 60, "Starter"),
    "desmith": Goalie("Casey DeSmith", 50, "Backup"),
    # Red Wings
    "talbot": Goalie("Cam Talbot", 60, "Starter"),
    "husso": Goalie("Ville Husso", 40, "Backup"),
    "lyon": Goalie("Alex Lyon", 50, "1B"),
    "campbell": Goalie("Jack Campbell", 40, "Inactive"),
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
    "annunennsh": Goalie("Justus Annunen", 45, "Backup"),
    "wedgewood": Goalie("Scott Wedgewood", 40, "Inactive"),
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
    "forsberg": Goalie("Anton Forsberg", 45, "Backup"),
    "sogaard": Goalie("Mads Sogaard", 30, "Inactive"),
    # Flyers
    "fedotov": Goalie("Ivan Fedotov", 40, "1B"),
    "ersson": Goalie("Samuel Ersson", 50, "1A"),
    "kolosov": Goalie("Aleksei Kolosov", 30, "Third"),
    # Penguins
    "jarry": Goalie("Tristan Jarry", 50, "1A"),
    "ned": Goalie("Alex Nedeljkovic", 40, "1B"),
    "blomqvist": Goalie("Joel Blomqvist", 50, "Third"),
    # Sharks
    "askarov": Goalie("Yaroslav Askarov", 40, "Third"),
    "blackwood": Goalie("Mackenzie Blackwood", 50, "Inactive"),
    "vanacek": Goalie("Vitek Vanecek", 50, "1A"),
    "georgievsj": Goalie("Alexandar Georgiev", 45, "1B"),
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
    "woll": Goalie("Joseph Woll", 60, "1A"),
    "hildeby": Goalie("Dennis Hildeby", 30, "Inactive"),
    # Utah
    "vemelka": Goalie("Karel Vejmelka", 50, "1B"),
    "ingram": Goalie("Connor Ingram", 55, "1A"),
    "stauber": Goalie("Jaxson Stauber", 40, "Third"),
    # Canucks
    "demko": Goalie("Thatcher Demko", 60, "1A"),
    "silvos": Goalie("Arturs Silovs", 30, "Third"),
    "lankinen": Goalie("Kevin Lankinen", 55, "1B"),
    # Golden Knights
    "hill": Goalie("Adin Hill", 55, "1A"),
    "samsonov": Goalie("Ilya Samsonov", 45, "1B"),
    "schmid": Goalie("Akira Schmid", 20, "Inactive"),
    # Capitals
    "thompson": Goalie("Logan Thompson", 60, "1A"),
    "lindgren": Goalie("Charlie Lindgren", 55, "1B"),
    # Jets
    "hellebuyck": Goalie("Connor Hellebuyck", 80, "Starter"),
    "comrie": Goalie("Eric Comrie", 40, "Backup")
}