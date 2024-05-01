import requests
from bs4 import BeautifulSoup

def fetch_walmart(query, agent):
    try:
        # Perform the search
        url = f"https://www.walmart.com/search?q={query}"
        response = requests.get(url, headers={'User-Agent': agent})
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
        return item
    except:
        return False