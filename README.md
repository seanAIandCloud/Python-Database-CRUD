Soccer Player Database

A Python GUI application for managing soccer player stats. Built with PyQt5 and SQLite, this app lets you add, update, delete, and filter players through an interactive interface.

Features

Add Player: Enter player details—name, position, nationality, club, goals, assists, appearances.

Update Stats: Modify an existing player's stats quickly.

Delete Player: Remove players from the database.

Filter Players:

By Position

By Nationality (case-insensitive)

Display All Players: View all database entries.

Clear Values: Reset all input fields and table selection.

Interactive Table: Click a player in the table to auto-fill the form for editing or deletion.

Tech Stack

Python 3.x

PyQt5 – GUI framework

SQLite3 – Lightweight SQL database

Qt Designer – Visual UI design

Usage

Run the app:

python main.py


Use the GUI to:

Add, update, or delete players

Filter players by position or nationality

Select a player in the table to auto-fill fields

Database

Database File: soccer_players.db

Table: Players

Columns:

Player_Name (TEXT, Primary Key)

Position (TEXT)

Nationality (TEXT)

Current_Club (TEXT)

Goals (INTEGER)

Assists (INTEGER)

Appearances (INTEGER)

The database is created automatically if it doesn’t exist. Sample players included: Lionel Messi, Erling Haaland, Kylian Mbappe.
