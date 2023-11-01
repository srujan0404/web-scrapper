from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def snapdeal(url):
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    # Getting the name of the product
    title_div = soup.find('h1', class_='pdp-e-i-head')
    product_name = title_div.text.strip()

    # Getting the price of the product
    price_span = soup.find('span', class_='pdp-final-price')
    price = price_span.text.strip()

    # Getting the name of the website
    website_source = "Snapdeal"

    print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')

    return price
