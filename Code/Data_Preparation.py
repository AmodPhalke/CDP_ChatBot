import requests
from bs4 import BeautifulSoup
import time
import random

def fetch_and_save_clean_docs(doc_info):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for platform, (url, filename) in doc_info.items():
        attempt = 0
        while attempt < 3:  # Retry a few times in case of failure
            try:
                print(f"Fetching documentation for {platform}...")
                response = requests.get(url, headers=headers)
                response.raise_for_status()

                # Parse HTML content
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract specific sections (e.g., main content area)
                main_content = soup.find('main')  # Adjust based on actual HTML structure
                if main_content:
                    text_content = main_content.get_text(separator="\n")
                else:
                    text_content = soup.get_text(separator="\n")  # Fallback to full text

                # Clean text: remove excessive newlines or blank lines
                clean_text = "\n".join([line.strip() for line in text_content.splitlines() if line.strip()])

                # Additional cleanup: remove footer-like content or irrelevant sections (if needed)
                clean_text = clean_text.split("footer")[0]  # Example of removing footer content

                # Save cleaned text to file
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(clean_text)
                print(f"Saved cleaned {platform} documentation to {filename}.")
                break  # Exit retry loop if successful

            except requests.exceptions.RequestException as e:
                attempt += 1
                print(f"Error fetching {platform} documentation (Attempt {attempt}): {e}")
                time.sleep(random.uniform(1, 3))  # Randomized backoff before retrying

        if attempt == 3:
            print(f"Failed to fetch documentation for {platform} after 3 attempts.")

# Documentation URLs and corresponding filenames
documentation = {
    "Segment": ("https://segment.com/docs/?ref=nav", "Segment_Docs.txt"),
    "mParticle": ("https://docs.mparticle.com/", "mParticle_Docs.txt"),
    "Lytics": ("https://docs.lytics.com/", "Lytics_Docs.txt"),
    "Zeotap": ("https://docs.zeotap.com/home/en-us/", "Zeotap_Docs.txt")
}

fetch_and_save_clean_docs(documentation)
