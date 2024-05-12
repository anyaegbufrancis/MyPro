from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
from queries import get_all_nba, add_player, delete_player, update_player, get_player_by_name

app = Flask(__name__)

# Configure Session
app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)


# Create all your routes below here

@app.route("/")
def index():
    ret = get_all_nba()
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("index.html")

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        pname = request.form['pname']
        ppoints = request.form['ppoint']
        passists = request.form['passist']
        preb = request.form['preb']
        pteam = request.form['pteam']
        add_player(pname, ppoints, passists, preb, pteam)
        return redirect("/list")


@app.route("/list")
def list():
    nbas = get_all_nba()
    return render_template("list.html", nbas=nbas)
    

@app.route("/delete/<name>", methods=['POST'] )
def delete(name):
    delete_player(name)
    flash(f"{name} has been deleted")
    return redirect("/list")

@app.route("/edit/<name>", methods=["GET", "POST"])
def edit(name):
    if request.method == "POST":
        player_details = get_player_by_name(name)
        new_name = name
        new_points = player_details[2] if request.form.get("ppoints") == "" else request.form.get("ppoints")
        new_assists = player_details[3] if request.form.get("passists") == "" else request.form.get("passists")
        new_reb = player_details[4] if request.form.get("preb") == "" else request.form.get("preb")
        new_team = player_details[5] if request.form.get("pteam") == "" else request.form.get("pteam")
        update_player(name, new_name, new_points, new_assists, new_reb, new_team)
        return redirect("/list")
    else:
        player = get_player_by_name(name)
        return render_template("edit.html", nba=player)

