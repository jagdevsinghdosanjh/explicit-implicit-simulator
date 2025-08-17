import os
import json
from bs4 import BeautifulSoup
import re

INPUT_DIR = "djoyce"
OUTPUT_JSON = "djoyce.json"

def parse_title(soup):
    title = soup.title.string if soup.title else ""
    match = re.search(r'Book\s+([IVXLCDM]+)\s+Proposition\s+(\d+)', title)
    if match:
        return match.group(1), match.group(2)
    return None, None

def extract_statement(soup):
    h2 = soup.find("h2")
    return h2.get_text(strip=True) if h2 else "Untitled Proposition"

def extract_diagram(soup):
    img = soup.find("img")
    return img['src'] if img and 'src' in img.attrs else None

def extract_commentary(soup):
    paragraphs = soup.find_all("p")
    commentary = []
    for p in paragraphs:
        text = p.get_text(strip=True)
        if text and not text.startswith("Return to"):
            commentary.append(text)
    return " ".join(commentary)

def symbolic_tag(statement):
    # Simple symbolic mapping (expandable)
    if "equilateral triangle" in statement.lower():
        return "△"
    elif "right angle" in statement.lower():
        return "∠"
    elif "circle" in statement.lower():
        return "◯"
    return None

def parse_all_files():
    data = []
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".html"):
            path = os.path.join(INPUT_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                book, prop = parse_title(soup)
                statement = extract_statement(soup)
                diagram = extract_diagram(soup)
                commentary = extract_commentary(soup)
                symbol = symbolic_tag(statement)

                entry = {
                    "book": book,
                    "proposition": prop,
                    "statement": statement,
                    "diagram": diagram,
                    "commentary": commentary,
                    "symbolic_overlay": symbol
                }
                data.append(entry)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Parsed {len(data)} propositions into {OUTPUT_JSON}")

# Run parser
parse_all_files()
