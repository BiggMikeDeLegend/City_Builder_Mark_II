import pygame
import Unnamed_0x00 as gen
class Draw:
    def __init__(self):
        pass

    def hombre(self, surface, Person: gen.Person):
        pygame.draw.rect(surface, (Person.status * 2))
