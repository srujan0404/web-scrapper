from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}


def amazon(url):
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    # Getting the name of the product
    title_div = soup.find('div', id='titleSection')
    title_h1 = title_div.find('h1', id='title').text.strip()
    product_name = title_h1

    # Getting the price of the product
    price_span = soup.find('span', class_='a-price-whole')
    price = price_span.text.strip()

    # Getting the name of website
    website_source = soup.find('title')
    website_source = website_source.text.strip().split(' ')[-1]

    print(
        f'The Product: {product_name} is available at {website_source} for Rs.{price}')

    return price