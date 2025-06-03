import time
from browser import open_brave, close_brave
from friends import watch_episodes
from url_generator import generate_url

if __name__ == "__main__":

    # Construct the URL
    url = generate_url()
    print(f"Generated URL: {url}")

    # Open Brave with URL
    open_brave(url)
    
    # Wait for page to load
    time.sleep(5)
    
    # Start watching episodes in a loop
    watch_episodes(120)

    print("Exiting after 2 hours of watching.")
    close_brave()