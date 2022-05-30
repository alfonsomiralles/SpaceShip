from src.main.spaceship import Spaceship

class SpaceshipRepository:
    __spaceships = [0, "Omega"]

    def addSpaceship(self, spaceship):
        self.__spaceships.append(spaceship)


    def getSpaceship(self):
        return self.__spaceships