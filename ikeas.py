from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def ikea(url):
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'html.parser')

    # Getting the name of the product
    title_h1 = soup.find('h1', class_='pip-header-section__title--big notranslate')
    product_name = title_h1.text.strip()

    # Getting the price of the product
    price_span = soup.find('span', class_='pip-temp-price__integer')
    price = price_span.text.strip()

    # Getting the name of the website
    website_source = "IKEA"

    print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')

    return price
