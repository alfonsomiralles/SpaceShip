

class Spaceship:

    def __init__(self, name, health):
        if  health < 0:  
            raise ValueError ("The Spaceship can't have health below 0. Please try again")       
        else:
            self.name = name
            self.health = health
            self.alive = True
            self.weapon = 'weapon'

    def __hash__(self):
        return hash((self.name, self.health, self.alive))

    def __eq__(self, other):
        return (self.name, self.health, self.alive, self.weapon) == (other.name, other.health, other.alive, other.weapon)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

    def shoot(spaceships, attacker, target):
        for x in spaceships:
            if x['name'] == attacker:
                if x['alive'] == False:
                    raise Exception("A Spaceship destroyed can't shoot")
            else:
                if x['name'] == target:
                    if x['health']==0:
                        raise Exception("Target is destroyed")
                    x['health']-=1 
                    if x['health'] == 0 :
                        x['alive'] = False   