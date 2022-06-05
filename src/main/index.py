import json
from flask import Flask, redirect, url_for, render_template, request,jsonify
from spaceship import Spaceship
import json

app = Flask(__name__)


# Defining the home page of our site


@app.route("/")  # this sets the route to this page
def home():
    return render_template("index.html")
	# return "Hello! this is the main page <h1>Faster Than ight</h1>"  # some basic inline html

spaceships = []
@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        health = int(request.form["health"])
        
        if (health > 0):
            Ship =Spaceship(name, health)
            spaceships.append(Ship)
            okmessage = f"Spaceship: {name} created is alive with Health: {health}"
            return render_template("create.html", message=okmessage)
        else:
            Ship =Spaceship(name, health)
            Ship.alive = False
            spaceships.append(Ship)
            failmessage = f"The Spaceship: {name} created is already distroyed because Health: {health} must be over 0"
            return render_template("create.html", message = failmessage)
    return  render_template("create.html")           

@app.route("/show", methods=["GET"])
def show():
    if request.method == "GET":
        if len(spaceships) == 0:
            emptymessage = "The list of SpaceShips is empty, you need to create SpaceShips"
            return render_template("show.html", message1 = emptymessage)
        else:
            allmessage = spaceships
            return render_template("show.html", message = allmessage)
    return render_template("show.html")


if __name__=="__main__":
    app.run(debug=True)