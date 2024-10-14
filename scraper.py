# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Base URLs
# page_1 = 'https://www.buyrentkenya.com/property-for-rent/nairobi'
# base_url = 'https://www.buyrentkenya.com'
# page_base_url = "https://www.buyrentkenya.com/property-for-rent/nairobi?page="

# # Lists to store data
# Location = []
# Price = []
# Bedrooms = []
# Bathrooms = []
# Amenities = []

# def fetch_page(page):
#     if page == 1:
#         page_url = page_1
#     else:
#         page_url = f'{page_base_url}{page}'

#     page_response = requests.get(page_url)
#     if page_response.status_code != 200:
#         print(f"Page: {page} request failed")
#         return []
    
#     page_soup = BeautifulSoup(page_response.text, "lxml")
#     houses = page_soup.find_all('div', class_='flex flex-col gap-y-3 w-full md:w-4/5')
    
#     page_data = []
    
#     for house in houses:
#         try:
#             url = house.find('h2', class_='font-semibold md:hidden').find('a', class_='no-underline')['href']
#             house_url = base_url + url
#             house_response = requests.get(house_url)
#             if house_response.status_code != 200:
#                 print(f"House: {house_url} request failed")
#                 continue

#             house_soup = BeautifulSoup(house_response.text, 'lxml')

#             # Extract information
#             location = house_soup.find('p', class_='hidden items-center text-sm text-gray-500 md:flex')
#             location = location.text.strip() if location else None

#             price = house_soup.find('span', class_='block text-right text-xl font-semibold leading-7 md:text-xxl md:font-extrabold')
#             price = price.text.strip().strip('KSh') if price else None

#             bedrooms = house_soup.find('span', class_='flex h-6 max-w-24 items-center rounded-2xl bg-highlight px-3 py-2 mr-5 font-bold')
#             bedrooms = bedrooms.text.strip() if bedrooms else None

#             bathrooms = house_soup.find('span', class_='flex h-6 max-w-24 items-center rounded-2xl bg-highlight px-3 py-2 font-bold')
#             bathrooms = bathrooms.text.strip() if bathrooms else None

#             description = house_soup.find('div', class_='my-3 overflow-hidden bg-white rounded-2xl md:rounded-0 p-3 md:px-0')
#             description = description.text.strip() if description else None

#             features = house_soup.find_all('ul', class_='flex flex-row flex-wrap items-center')
#             amenities = []
#             feat_no = 0
#             for feature in features:
#                 if feat_no == 2:
#                     break
#                 amenity = feature.find_all('li', class_='flex')
#                 for item in amenity:
#                     amenities.append(item.text.strip('\n\n|'))
#                 feat_no += 1
#             amenities = sorted(amenities) if amenities else []

#             # Append to page data
#             page_data.append({
#                 "Location": location,
#                 "Price": price,
#                 "Bedrooms": bedrooms,
#                 "Bathrooms": bathrooms,
#                 "Amenities": amenities,
#             })

#         except Exception as e:
#             print(f"Error processing house on page {page}: {e}")

#     print(f'Page: {page} Done')
#     return page_data

# # Use ThreadPoolExecutor to fetch pages concurrently
# with ThreadPoolExecutor(max_workers=10) as executor:
#     futures = [executor.submit(fetch_page, page) for page in range(1, 428)]
    
#     for future in as_completed(futures):
#         page_data = future.result()
#         for house_data in page_data:
#             Location.append(house_data["Location"])
#             Price.append(house_data["Price"])
#             Bedrooms.append(house_data["Bedrooms"])
#             Bathrooms.append(house_data["Bathrooms"])
#             Amenities.append(house_data["Amenities"])

# # Create DataFrame and save to CSV
# data = {
#     "Location": Location, 
#     "Bedrooms": Bedrooms, 
#     "Bathrooms": Bathrooms,
#     "Amenities": Amenities,
#     "Price": Price,
# }
# df = pd.DataFrame(data)
# df.to_csv('buyrentke.csv', index=False)
# print('===================\nDone Extracting\n===================')