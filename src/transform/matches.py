import json

with open("data/raw_matches.json", "r") as file:
    matches = json.load(file)


def transform_match(match):
    clean_match = {
        "match_id": match["id"],
        "season": match["season"]["id"],
        "date": match["utcDate"],
        "matchday": match["matchday"],
        "home_team_id": match["homeTeam"]["id"],
        "home_team_name": match["homeTeam"]["name"],
        "away_team_id": match["awayTeam"]["id"],
        "away_team_name": match["awayTeam"]["name"],
        "home_goals": match["score"]["fullTime"]["home"],
        "away_goals": match["score"]["fullTime"]["away"],
        "winner": match["score"]["winner"],
        "referee_name": match["referees"][0]["name"]
    }

    return clean_match


def transform_matches(matches):
    clean_matches = []

    for match in matches:
        clean_match = transform_match(match)
        clean_matches.append(clean_match)

    return clean_matches


def save_matches(clean_matches):
    with open("data/clean_matches.json", "w") as file:
        json.dump(clean_matches, file, indent=4)
        

if __name__ == "__main__":
    clean_matches = transform_matches(matches)
    save_matches(clean_matches)
    print(len(clean_matches))