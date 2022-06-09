

class Spaceship:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.alive = True

    def __str__(self):
        return str(self.__dict__)  

    def __repr__(self):
        return str(self.__dict__)
        

# Spaceship("Orion", 3, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))
# Spaceship("Mega", 4, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))