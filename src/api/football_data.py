from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.football-data.org/v4/competitions/PL/matches"

headers = {"X-Auth-Token": api_key}



def get_matches(season):
    params={
        "season": season
    }

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    print(response.status_code)

    data = response.json()

    matches = data["matches"]


    return matches

if __name__ == "__main__":
    seasons = [2023, 2024, 2025]
    all_matches = []
    for season in seasons:
        print(f"Hämtar säsong {season}")
        matches = get_matches(season)
        all_matches.extend(matches)
    
    print(f"Totalt antal matcher: {len(all_matches)}")

    with open("data/raw_matches.json", "w") as file:
        json.dump(all_matches, file, indent=4)