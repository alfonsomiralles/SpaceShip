
class Spaceship:

    def __init__(self, name, health, spaceshipsList: list):
        self.name = name
        self.health = health
        spaceshipsList.append(self)

    def serialize(spaceshipsList):
        data = ""
        for i in spaceshipsList:
            data += f"Name: {str(i.name)}\nHealth: {str(i.health)}\n"
        return data


# ship = Spaceship(-1, 'Orion')
# print(ship)
