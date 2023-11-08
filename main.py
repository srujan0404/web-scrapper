def compare_prices():
    price1 = None
    price = None
    cheapest = None

    for i in range(1, 3):
        website_url = input("Enter the URL of the product: ")
        if 'flipkart' in website_url:
            from flipkarts import flipkart
            price1 = flipkart(website_url)
        elif 'amazon' in website_url:
            from amazons import amazon
            price = amazon(website_url)
            
        elif 'shopclues' in website_url:
            from shopcluess import shopclues
            price = shopclues(website_url)
        elif 'snapdeal' in website_url:
            from snapdeals import snapdeal
            price = snapdeal(website_url)
        


    if price and price1:
        if price1 < price:
            cheapest = ("Flipkart", price1)
        elif price1 > price:
            cheapest = ("Amazon", price)
        else:
            cheapest = ("Both Amazon and Flipkart", price)  

        if cheapest:
            print(f'The product is cheapest at {cheapest[0]} for ₹{cheapest[1]}')

compare_prices()
