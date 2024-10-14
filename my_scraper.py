import re
from bs4 import BeautifulSoup
import requests
import csv

def scraper(url, writer):
    try:
        # Parsing HTML
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        if 'houses-for-rent' in url:
            property_type = 'House'
            purchase_type = 'Rent'
        elif 'flats-apartments-for-rent' in url:
            property_type = 'Apartment'
            purchase_type = 'Rent'
        elif 'bedsitters-for-rent' in url:
            property_type = 'Bedsitter'
            purchase_type = 'Rent'
        elif 'houses-for-sale' in url:
            property_type = 'House'
            purchase_type = 'Sale'
        elif 'flats-apartments-for-sale' in url:
            property_type = 'Apartment'
            purchase_type = 'Sale'
        else:
            property_type = 'Unknown'
            purchase_type = "Unknown"

        properties = soup.find_all('div', class_='flex flex-col justify-between px-5 py-4 md:w-3/5')

        if not properties:
            print(f"No properties found on {url}")
            return

        for prop in properties:
            location = prop.find('p', class_="ml-1 truncate text-sm font-normal capitalize text-grey-650")
            size = prop.find('span', class_="whitespace-nowrap", attrs={'data-cy':"card-area"})
            bedroom = prop.find("span", class_="whitespace-nowrap font-normal", attrs={'data-cy':"card-beds"})
            bathroom = prop.find('span', class_="whitespace-nowrap font-normal", attrs={'data-cy':"card-bathrooms"})
            price = prop.find('p', class_="text-xl font-bold leading-7 text-grey-900").find('a', class_="no-underline")

            # Get location
            if location:
                location_text = location.text.strip()
                location_parts = location_text.split(",", 1)
                location_text = location_parts[0].strip()
                other_location_details = location_parts[1].strip() if len(location_parts) > 1 else ''
            else:
                location_text = "None"
                other_location_details = "None"

            size_text = size.text.strip() if size else 'None'
            bedroom_text = bedroom.text.strip() if bedroom else 'None'
            bathroom_text = bathroom.text.strip() if bathroom else 'None'
            price_text = price.text.strip() if price else 'None'

            # Cleaning price section
            match = re.search(r'(\d{1,3}(?:,\d{3})*)', price_text)
            if match:
                price_tag = match.group(0).replace(',', '')  # Remove commas from the price
            else:
                price_tag = 'Price not found'

            writer.writerow([location_text, other_location_details, size_text, bedroom_text, bathroom_text, price_tag, property_type, purchase_type])
    except Exception as e:
        print(f"Error fetching properties from {url}: {e}")

# Base URLs
base_urls = [
    'https://www.buyrentkenya.com/houses-for-rent',
    "https://www.buyrentkenya.com/flats-apartments-for-rent",
    "https://www.buyrentkenya.com/bedsitters-for-rent",
    "https://www.buyrentkenya.com/houses-for-sale",
    "https://www.buyrentkenya.com/flats-apartments-for-sale",
]

with open('scraped_buy_rent.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Location', 'Other Location Details', 'Size', 'Bedrooms', 'Bathrooms', 'Price', 'Property Type', 'Purchase Type'])

    for base_url in base_urls:
        page = 1
        while True:
            url = base_url if page == 1 else f'{base_url}?page={page}'
            print(f"Fetching data from {url}...")
            try:
                scraper(url, writer)
                page += 1

                # Checking for next page existence
                html_text = requests.get(url).text
                soup = BeautifulSoup(html_text, 'lxml')
                next_button_div = soup.find('div', class_="mt-4 flex w-full flex-row items-center justify-center space-x-1 md:space-x-3")
                
                if next_button_div:
                    next_button_link = next_button_div.find('svg', class_="fill-current transform -rotate-90 inline-block text-secondary w-3")
                    if not next_button_link:
                        break
                else:
                    break
            except Exception as e:
                print(f"Error fetching properties from {url}: {e}")
                break

print("File saved successfully")
