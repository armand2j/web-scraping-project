import requests
import json
import psycopg2 as pg

connection = pg.connect(
    database="python",
    user="postgres",
    password="Armando10122008",
    host="localhost",
    port="5432",
)


clubs_list: list = []

with open("data/clubs.json") as f:
    clubs_list = json.load(f)


cursor = connection.cursor()

# for club in clubs_list:
#     name = club["name"]
#     location = club["location"]
#     stadium = club["stadium"]
#     manager = club["manager"]

#     cursor.execute(f"""
#         INSERT INTO clubs (name, location, stadium, manager)
#         VALUES ('{name}', '{location}', '{stadium}', '{manager}')
#     """)


connection.commit()
