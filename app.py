from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
import queries

app = Flask(__name__)

# Configure Session
app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


# Create all your routes below here

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/base")
def base():
    return render_template("index.html")
@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("pname")
        points = request.form.get("ppoints")
        assists = request.form.get("passist")
        reb = request.form.get("Preb")
        teams = request.form.get("Teams")
        add_p = queries.add_player(name, points, assists, reb, teams)
        print(add_p)
        return redirect("/list")
    return render_template("add.html")
@app.route("/list")
def list():

    text = queries.get_all_nba()
    List  = queries.get_avg()
    print(text)
    print(List)
    return render_template("list.html", nbas=text)

@app.route("/delete/<name>", methods=['POST'] )
def delete(name):

    print(name)
    dele_p = queries.delete_p(name)
    print(dele_p)
    flash(name + " data has been removed")
    return render_template("list.html")

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        name = request.form.get("pname1")


        update = queries.upd(name, points, assists, reb, team)
        print(update)
        return redirect("/list")

    return render_template("edit.html")
