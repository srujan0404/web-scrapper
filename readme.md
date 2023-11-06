# Price Comparison Web Scraper

This Python project allows you to compare prices of a product from different e-commerce websites, including Amazon, Flipkart, Myntra, Ikea, ShopClues, Snapdeal, and JioMart.

## Project Structure

The project consists of several Python scripts for scraping product information from different e-commerce websites:

- `amazons.py`: Scrapes product information from Amazon.
- `flipkarts.py`: Scrapes product information from Flipkart.
- `myntras.py`: Scrapes product information from Myntra.
- `ikeas.py`: Scrapes product information from Ikea.
- `shopcluess.py`: Scrapes product information from ShopClues.
- `snapdeals.py`: Scrapes product information from Snapdeal.
- `jiomarts.py`: Scrapes product information from JioMart.

The main script, `main.py`, allows you to enter the URL of the product you want to compare, and it will fetch and display the product information from the respective website. After providing URLs from two different websites, the script will compare the prices and inform you which website offers the product at a better price.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/srujan0404/web-scrapper
   cd web-scrapper

2. install packages:

    ```bash
    pip install requests
    pip install beautifulsoup4

3. Run the main script:

    ```bash
    python main.py


**EXAMPLE**

``````
python main.py

Enter the URL of the product: https://www.amazon.in/product123

Enter the URL of the product: https://www.flipkart.com/product123

Example output: The Product is cheaper at Flipkart for ₹199

``````

