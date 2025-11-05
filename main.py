import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic

class SoccerDB(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("player_database.ui", self)

        self.conn = sqlite3.connect("soccer_players.db")
        self.cur = self.conn.cursor()
        self.create_table()

        self.add_players.clicked.connect(self.add_player)
        self.update_stats.clicked.connect(self.update_player)
        self.delete_players.clicked.connect(self.delete_player)
        self.filter_position.clicked.connect(self.filter_by_position)
        self.filter_nationality.clicked.connect(self.filter_by_nationality)
        self.display_players.clicked.connect(self.display_all_players)
        self.clear_values.clicked.connect(self.clear_fields)

        self.display_all_players()

        self.tableWidget.itemSelectionChanged.connect(self.load_selected_player)

    def create_table(self):
        self.cur.execute("""
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
        self.conn.commit()

    def add_player(self):
        name = self.Player_name.text()
        position = self.Position.currentText()
        nationality = self.Nationality.text()
        club = self.Current_club.text()
        goals = int(self.Goals.text() or 0)
        assists = int(self.assists.text() or 0)
        appearances = int(self.appearences.text() or 0)

        try:
            self.cur.execute("""
                INSERT INTO Players (Player_Name, Position, Nationality, Current_Club, Goals, Assists, Appearances)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, position, nationality, club, goals, assists, appearances))
            self.conn.commit()
            self.display_all_players()
            print(f"Player {name} added successfully!")
        except sqlite3.IntegrityError:
            print(f"Player {name} already exists.")

    def update_player(self):
        name = self.Player_name.text()
        position = self.Position.currentText()
        nationality = self.Nationality.text()
        club = self.Current_club.text()
        goals = int(self.Goals.text() or 0)
        assists = int(self.assists.text() or 0)
        appearances = int(self.appearences.text() or 0)

        self.cur.execute("""
            UPDATE Players
            SET Position=?, Nationality=?, Current_Club=?, Goals=?, Assists=?, Appearances=?
            WHERE Player_Name=?
        """, (position, nationality, club, goals, assists, appearances, name))
        self.conn.commit()
        self.display_all_players()
        print(f"Player {name} updated successfully!")

    def delete_player(self):
        name = self.Player_name.text()
        self.cur.execute("DELETE FROM Players WHERE Player_Name=?", (name,))
        self.conn.commit()
        self.display_all_players()
        print(f"Player {name} deleted successfully!")

    def filter_by_position(self):
        position = self.Position.currentText()
        self.cur.execute("SELECT * FROM Players WHERE Position=?", (position,))
        players = self.cur.fetchall()
        self.populate_table(players)

    def filter_by_nationality(self):
        nationality = self.Nationality.text()
        self.cur.execute("SELECT * FROM Players WHERE Nationality=? COLLATE NOCASE", (nationality,))
        players = self.cur.fetchall()
        self.populate_table(players)

    def display_all_players(self):
        self.cur.execute("SELECT * FROM Players")
        players = self.cur.fetchall()
        self.populate_table(players)

    def populate_table(self, players):
        self.tableWidget.setRowCount(0)
        for row_idx, player in enumerate(players):
            self.tableWidget.insertRow(row_idx)
            for col_idx, value in enumerate(player):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def load_selected_player(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            return

        def get_item(col):
            item = self.tableWidget.item(row, col)
            return item.text() if item else ""

        self.Player_name.setText(get_item(0))
        self.Position.setCurrentText(get_item(1))
        self.Nationality.setText(get_item(2))
        self.Current_club.setText(get_item(3))
        self.Goals.setText(get_item(4))
        self.assists.setText(get_item(5))
        self.appearences.setText(get_item(6))

    def clear_fields(self):
        self.Player_name.clear()
        self.Position.setCurrentIndex(0)
        self.Nationality.clear()
        self.Current_club.clear()
        self.Goals.clear()
        self.assists.clear()
        self.appearences.clear()
        self.tableWidget.clearSelection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoccerDB()
    window.show()
    sys.exit(app.exec_())
