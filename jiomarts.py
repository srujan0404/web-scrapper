from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

def jiomart(url):
    html_text = requests.get(url, headers=header).text
    soup = BeautifulSoup(html_text, 'lxml')
    title_div = soup.find('div', id='pdp_product_name')
    product_name = title_div.text.strip()
    
    price_div = soup.find('div', class_='product-price-offer-box')
    price_span = price_div.find('span', class_='jm-heading-xs jm-ml-xxs')
    
    if price_span is not None:
        price = price_span.text.strip()
        print(price)
    else:
        print("Price not found on the page.")
