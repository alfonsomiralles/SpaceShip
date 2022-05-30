
class Spaceship:

    def __init__(self, health, name):
        self.health = health
        self.name = name
        if (self.health < 0):
            raise Exception ('The SpaceShip is destroyed because health is < 0')

    def serialize(self):
        return f'health:{self.health}, name:{self.name}'


# ship = Spaceship(-1, 'Orion')
# print(ship)