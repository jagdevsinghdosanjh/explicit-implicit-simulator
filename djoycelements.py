import requests
from bs4 import BeautifulSoup
import os
import json
from urllib.parse import urljoin, urlparse

BASE_URL = "https://mathcs.clarku.edu/~djoyce/"
OUTPUT_DIR = "dejoyce"
JSON_OUTPUT = "djoyce.json"

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_valid_link(href):
    return href and not href.startswith("mailto:") and not href.startswith("javascript:")

def download_page(url):
    print(f"Fetching: {url}")
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def save_html(content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def extract_links(soup, base_url):
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        if is_valid_link(href) and urlparse(full_url).netloc == urlparse(base_url).netloc:
            links.append(full_url)
    return list(set(links))  # Remove duplicates

def scrape_site(start_url):
    visited = set()
    queue = [start_url]
    index = {}

    while queue:
        current_url = queue.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            html = download_page(current_url)
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string if soup.title else "Untitled"
            filename = os.path.join(OUTPUT_DIR, urlparse(current_url).path.split("/")[-1] or "index.html")
            save_html(html, filename)

            index[current_url] = {
                "title": title,
                "local_file": filename
            }

            new_links = extract_links(soup, current_url)
            queue.extend([link for link in new_links if link not in visited])
        except Exception as e:
            print(f"Error fetching {current_url}: {e}")

    # Save index as JSON
    with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"\n✅ Download complete. {len(index)} pages saved.")
    print(f"📁 HTML files in: {OUTPUT_DIR}")
    print(f"📜 Index saved to: {JSON_OUTPUT}")

# Run the scraper
scrape_site(BASE_URL)
