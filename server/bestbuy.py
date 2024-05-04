import requests
from bs4 import BeautifulSoup

def fetch_bestbuy(query, agent):
    try:
        # Perform the search
        url = f"https://www.bestbuy.com/site/searchpage.jsp?intl=nosplash&st={query}"
        response = requests.get(url, headers={'User-Agent': agent})
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