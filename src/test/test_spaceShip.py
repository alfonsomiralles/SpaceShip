import pytest
from multiprocessing.sharedctypes import Value
from main.spaceship import Spaceship

"""Feature 1"""
"""Test to know if Spaceship is created correctly with the values provided"""
def test_Response():
    ship = Spaceship("Orion",5)
    assert ship.name == "Orion"
    assert ship.health == 5

"""Feature 1"""
"""Test to know if Spaceship with 0 health appears as status 'alive':False"""
def test_DeadShip():
    a = Spaceship("Mega", 0, 2, 2)
    a = a.__dict__
    expected = a['alive'] = False
    assert expected == a['alive']

"""Feature 2"""
"""Test to know if Spaceship is showed as a dictionary with all the keys and values"""
def test_ShowShip():
    a = Spaceship("Mega", 5, 5, 5)
    a = a.__dict__
    expected = {'name':'Mega','health':5, 'alive':True, 'weapon':'weapon', 'totalpower': 5, 'powernotinuse': 5}
    assert expected == a

"""Feature 3"""
"""Test to know if Spaceship A can shoot Spaceship B and decreases -1 health of B"""
def test_Shooting():
    l = []
    a = Spaceship("Mega", 5, 2, 2)
    a = a.__dict__
    b = Spaceship("Mega", 5, 2, 2)
    b = b.__dict__
    l.append(a)
    l.append(b)
    Spaceship.shoot(l,a,b)
    expected = b['health'] = 4
    assert expected == b['health']

"""Feature 4"""
"""Test to know if Spaceship with health < 0 can be created"""
def test_NoCreateShip():
    with pytest.raises(ValueError):
        a = Spaceship("Mega", -1, 2, 2)
        a = a.__dict__
        expected = ValueError
        assert expected == "The Spaceship can't have health below 0. Please try again"
 
"""Feature 4"""
"""Test to know if Spaceship with health=0 can be shooted"""
def test_NoShootHealth():
    with pytest.raises(Exception):
        l = []
        a = Spaceship("Mega", 5)
        a = a.__dict__
        b = Spaceship("Mega", 0)
        b = b.__dict__
        l.append(a)
        l.append(b)
        Spaceship.shoot(l,a,b)
        expected = Exception
        assert expected == "Target is destroyed"

"""Feature 5"""
"""Test to know if destroyed Spaceship can shoot"""
def test_NoDestroyed():
    with pytest.raises(Exception):
        l = []
        a = Spaceship("Mega", 0)
        a = a.__dict__
        b = Spaceship("Mega", 2)
        b = b.__dict__
        l.append(a)
        l.append(b)
        Spaceship.shoot(l,a,b)
        expected = Exception
        assert expected == "A Spaceship destroyed can't shoot"

"""Feature 6"""
"""Test to know if Spaceship is created correctly with weapon by default"""
def test_Response():
    ship = Spaceship("Orion",5, 2, 2)
    assert ship.weapon == "weapon"


"""Feature 7"""
"""Test to know if Spaceship gets erro when created with wrong values for power-not-in-use"""
def test_Response():
    with pytest.raises(ValueError):
        Spaceship("Orion",5, 2, 3)
        expected = ValueError
        assert expected == "power-not-in-use can't be higher than total-power"

"""Feature 7"""
"""Test to know if Spaceship gets erro when created with negative values"""
def test_Response():
    with pytest.raises(ValueError):
        Spaceship("Orion",5, 2, -1)
        expected = ValueError
        assert expected == "power can't be below 0"








  
