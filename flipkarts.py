from bs4 import BeautifulSoup
import requests

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}


def flipkart(url):
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    # Getting the name of the product
    title_div = soup.find('span', class_='B_NuCI')
    title = title_div.text.strip()
    product_name = title

    # Getting the price of the product
    price_div = soup.find('div', class_='_30jeq3 _16Jk6d')
    price = price_div.text.strip()

    print(f'The Product: {product_name} is available at Flipkart for {price}')

    return price