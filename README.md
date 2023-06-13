# Amazon Product Scraper

A Python script to scrape product details from Amazon product listing pages.

## Description

This script utilizes the Selenium library to scrape product information from Amazon. It navigates through the product listing pages, extracts details such as product URLs, names, prices, ratings, and review counts, and saves the data to an Excel file. The script also handles cases where certain elements may not be present by appending 'N/A' as a placeholder.

## Features

- Scrapes product details from Amazon product listing pages
- Extracts product URLs, names, prices, ratings, and review counts
- Handles cases where certain elements are not found
- Saves the extracted data to an Excel file
- Easy to configure and customize

## Requirements

- Python 3.x
- Selenium
- Pandas

## Installation

1. Clone the repository:

git clone https://github.com/your-username/amazon-product-scraper.git

2. Install the required dependencies:

pip install -r requirements.txt

## Usage

1. Configure the Selenium web driver by providing the path to the Chrome driver.
2. Open the desired Amazon product listing page by setting the `url` variable in the code.
3. Run the script:
python scrape.py

4. Wait for the scraping process to complete.
5. The extracted product data will be saved in an Excel file named `Amazon products.xlsx` in the current directory.



