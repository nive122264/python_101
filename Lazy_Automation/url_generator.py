from dotenv import load_dotenv
import os
import random


def generate_url():
    load_dotenv()

    base_url = os.getenv("BASE_URL")
    season = random.randint(1, 10)
    episode = random.randint(1, 20)

    url = f"{base_url.rstrip('/')}/episode/friends-season-{season}-episode-{episode}"
    print(f"Trying to play: Season {season}, Episode {episode}")

    return url
