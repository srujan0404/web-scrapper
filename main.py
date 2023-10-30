import requests
from bs4 import BeautifulSoup

def get_product_info(product_name, websites):
    product_data = []

    for website, url in websites.items():
        response = requests.get(url.format(product_name))

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Implement the logic to check if the product is found on the website
            if is_product_found(website, soup):
                product_price = get_product_price(website, soup)
                product_data.append({
                    'Website': website,
                    'Product Name': product_name,
                    'Product Price': product_price
                })
            else:
                product_data.append({
                    'Website': website,
                    'Product Name': product_name,
                    'Product Price': 'Product not found on this website'
                })
        else:
            product_data.append({
                'Website': website,
                'Product Name': product_name,
                'Product Price': 'Failed to retrieve data from this website'
            })

    return product_data

def is_product_found(website, soup):
    if website == 'amazon':
        # Check if the product is found on Amazon (based on its HTML structure)
        return bool(soup.find("span", {"id": "priceblock_ourprice"}))
    elif website == 'flipkart':
        # Check if the product is found on Flipkart (based on its HTML structure)
        return bool(soup.find("div", {"class": "_30jeq3"}))
    return False  # If the website is not recognized

def get_product_price(website, soup):
    if website == 'amazon':
        # Extract and return the product price from Amazon
        price_element = soup.find("span", {"id": "priceblock_ourprice"})
        if price_element:
            return price_element.get_text()
    elif website == 'flipkart':
        # Extract and return the product price from Flipkart
        price_element = soup.find("div", {"class": "_30jeq3"})
        if price_element:
            return price_element.get_text()
    return 'Price not found'  # If the website is not recognized

if __name__ == '__main__':
    product_name = input("Enter the name of the product: ")
    num_websites = int(input("How many websites do you want to compare? "))
    
    websites = {}
    
    for i in range(num_websites):
        website_name = input(f"Enter the name of Website {i + 1}: ")
        website_url = input(f"Enter the URL of Website {i + 1}: ")
        websites[website_name] = website_url

    product_info = get_product_info(product_name, websites)

    print("\nPrice Comparison Results:")
    for item in product_info:
        print(f"Website: {item['Website']}")
        print(f"Product Name: {item['Product Name']}")
        print(f"Product Price: {item['Product Price']}\n")
