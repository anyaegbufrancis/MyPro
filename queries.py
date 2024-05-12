# from cs50 import SQL
import sqlite3


def get_all_nba():
    conn = sqlite3.connect('project.db')
    db = conn.cursor()
    sql = """SELECT * FROM nba ORDER BY points DESC"""
    rows = db.execute(sql).fetchall()
    conn.close()
    return rows

def add_player(name, points, assists, reb, team):
    conn = sqlite3.connect('project.db')
    db = conn.cursor()
    sql = """INSERT INTO nba (name, points, assists, reb, team) Values (?,?,?,?,?)"""
    params = (name, points, assists, reb, team)    
    id = db.execute(sql, params)
    conn.commit()
    conn.close()
    return id

def delete_player(name):
    conn = sqlite3.connect('project.db')
    db = conn.cursor()
    sql = """DELETE FROM nba WHERE name = ?"""
    id = db.execute(sql, (name,))
    conn.commit()
    conn.close()
    return id

def update_player(name, new_name, new_points, new_assists, new_reb, new_team):
    conn = sqlite3.connect('project.db')
    db = conn.cursor()
    sql = """UPDATE nba SET name = ?, points = ?, assists = ?, reb = ?, team = ? WHERE name = ?"""
    params = (new_name, new_points, new_assists, new_reb, new_team, name)    
    id = db.execute(sql, params)
    conn.commit()
    conn.close()
    return id

def get_player_by_name(name):
    try:
        conn = sqlite3.connect('project.db')
        db = conn.cursor()
        sql = """SELECT * FROM nba WHERE name = ?"""
        db.execute(sql, (name,))
        player = db.fetchone()
        return player        
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None    
    finally:
        conn.close()

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




