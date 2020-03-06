class Person:
    def __init__(self):
        # General Attributes:
        self.settlement = None
        self.home = None
        # Person Attributes:
        self.names = self.fetch_random_name() # Also need to account for lineage and passing down of last names
        self.weight = 100
        self.status = self.get_status()
        self.wealth = 0
        self.family = None
        # Profession Attributes:
        self.job = None
        self.skills = None
        self.employer = None
        # Live Simulation Attributes:
        self.pos = [0,0]
        self.vel = [0,0]
        self.current_destination = None
        self.load_capacity = 0
        self.load_type = None

    def fetch_status(self, status:int):
        # Combine lineage and wealth (Potentially other factors)
        # Calculate for citizens that have seen net Finance sifts of over some number to cut down computations for larger cities
        return status

    def fetch_lineage(self):
        pass

    @staticmethod
    def fetch_random_name():
        names = ["Freddie", "Earl", "Carmichael"]
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

    class Industrial:
        def __init__(self):
            pass

        class Test:
            def __init__(self, test:int):
                self.test = test

    class Residential:
        pass

    class Agricultural:
        pass

    class Governmental:
        pass

    class Commercial:
        pass

Test_object = Building.Industrial.Test(1)
print(Test_object.test)

# Instantiate some form of currency standards rate system, could be based on a gold standard and would need conversion rates.

# Cities once out of periphery will operate as systems following the projections of growth or decline from the previous years
# with some injections of random events.

# Create a vast intertwined global stage in which events that happen in other cities affect the progression of other cities

# Time period: Dawn of the 20th century
# Electricity
# Ending of Traditional Warfare : Introduction of Guerrilla Warfare
# Railroads for international commerce
