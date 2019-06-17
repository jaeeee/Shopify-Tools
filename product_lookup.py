import requests
import json

def findproduct( link, product ):
    bro = product
    url = link + '/products.json'
    r = requests.get(url)
    products = json.loads((r.text))['products']
    for product in products:
        productName = product['title']
        searchA = productName.lower()
        searchB = bro.lower()
        if (searchA.find(searchB) != -1):
            print(productName)
            producturl = link + "/products/" + product['handle']
            print(producturl)
bruv = input("Enter website url: ")
yes = input("Enter product name: ")
findproduct(bruv, yes)
