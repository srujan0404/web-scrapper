from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def scrape_amazon(url, user_agent):
    max_attempts = 1000  # Set the maximum number of retry attempts
    for _ in range(max_attempts):
        response = requests.get(url, headers=user_agent)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            name_element = soup.find('span', class_='a-size-large product-title-word-break')
            price_element = soup.find('span', class_='a-price-whole')
            if price_element:
                price = price_element.get_text()
                name = name_element.get_text()
                return price.strip(), name.strip()
        # Wait or use a retry delay here if needed
    return None, None

def amazon(url):
    price, product_name = scrape_amazon(url, header)
    if price and product_name:
        website_source = "Amazon"
        print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')
        return float(price.replace(',',''))
    else:
        print("Failed to retrieve data from Amazon.")
