import requests
import json

uri = "https://api.football-data.org/v4/teams/81"
headers = {"X-Auth-Token": "63f93cc0883045b18ed730335a16f895"}

response: requests.Response = requests.get(uri, headers=headers)

barca = response.json()

for player in barca["squad"]:
    print(player["name"])

print(barca["coach"]["name"])

# with open("data/football_data/team.json", "w") as f:
#     json.dump(response.json(), f, indent=2)

# print(team_response.json())

# for match in team_response.json():
#     print(team_response)
