import requests
from bs4 import BeautifulSoup

url = 'https://api.hahow.in/api/homepage/latestIncubating'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    data = response.json()
    for item in data:
        title = item.get('title', 'No Title')  # Safely get title
        price_info = item.get('basePricingInfo', {})  # Get pricing dictionary
        price = price_info.get('preOrderedPrice', 'No Price')  # Extract pre-ordered price
        
        print(f"Course: {title} | Price: {price} TWD")

else:
    print('unsuccessful')