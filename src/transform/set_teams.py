import json

with open("data/clean_matches.json", "r") as file:
    clean_matches = json.load(file)


def set_teams(clean_matches):
    teams = {}

    for match in clean_matches:
        teams[match["home_team_id"]] = match["home_team_name"]
        teams[match["away_team_id"]] = match["away_team_name"]

    return teams


if __name__ == "__main__":
    teams = set_teams(clean_matches)

    print(teams)
    print(len(teams))