from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def myntra(url):
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Getting the name of the product
        title_element = soup.find('h1', class_='pdp-title')  # Update the class to match the actual HTML structure
        product_name = title_element.text.strip() if title_element else "Product name not found"

        # Getting the price of the product
        price_element = soup.find('span', class_='pdp-mrp')  # Update the class to match the actual HTML structure
        price = price_element.text.strip() if price_element else "Price not found"

        # Getting the name of the website
        website_source = "Myntra"

        print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')

        return price
    else:
        print(f'Failed to fetch the webpage. The status code was {response.status_code}')
        return None
