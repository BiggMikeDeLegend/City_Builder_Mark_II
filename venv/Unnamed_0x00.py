class Hombre:
    def __init__(self):
        # General Attributes:
        self.settlement = None
        self.home = None
        # Person Attributes:
        self.names = self.fetch_random_name() # Also need to account for lineage and passing down of last names
        self.weight = 100
        self.social_class = 0
        self.wealth = 0
        self.family = None
        # Profession Attributes:
        self.job = None
        self.skills = None
        self.employer = None

    @staticmethod
    def fetch_random_name():
        names = ["Freddie", "Earl", "Von Hickter"]
        return names

class Settlement:
    def __init__(self):
        self.tier = 0
        self.size = 1 # IDK??
        self.population = None
        self.people = None
        self.num_building = 0
        self.buildings = []

class Building:
    def __init__(self):
        self.type = None
        self.name = self.type.name

