
from flask import Flask,render_template, request
from spaceship import Spaceship

app = Flask(__name__)

spaceships = []
# Defining the home page of our site

@app.route("/")  # this sets the route to this page
def home():
    return render_template("index.html")
	# return "Hello! this is the main page <h1>Faster Than ight</h1>"  # some basic inline html

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        health = int(request.form["health"])
        totalpower = int(request.form["totalpower"])
        weapon_power_needed = int(request.form["weapon_power_needed"])
        for x in spaceships:
            if x['name'] == name:
                duplicatemessage = "The Spaceship can't be created because already exists!"
                return render_template("create.html", message = duplicatemessage)
        if (totalpower < 0):
            nomessage = f"power can't be below 0"
            return render_template("create.html", message=nomessage)
        if (totalpower < weapon_power_needed):
            nomessage = f"Weapon-power-needed can't be higher than Total-power"
            return render_template("create.html", message=nomessage)                
        if (health > 0):
            Ship =Spaceship(name, health, totalpower, weapon_power_needed)
            Ship = Ship.__dict__
            spaceships.append(Ship)
            okmessage = f"Spaceship: {name} created is alive with Health: {health}"
            return render_template("create.html", message=okmessage)  
        if (health < 0):
            nomessage = f"Spaceship: {name} can't have health below 0. Please try again."
            return render_template("create.html", message=nomessage)         
        else:
            Ship =Spaceship(name, health, totalpower, weapon_power_needed)
            Ship.alive = False
            Ship = Ship.__dict__
            spaceships.append(Ship)
            failmessage = f"The Spaceship: {name} created is already distroyed because Health: {health} must be over 0"
            return render_template("create.html", message = failmessage)
    return  render_template("create.html")           

@app.route("/show", methods=["GET"])
def show():
    if request.method == "GET":
        if len(spaceships) == 0:
            emptymessage = "The list of SpaceShips is empty, you need to create SpaceShips"
            return render_template("show.html", message = emptymessage)
        else:
            return render_template("show.html", showships = spaceships)
    return render_template("show.html")

@app.route("/shoot", methods=["POST", "GET"])
def shoot():
    if request.method == "POST":
        attacker = request.form["atacker"]
        target = request.form["target"]
        
        for x in spaceships:
            if x['name'] == attacker:
                if x['weapon_power_needed'] != x['power_consumed_by_weapon']:
                    deadmessage = "Weapon-Power-Needed must be equal than Power-Consumed-by-Weapon"
                    return render_template("shoot.html", message = deadmessage)   
                if x['alive'] == False:
                    destroyedmessage = "A Spaceship destroyed can't shoot"
                    return render_template("shoot.html", message = destroyedmessage)
        for x in spaceships:            
            if x['name'] == target:
                if x['alive']==False:
                    deadmessage = "Target is already destroyed"
                    return render_template("shoot.html", message = deadmessage)
        if (target == attacker):
            samemessage = "The SpaceShips must be different"
            return  render_template("shoot.html", message = samemessage)            
        else:
            Spaceship.shoot(spaceships, attacker, target)
            shootmessage = f'The Spaceship {target} has received a shoot'
            return  render_template("shoot.html", message = shootmessage)                              
        
        
    return  render_template("shoot.html")

@app.route("/power", methods=["POST", "GET"])
def power():
    if request.method == "POST":
        name = request.form["name"]
        power_consumed_by_weapon = int(request.form["power_consumed_by_weapon"])
        if (power_consumed_by_weapon < 0):
            nomessage = f"power can't be below 0"
            return render_template("power.html", message=nomessage)
        for x in spaceships:
            if x['name'] == name:
                if power_consumed_by_weapon > x['total_power']:
                    nomessage ="power can't be higher than total-power"
                    return render_template("power.html", message = nomessage)
                else:       
                    Spaceship.modify(spaceships, name, power_consumed_by_weapon)
                    okmessage = "Power-consumed-by-weapon modified"
                    return render_template("power.html", message = okmessage)     
                      
    return  render_template("power.html")       

if __name__=="__main__":
    app.run(debug=True)