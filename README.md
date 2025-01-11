# quotes_scraper

Python script that scrapes random popular quotes from goodreads.com.

**Features:**

Scrapes 5 quotes from a random selection of goodreads.com popular quote pages.
Extracts quotes and authors (goodreads does not display book information at this time).
Implements basic rate limiting with a 2-second delay between requests to avoid overwhelming the server.
Duplicate quote prevention.

**Requirements:**

Python
requests
beautifulsoup4

**Installation:**

Clone this repository: git clone https://github.com/lindstho/quotes_scraper
Install required libraries: pip install requests beautifulsoup4

**Usage:**

Open a terminal window and navigate to the repository directory.
$ cd quotes_scraper
Run the script: python goodreads_quote_scraper.py
