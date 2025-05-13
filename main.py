import requests
from bs4 import BeautifulSoup



# link = f"https://vinylla.lv/index.php?route=product/search&filter_name={input_artist}"

# link = "https://vinylla.lv/index.php?route=product/search&filter_name=radiohead"
# page = requests.get(link)

def getVinylPrices(artist):
    link = f"https://vinylla.lv/index.php?route=product/search&filter_name={artist}"
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")

    products = soup.find_all("div", class_="product")

    product_list = []

    for product in products:

        names = product.find("div", class_ = "name")
        name = names.string
        prices = product.find("div", class_ = "price")


        product_dict = {}
        if input_artist in name and " - " in name:
            if prices.string is not None:
                artist = name.split(" - ")[0]
                title = name.split(" - ")[1].split(",")[0]
                price = prices.string.strip()
            

            product_dict["artist"] = artist
            product_dict["title"] = title
            product_dict["price"] = price
        
        print(product_dict)

        # if "Radiohead" in name:
        #     if prices.string is not None:
        #         artist = name.split(" - ")[0]
        #         title = name.split(" - ")[1].split(",")[0]
        #         price = prices.string.strip()
        
        
        


input_artist = input("Enter artist name: ").title().strip()
getVinylPrices(input_artist)
   
    





    