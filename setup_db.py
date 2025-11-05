import sqlite3

conn = sqlite3.connect("soccer_players.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Players (
    Player_Name TEXT PRIMARY KEY,
    Position TEXT,
    Nationality TEXT,
    Current_Club TEXT,
    Goals INTEGER,
    Assists INTEGER,
    Appearances INTEGER
)
""")

cur.execute("DELETE FROM Players")

players = [
    ("Erling Haaland", "Striker", "Norway", "Manchester City", 36, 8, 32),
    ("Kylian Mbappe", "Striker", "France", "Paris Saint-Germain", 28, 12, 30),
    ("Lionel Messi", "Attacking Midfielder", "Argentina", "Inter Miami", 25, 15, 29)
]

cur.executemany("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?)", players)

conn.commit()
conn.close()

