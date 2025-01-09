import requests
from bs4 import BeautifulSoup
import random
import time

def get_random_page():
    return random.randint(1, 100)  # Goodreads only has 100 pages of popular quotes

def scrape_quotes(page_num):
    url = f"https://www.goodreads.com/quotes?page={page_num}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        time.sleep(2)  # Basic rate limiting for 2 seconds before next request
        return quote_elements
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_num}: {e}")
        return None

def extract_quote(quote_element):
    quote_text = quote_element.find("div", class_="quoteText").text.strip().split("―")[0].strip().replace('“', '').replace('”', '')
    author = quote_element.find("span", class_="authorOrTitle").text.strip()
    return {"quote": quote_text, "author": author} 

def main():
    num_quotes_to_display = 5 # Adjust to preference
    displayed_quotes = set()

    for _ in range(num_quotes_to_display):
        while True:
            page_num = get_random_page()
            quote_elements = scrape_quotes(page_num)
            if quote_elements:
                random_quote_element = random.choice(quote_elements)
                quote_data = extract_quote(random_quote_element)
                quote_tuple = (quote_data['quote'], quote_data['author'])
                if quote_tuple not in displayed_quotes:
                    displayed_quotes.add(quote_tuple)
                    break
            else:
                time.sleep(2)
                continue

        print("--------------------")
        print(f"{quote_data['quote']}")
        print(f"- {quote_data['author']}")
        time.sleep(1)

if __name__ == "__main__":
    main()