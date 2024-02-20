# Web Scraping Google Maps for Software Companies in Bangalore

This Python script utilizes Selenium to scrape Google Maps for software companies in Bangalore. It collects links to the search results and saves them to a CSV file.

## Requirements

- Python 3.x
- Selenium
- Pandas
- Chrome WebDriver (automatically installed using `webdriver_manager`)

## Usage

1. Make sure you have all the requirements installed.
2. Run the Python script `google_maps_scraper.py`.
3. The script will open Google Maps, search for software companies in Bangalore, scroll through the search results, collect links, and save them to a CSV file named `companies.csv`.

## Important Note

- Adjust the `options.headless` parameter in the script to run the browser in headless mode if needed.

## Author

[Sanjay Kumar A]
