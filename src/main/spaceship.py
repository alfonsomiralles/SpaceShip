

class Spaceship:

    def __init__(self, name, health):
        if  health < 0:  
            raise ValueError ("The Spaceship can't have health below 0. Please try again")       
        else:
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

    def shoot(spaceships, target):
        for x in spaceships:
            if x['name'] == target:
                if x['health']==0:
                    raise Exception("Target is destroyed")
                x['health']-=1 
                if x['health'] == 0 :
                    x['alive'] = False  

        

# Spaceship("Orion", 3, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))
# Spaceship("Mega", 4, SpaceshipRepository.spaceships)
# print(Spaceship.serialize(SpaceshipRepository.spaceships))