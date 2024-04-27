import requests
from bs4 import BeautifulSoup

# Global list to store all items
bestbuy_items = []

proxy = {
    'http': "username:password@host",
    'https': "username:password@host"
}

def fetch_bestbuy(query):
    current_page = 1
    proceed = True
    
    while proceed and current_page < 3:
        # Modified URL to include page number
        url = f"https://www.bestbuy.com/site/searchpage.jsp?cp={current_page}&st={query}"
        page = requests.get(url, proxies=proxy)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        # Check if the page is valid and contains products
        if "undefined - Best Buy" in soup.title.text or not soup.find_all('li', class_="sku-item"):
            proceed = False
        else:
            cp_products = soup.find_all("li", class_="sku-item")
            for product in cp_products:
                # Corrected to find elements within each product
                title_element = product.find("img").attrs["alt"]
                price_element = product.find("class",class_ = "sr-only")

                print(title_element)
                print(price_element)
                if title_element and price_element:
                    title = title_element.get_text(strip=True)
                    price = price_element.get_text(strip=True)
                    item = {
                        'site': 'BestBuy',
                        'item_title_name': title,
                        'price': price
                    }
                    bestbuy_items.append(item)
            current_page += 1

    return bestbuy_items

# Example usage
product_name = input("Enter the product name: ")
fetch_bestbuy(product_name)
for item in bestbuy_items:
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