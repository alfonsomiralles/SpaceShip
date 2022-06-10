class Spaceship:

    def __init__(self, name, health, total_power, weapon_power_needed):
        if  health < 0:  
            raise ValueError ("The Spaceship can't have health below 0. Please try again")
        if total_power < 0:
            raise ValueError ("power can't be below 0")  
        if  weapon_power_needed < 0 or weapon_power_needed > total_power:
            raise ValueError ("weapon power needed can't have that value") 
        else:
            self.name = name
            self.health = health
            self.alive = True
            self.total_power = total_power
            self.weapon_power_needed = weapon_power_needed
            self.power_consumed_by_weapon = self.weapon_power_needed
            self.power_not_in_use = self.total_power-self.weapon_power_needed
                 
    def __hash__(self):
        return hash((self.name, self.health, self.alive, self.total_power, self.weapon_power_needed, self.power_not_in_use, self.power_consumed_by_weapon))

    def __eq__(self, other):
        return (self.name, self.health, self.alive, self.total_power, self.weapon_power_needed, self.power_not_in_use, self.power_consumed_by_weapon) == (other.name, other.health, other.alive, other.total_power, other.weapon_power_needed, other.power_not_in_use, other.power_consumed_by_weapon)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

    def shoot(spaceships, attacker, target):
        for x in spaceships:
            if x['name'] == attacker:
                if x['weapon_power_needed'] != x['power_consumed_by_weapon']:
                    raise Exception("Weapon-Power-Needed must be equal than Power-Consumed-by-Weapon")
                if x['alive'] == False:
                    raise Exception("A Spaceship destroyed can't shoot")
            else:
                if x['name'] == target:
                    if x['health']==0:
                        raise Exception("Target is destroyed")
                    x['health']-=1 
                    if x['health'] == 0 :
                        x['alive'] = False 

    def modify(spaceships, name, power_consumed_by_weapon):
        if (power_consumed_by_weapon < 0):
            raise ValueError ("power can't be below 0")
        for x in spaceships:
            if x['name'] == name:
                if power_consumed_by_weapon > x['total_power']:
                    raise ValueError ("power can't be higher than total-power")
                else:    
                    x['power_consumed_by_weapon'] = power_consumed_by_weapon
                    x['power_not_in_use'] = x['total_power'] - power_consumed_by_weapon   
        
                    

       
