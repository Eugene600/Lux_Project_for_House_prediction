# Web Scraping BuyRentKenya Properties

## Overview

This project is a web scraper built using Python, BeautifulSoup, and the requests library. It scrapes property listings from the [BuyRentKenya](https://www.buyrentkenya.com) website for various property types, such as houses, apartments, and bedsitters, for both sale and rent. The scraped data is saved in a CSV file with detailed information on each property.

## Features

- Scrapes property listings (houses, apartments, bedsitters) for sale and rent.
- Extracts details such as location, size, number of bedrooms and bathrooms, and price.
- Saves the scraped data in a structured CSV format.
- Handles pagination to ensure all properties are scraped.

## Technologies Used

- **Python 3.x**: The programming language used for scripting.
- **BeautifulSoup (bs4)**: For parsing HTML and extracting relevant data.
- **requests**: For sending HTTP requests to fetch web pages.
- **CSV module**: To store the scraped data in a CSV file format.

## Installation

To set up and run this project, you'll need to have Python installed. Follow the instructions below to get started:

1. Clone this repository:
   ```bash
   git clone https://github.com//Eugene600/Lux_Project_for_House_prediction.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:
   ```
   requests
   beautifulsoup4
   lxml
   ```

## How It Works

The script navigates through specific property listing pages on the BuyRentKenya website, extracts relevant information, and writes it to a CSV file. Here's a breakdown of the steps:

1. **Send Request**: A GET request is sent to the property listing pages.
2. **Parse HTML**: BeautifulSoup parses the HTML content to find relevant property details.
3. **Extract Data**: Data such as location, size, number of bedrooms, bathrooms, and price are extracted.
4. **Pagination**: The script navigates through paginated results until all listings are scraped.
5. **Save to CSV**: The extracted data is saved into a CSV file (`scraped_buy_rent.csv`) with columns like location, size, bedrooms, bathrooms, price, property type, and purchase type.

### Data Fields

- **Location**: The general location of the property.
- **Other Location Details**: Additional details about the location (if available).
- **Size**: Size of the property (if available).
- **Bedrooms**: Number of bedrooms.
- **Bathrooms**: Number of bathrooms.
- **Price**: Property price (cleaned from special characters and commas).
- **Property Type**: Either "House", "Apartment", or "Bedsitter".
- **Purchase Type**: Either "Sale" or "Rent".

## Running the Scraper

To run the scraper, execute the following command in your terminal:

```bash
python my_scraper.py
```

This will start scraping the property listings and save the results to `scraped_buy_rent.csv` in the project folder.

## Example Output

The output CSV file will contain rows like:

| Location      | Other Location Details | Size   | Bedrooms | Bathrooms | Price  | Property Type | Purchase Type |
|---------------|------------------------|--------|----------|-----------|--------|---------------|---------------|
| Westlands     | Nairobi                 | 250 sqm| 3        | 2         | 100000 | Apartment     | Rent          |
| Lavington     | Nairobi                 | 400 sqm| 4        | 3         | 250000 | House         | Sale          |

## Error Handling

- The script gracefully handles any errors (such as failed requests or missing data) by printing an error message to the console and continuing with the next property or page.
- If no properties are found on a page, the script prints a message indicating so and skips to the next page.

## Future Enhancements

- Improve error handling to retry requests on failures.
- Add support for scraping additional property details, such as amenities or neighborhood information.
- Optionally integrate a database for more robust data storage and querying.
- Extend the scraper to handle additional websites or property listing platforms.
