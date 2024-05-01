import requests
from bs4 import BeautifulSoup
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]
headers = {}
items = []

def fetch_bestbuy(query):
    try:
        # Perform the search
        url = f"https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st={query}"
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if the page is valid and contains products
        if "undefined - Best Buy" in soup.title.text:
            return False 
        else:
            product = soup.find("li", class_="sku-item")
            link_element = product.find("a", class_="image-link")
            title_element = product.find("h4", class_="sku-title")
            price_element = product.find("div", class_=["priceView-hero-price","priceView-customer-price"]).findChildren()[0]
            if link_element and title_element and price_element:
                link = link_element['href'] 
                title = title_element.get_text(strip=True)
                price = price_element.get_text(strip=True)
                item = {
                    'site': 'BestBuy',
                    'link': f"https://www.bestbuy.com{link}&intl=nosplash",
                    'item_title_name': title,
                    'price': price
                }
        items.append(item)
        return item
    except:
        return False
                

def fetch_walmart(query):
    try:
        # Perform the search
        url = f"https://www.walmart.com/search?q={query}"
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if the page is valid and contains products
        product = soup.find("div", class_="h-100 pb1-xl pr4-xl pv1 ph1")
        if product is None:
            return False 
        else:
            link_element = product.find("a", class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
            title_element = product.find("span", class_="w_iUH7")
            price_elements = product.find("div", class_=("mr1 mr2-xl b black lh-copy f5 f4-l")).findChildren()
            dollars = price_elements[2]
            cents = price_elements[3]
            if link_element and title_element and len(price_elements) >= 4:
               link = link_element['href'] 
               title = title_element.get_text(strip=True)
               price = dollars.get_text(strip=True) + "." + cents.get_text(strip = True)
               item = {
                   'site': 'Walmart',
                   'link': f"{link}",
                   'item_title_name': title,
                   'price': price
               }
        items.append(item)
        return item
    except:
        return False

def fetch_newegg(query):
    try:
        # Perform the search
        url = f"https://www.walmart.com/search?q={query}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if the page is valid and contains products
        product = soup.find("div", class_="h-100 pb1-xl pr4-xl pv1 ph1")
        if product is None:
            return False 
        else:
            link_element = product.find("a", class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
            title_element = product.find("span", class_="w_iUH7")
            price_elements = product.find("div", class_=("mr1 mr2-xl b black lh-copy f5 f4-l")).findChildren()
            dollars = price_elements[2]
            cents = price_elements[3]
            if link_element and title_element and len(price_elements) >= 4:
               link = link_element['href'] 
               title = title_element.get_text(strip=True)
               price = dollars.get_text(strip=True) + "." + cents.get_text(strip = True)
               item = {
                   'site': 'Newegg',
                   'link': f"{link}",
                   'item_title_name': title,
                   'price': price
               }
        items.append(item)
        return item
    except:
        return False


product_name = input("Enter the product name: ")
fetch_walmart(product_name)
fetch_bestbuy(product_name)
# item = fetch_newegg(product_name)
for item in items:
    print(item)