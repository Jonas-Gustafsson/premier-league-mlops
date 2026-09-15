import os
import psycopg
import json
from dotenv import load_dotenv
from src.transform.set_teams import set_teams

with open("data/clean_matches.json", "r") as file:
    clean_matches = json.load(file)

teams = set_teams(clean_matches)
print(teams)

load_dotenv()

db_host=os.getenv("DB_HOST")
db_port=os.getenv("DB_PORT")
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")

connection = psycopg.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

cursor = connection.cursor()

for match in clean_matches:
    cursor.execute(
        """
        INSERT INTO matches (
            match_id,
            season_id,
            season_year,
            date,
            matchday,
            home_team_id,
            away_team_id,
            home_goals,
            away_goals,
            winner,
            referee_name
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (match_id)
        DO UPDATE SET
            season_id = EXCLUDED.season_id,
            season_year = EXCLUDED.season_year,
            date = EXCLUDED.date,
            matchday = EXCLUDED.matchday,
            home_team_id = EXCLUDED.home_team_id,
            away_team_id = EXCLUDED.away_team_id,
            home_goals = EXCLUDED.home_goals,
            away_goals = EXCLUDED.away_goals,
            winner = EXCLUDED.winner,
            referee_name = EXCLUDED.referee_name;
        """,
        (
            match["match_id"],
            match["season_id"],
            match["season_year"],
            match["date"],
            match["matchday"],
            match["home_team_id"],
            match["away_team_id"],
            match["home_goals"],
            match["away_goals"],
            match["winner"],
            match["referee_name"]
        )
    )

connection.commit()

connection.commit()
cursor.execute("SELECT * FROM teams;")

rows = cursor.fetchall()

print(rows)

cursor.close()

connection.close()
