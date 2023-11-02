from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def myntra(url):
    try:
        response = requests.get(url, headers=header)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            # Getting the name of the product
            title_div = soup.find('h1', class_='pdp-title')
            product_name = title_div.text.strip()

            # Getting the price of the product
            price_span = soup.find('span', class_='pdp-mrp')
            price = price_span.text.strip()

            # Getting the name of the website
            website_source = "Myntra"

            print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')

            return price
        else:
            print(f'Failed to fetch the webpage. The status code was {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None