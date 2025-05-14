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

            info_list = {}
            
            if artist_name in name and " - " in name:
                if prices.string is not None:
                    artist = name.split(" - ")[0]
                    title = name.split(" - ")[1].split(",")[0]
                    price = prices.text.strip()
                    price = price.replace("€", "").replace(",", ".").strip()

                    for format_item in formats:
                        format = format_item.text
                        vinyl_format = ""

                        if "Vinyl" in format:
                            vinyl_format_details = format.replace("Format:", "").strip()
                            vinyl_format = vinyl_format_details.split(",")[0].strip()

                            
                            

                            if "Ir veikalā" in format:
                                avail = format.replace("Pieejamība:", "").strip()
                                info_list["availability"] = avail
                            if "Pārdots" in format:
                                sold = format.replace("Pieejamība:", "").strip()
                                info_list["availability"] = sold
                            
                            info_list["artist"] = artist
                            info_list["title"] = title
                            info_list["price"] = price
                            info_list["format"] = vinyl_format
                        
                            
                            self.products_info_list.append(info_list)
                            

    def printList(self):
        for product in self.products_info_list:
            print(f"Artist: {product['artist']}, Title: {product['title']}, Price: {product['price']} €, Format: {product['format']}")


    def isAlbumAvailable(self, album_title):
        for product in self.products_info_list:
            if product["title"] == album_title.title():
                return f"Album '{album_title}' is available" 
                
        return f"Album '{album_title}' is not available."

    def sortPrice(self, getVinylInfo):
        vinyl_list = self.products_info_list
        for i in range(len(vinyl_list)):
            for j in range(0, len(vinyl_list) - i - 1):
                if float(vinyl_list[j]['price']) > float(vinyl_list[j + 1]['price']):
                    vinyl_list[j], vinyl_list[j + 1] = vinyl_list[j + 1], vinyl_list[j]
    
        for product in vinyl_list:
            print(f"Artist: {product['artist']}, Title: {product['title']}, Price: {product['price']} €")
    
    def calculateAverageAlbumPrice(self, album_title):
        total_price = 0
        count = 0
        for product in self.products_info_list:
            if product["title"] == album_title.title():
                total_price += float(product["price"])
                count += 1
        avg_price = total_price / count
        print(f"Average price for album '{album_title}': {avg_price} €")

    def serachAlbum(self, album_title):
        for product in self.products_info_list:
            if product["title"] == album_title.title():
                print(f"Artist: {product['artist']}, Title: {product['title']}, Price: {product['price']} €, Format: {product['format']}")
        

        
        
        

input_artist = input("Enter artist name or album name: ").title().strip()
vinyl_info = Product()
vinyl_info.getVinylInfo(input_artist)

if len(vinyl_info.products_info_list) == 0:
    print(f"No results found for artist: {input_artist}")
    exit()

vinyl_info.printList()

print("Input: \n 1) Sorting by price \n 2) Check album availability \n 3) Check average preice of album \n 4) Search for album")
q_sortPrice = int(input("Enter your choice: "))

match q_sortPrice:
    case 1:
        vinyl_info.sortPrice(vinyl_info) 
    case 2:
        album_title = input("Enter album title: ").title().strip()
        print(vinyl_info.isAlbumAvailable(album_title))
    case 3:
        album_title = input("Enter album title: ").title().strip()
        print(vinyl_info.calculateAverageAlbumPrice(album_title))
    case 4:
        album_title = input("Enter album title: ").title().strip()
        vinyl_info.serachAlbum(album_title)
    case _:
        print("Invalid input")

    
