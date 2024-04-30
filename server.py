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
headers = {'User-Agent': random.choice(user_agents)}

items = []

def fetch_bestbuy(query):
    try:
        # Perform the search
        url = f"https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st={query}"
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
        return item
    except:
        return False
                
   

product_name = input("Enter the product name: ")
item = fetch_bestbuy(product_name)
print(item)


# def fetch_walmart(query):
    # url = f"https://www.walmart.com/search/?query={query}"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # title = soup.find('a', class_='product_title_class').get_text(strip=True)
    # price = soup.find('span', class_='price_class').get_text(strip=True)
    # return Item('Walmart', title, price)
# 
# def fetch_newegg(query):
    # url = f"https://www.newegg.com/p/pl?d={query}"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # title = soup.find('a', class_='item-title').get_text(strip=True)
    # price = soup.find('li', class_='price-current').get_text(strip=True)
    # return Item('Newegg', title, price)