from flask import Flask, redirect, url_for, render_template, request
from spaceShipRepository import SpaceshipRepository
from spaceship import Spaceship

app = Flask(__name__)


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
        Spaceship(name, health, SpaceshipRepository.spaceships)
        print(Spaceship.serialize(SpaceshipRepository.spaceships))
        if (health > 0):
            okmessage = f"Spaceship: {name} created is alive with Health: {health}"
            return render_template("create.html", message=okmessage)
        else:
            failmessage = f"The Spaceship: {name} created is already distroyed because Health: {health} must be over 0"
            return render_template("create.html", message=failmessage)
    return  render_template("create.html")           

@app.route("/admin")
def admin():
      return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"


if __name__=="__main__":
    app.run(debug=True)