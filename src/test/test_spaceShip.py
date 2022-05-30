from cgi import test
from main.spaceship import Spaceship

def test_Spaceship():

    ship = Spaceship(2, 'Orion')

    assert ship.serialize() == 'health:2, name:Orion'

# def test_Spaceship_destroyed():

#     ship = Spaceship(-1, 'Mega')
#     assert ship == 'Exception: The SpaceShip is destroyed because health is < 0'