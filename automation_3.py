import os
import re
import shutil
import urllib.request

URL = "https://www.youtube.com/"
TARGET_DIR = "./web_scrapes"
TEMP_FILE = "temp_title.txt"
FINAL_FILE = "scraped_title.txt"

def automate_scraping():
    try:
        with urllib.request.urlopen(URL, timeout=10) as response:
            html_content = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Error: {e}")
        return

    title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE | re.DOTALL)
    
    if title_match:
        page_title = title_match.group(1).strip()
    else:
        print("Could not find a <title> tag.")
        return

    with open(TEMP_FILE, "w", encoding="utf-8") as file:
        file.write(f"URL: {URL}\nTitle: {page_title}\n")

    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    destination_path = os.path.join(TARGET_DIR, FINAL_FILE)
    
    try:
        shutil.move(TEMP_FILE, destination_path)
        print(f"Success! Saved to {destination_path}")
    except Exception as e:
        print(f"Error moving file: {e}")
        if os.path.exists(TEMP_FILE):
            os.remove(TEMP_FILE)

if __name__ == "__main__":
    automate_scraping()