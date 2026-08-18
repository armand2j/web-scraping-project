import requests
import json
import psycopg2 as pg

# uri = "https://api.football-data.org/v4/matches"
# headers = {"X-Auth-Token": "63f93cc0883045b18ed730335a16f895"}

# response = requests.get(uri, headers=headers)

# for match in response.json()["matches"]:
#     print(match)

connection = pg.connect(
    database="python",
    user="postgres",
    password="Armando10122008",
    host="localhost",
    port="5432",
)


with open("data/clubs.json", encoding="utf-8") as f:
    clubs: list = json.load(f)
    string = json.dumps(clubs, indent=2, ensure_ascii=False)
    # print(string)


cursor = connection.cursor()
cursor.execute("""DROP TABLE IF EXISTS test;
""")

connection.commit()
