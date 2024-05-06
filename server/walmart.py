from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver(agent):
    """Configures and returns a Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--incognito")  # Opens Chrome in incognito mode.
    options.add_argument(f'user-agent={agent}')  # Sets a random user agent.
    driver = webdriver.Chrome(options=options)
    return driver

def fetch_walmart(query, agent):
    try:
        driver = setup_driver(agent)
        # Perform the search
        url = f"https://www.walmart.com/search?q={query}"
        driver.get(url)
        print(driver.page_source)
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-automation-id="product-title"]')))
        # Check if the page is valid and contains products
        product_element = driver.find_element(By.CSS_SELECTOR, '[data-automation-id="product-title"]')
        price_element = driver.find_element(By.CSS_SELECTOR, '[data-automation-id="product-price"]')
        item = {
            'site': 'Walmart',
            'link': driver.current_url,
            'item_title_name': product_element.text,
            'price': price_element.text
        }
        return item
    except Exception as e:
        print(f"Error fetching from Walmart: {e}")
    finally:
        driver.quit()
    return False