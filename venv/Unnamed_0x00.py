import random

class Person:
    def __init__(self):
        # General Attributes:
        self.settlement = None
        self.home = None
        # Person Attributes:
        self.names = self.fetch_random_name() # Also need to account for lineage and passing down of last names
        self.gender = None
        self.weight = 100
        self.status = self.get_status()
        self.family = None
        # Profession Attributes:
        self.job = None
        self.skills = None
        self.employer = None
        # Financial Attributes:
        self.net_monetary_funds = 0
        self.properties = None
        # Live Simulation Attributes:
        self.pos = [0,0]
        self.vel = [0,0]
        self.current_destination = None
        self.load_capacity = 0
        self.load_type = None
        self.rng_seed = self.generate_rng_seed()

    def fetch_status(self):
        status = self.net_monetary_funds * self.appraise_propetry() * self.fetch_lineage()
        # Combine lineage and wealth (Potentially other factors)
        # Calculate for citizens that have seen net Finance sifts of over some number to cut down computations for
        # larger cities
        return status

    def appraise_property(self):
        temp_value = 0
        if self.properties is not None:
            for property in self.properties:
                temp_value += property.current_value
        return temp_value

    def fetch_lineage(self):
        return int

    def fetch_random_name(self):
        rng_seed = self.rng_seed
        names = ["Freddie", "Earl", "Carmichael"]
        return names

    @staticmethod
    def generate_rng_see():
        rng_seed_length = 3
        rList = [random.randint(0, 255) for i in range(rng_seed_length)]
        return bytes(rList)


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
        class Quarry:
            def __init__(self):
                pass
            # Different materials a Quarry can harvest include Limestone, Granite, Marble
        class Forester:
            def __init__(self):
                pass
            # Different materials a Forester can harvest include Oak, Birch, Pine,

        class Mine:
            pass

        class Rig:
            pass

        class Factory:
            pass

        class Construction:
            class Crane:
                pass

    class Agricultural:
        class Field:
            pass

        class Orcard:
            pass

    class Governmental:
        def __init__(self):
            pass

    class Commercial:
        def __init__(self):
            pass

    class Infastructure:
        class Hydro:
            pass

        class Electrical:
            pass

        class GeneralInfastructure:
            pass

    class Asthetics:
        class Park:
            pass
# Instantiate some form of currency standards rate system, could be based on a gold standard and would need conversion
# rates.

# Cities once out of periphery will operate as systems following the projections of growth or decline from the previous
# years with some injections of random events.

# Create a vast intertwined global stage in which events that happen in other cities affect the progression of other
# cities.

# Time period: Dawn of the 20th century
# Electricity
# Ending of Traditional Warfare : Introduction of Guerrilla Warfare
# Railroads for international commerce
# Steam Ships / Sailboats?
