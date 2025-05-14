import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self):
        self.products_info_list = []
        self.product_dict = {}

    def getVinylInfo(self, artist_name):

        link = f"https://vinylla.lv/index.php?route=product/search&filter_name={artist_name}"
        page = requests.get(link)
        soup = BeautifulSoup(page.text, "html.parser")
        

        products = soup.find_all("div", class_="product")


        for product in products:

            

            names = product.find("div", class_ = "name")
            name = names.text
            prices = product.find("div", class_ = "price")
            attributes = product.find("ul", class_ = "attribute")
            if attributes:
                formats = attributes.find_all("li")
            else:
                formats = []


            
            if artist_name in name and " - " in name:
                if prices.string is not None:
                    artist = name.split(" - ")[0]
                    title = name.split(" - ")[1].split(",")[0]
                    price = prices.text.strip()
                    price = price.replace("€", "").replace(",", ".").strip()

                    for format_item in formats:
                        format = format_item.text
                        vinyl_format = ""
                        info_list = {}
                        if "Vinyl" in format:
                            vinyl_format_details = format.replace("Format:", "").strip()
                            vinyl_format = vinyl_format_details.split(",")[0].strip()

                            info_list["artist"] = artist
                            info_list["title"] = title
                            info_list["price"] = price
                            info_list["format"] = vinyl_format
                            

                            if "Ir veikalā" in format:
                                avail = format.replace("Pieejamība:", "").strip()
                                info_list["availability"] = avail
                            if "Pārdots" in format:
                                sold = format.replace("Pieejamība:", "").strip()
                                info_list["availability"] = sold
                        
                        
                        self.products_info_list.append(info_list)
                            

        if len(self.products_info_list) == 0:
            print(f"No results found for artist: {artist_name}")
            return

    def printList(self):
        for product in self.products_info_list:
            print(f"Artist: {product['artist']}, Title: {product['title']}, Price: {product['price']} €")


    def isAlbumAvailable(self, album_title):
        for product in self.products_info_list:
            if product["title"] == album_title.title():
                return f"Album '{album_title}' is available for {product['price']} €." 
                
        return f"Album '{album_title}' is not available."

    def sortPrice(self, getVinylInfo):
        vinyl_list = self.products_info_list
        for i in range(len(vinyl_list)):
            for j in range(0, len(vinyl_list) - i - 1):
                if float(vinyl_list[j]['price']) > float(vinyl_list[j + 1]['price']):
                    vinyl_list[j], vinyl_list[j + 1] = vinyl_list[j + 1], vinyl_list[j]
    
        for product in vinyl_list:
            print(f"Artist: {product['artist']}, Title: {product['title']}, Price: {product['price']} €")
        
        

        
        
        

input_artist = input("Enter artist name: ").title().strip()
vinyl_info = Product()
vinyl_info.getVinylInfo(input_artist)

print("Input: \n 1) Sorting by price \n 2) Print list \n 3) Check album availability \n")
q_sortPrice = int(input("Enter your choice: "))

match q_sortPrice:
    case 1:
        vinyl_info.sortPrice(vinyl_info)
    case 2:
        vinyl_info.printList()
    case 3:
        album_title = input("Enter album title: ").title().strip()
        print(vinyl_info.isAlbumAvailable(album_title))
    case _:
        print("Invalid input")

    





    
