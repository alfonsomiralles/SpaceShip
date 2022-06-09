

class Spaceship:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.alive = True

    def __hash__(self):
        return hash((self.name, self.health, self.alive))

    def __eq__(self, other):
        return (self.name, self.health, self.alive) == (other.name, other.health, other.alive)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

        

# Spaceship("Orion", 3, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))
# Spaceship("Mega", 4, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))