
from main.spaceship import Spaceship

def test_Response():
    ship = Spaceship("Orion",5)
    assert ship.name == "Orion"
    assert ship.health == 5

def test_DeadShip():
    a = Spaceship("Mega", -1)
    a = a.__dict__
    expected = a['alive'] = False
    assert expected == a['alive']

def test_ShowShip():
    a = Spaceship("Mega", 5)
    a = a.__dict__
    expected = {'name':'Mega','health':5, 'alive':True}
    assert expected == a







  
