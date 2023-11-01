def compare_prices():
    price1 = 0
    price = 0

    for i in range(1, 3):
        website_url = input("Enter the URL of the product: ")
        if 'flipkart' in website_url:
            from flipkarts import flipkart
            price1 = flipkart(website_url)
        elif 'amazon' in website_url:
            from amazons import amazon
            price = amazon(website_url)
        elif 'jiomart' in website_url:
            from jiomarts import jiomart
            jiomart(website_url)
    if price and price1:
        price1 = price1.replace('₹', '')
        price1 = price1.replace(',', '')
        price = price.replace(',', '')
        price = price.replace('.', '')

        if int(price) > int(price1):
            print(f'The Product is cheaper at Flipkart for ₹{price1}')
        elif int(price) < int(price1):
            print(f'The Product is cheaper at Amazon for ₹{price}')


    

compare_prices()