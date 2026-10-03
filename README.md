# Election System

Console-based voting system in Python, featuring authentication, data persistence, and identity validation — built as a hands-on learning project.

## Description

The project started as an exercise while I was learning the language. It began as a simple Log-in simulation and gradually scaled up to its current state.

## Technologies

Python, Pandas, openpyxl, bcrypt.

## Features

- Login with data persistence
- Candidate registration
- Voter registration (no pre-existing electoral roll)
- Double-voting prevention
- Identity validation using a Luhn-style algorithm

## Installation / Usage

1. Clone the repository
2. Install dependencies via requirements.txt
3. Run: python run.py

## Project Status

The project is still under development. The core is nearly complete; what remains is refining the logic and adding exception handling, as well as finishing the migration of variable and function names to English.

## Next Steps

I plan to continue developing this project. Some of the planned implementations include:
- Migrating to a relational SQL database
- Keeping sessions active across program restarts
- Migrating from a console interface to a graphical interface