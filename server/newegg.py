import requests
from bs4 import BeautifulSoup

def fetch_newegg(query, agent):
    try:
        url = f"https://www.newegg.com/p/pl?d={query}"
        response = requests.get(url, headers={'User-Agent': agent})
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if the page is valid and contains products
        product = soup.find("div", class_="item-cell")
        if product is None:
            print("not even searching")
            return False 
        else:
            link_element = product.find("a", class_="item-img")
            title_element = product.find("a").find("img").get("title")
            price_elements = product.find("li", class_=("price-current"))
            dollars = price_elements.findChildren("strong")[0]
            cents = price_elements.findChildren("sup")[0]
            
            if link_element and title_element and price_elements:
               link = link_element['href'] 
               title = title_element
               price = dollars.get_text(strip=True) + cents.get_text(strip = True)
               item = {
                    'site': 'Newegg',
                    'link': f"{link}",
                    'item_title_name': title,
                    'price': price
                }
        return item
    except:
        return False