from cs50 import SQL
import queries as q

db = SQL("sqlite:///project.db")
# Create your functions for working with your database below here

def get_all_nba():
    sql = """SELECT * FROM nba ORDER BY points DESC"""
    rows = db.execute(sql)
    return rows

def get_avg():
    people = get_all_nba()
    player_avg = []
    for person in people:
        point = person.get("points")
        assist = person.get("assists")
        rebs = person.get("reb")
        avg = (point + assist + rebs)/3
        player_avg.append(round(avg, 2))
    return player_avg

def add_player(name, points, assists, reb, team):
    sql = """INSERT INTO nba (name, points, assists, reb, team) Values (?,?,?,?,?)"""
    id = db.execute(sql, name, points, assists, reb, team)
    return id


def delete_p(name):
    sql = """DELETE FROM nba WHERE name = ?"""
    id = db.execute(sql, name)
    return id

def upd(name, points, assists, reb, team):
    sql = """UPDATE nba SET name = ?, points = ?, assists = ?, reb = ?, team = ? WHERE name = ?"""
    id = db.execute(sql, name, points, assists, reb, team)
    return id
