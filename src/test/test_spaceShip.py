
from main.spaceship import Spaceship
from main.spaceShipRepository import SpaceshipRepository

def test_CreateResponse():
    Spaceship("Mega",3,SpaceshipRepository.spaceships)
    response = Spaceship.serialize(SpaceshipRepository.spaceships)
    assert response == "Name: Mega\nHealth: 3\n"  
    
def test_Create():
    response = Spaceship("Orion",5,SpaceshipRepository.spaceships)
    assert response.name == "Orion"
    assert response.health == 5
  
