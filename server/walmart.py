from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def init_driver(agent):
    """Configures and returns a Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--incognito")  # Opens Chrome in incognito mode.
    options.add_argument(f'user-agent={agent}')  # Sets a random user agent.
    service = Service('C:\\Users\\gilad\\Computer_Science\\Third_year\\Semester B\\From idea to reality\\Assignment2\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def fetch_walmart(query, agent):
    try:
        driver = init_driver(agent)
        # Perform the search
        url = f"https://www.walmart.com/search?q={query}"
        driver.get(url)
        driver.execute_script("window.scrollTo(0, 100)")  
        driver.execute_script("window.scrollTo(0, 150)")
        driver.save_screenshot('walmart.png')

        # extracting details
        title_element = driver.find_element(By.CLASS_NAME, 'w_iUH7')
        price_element = driver.find_element(By.CSS_SELECTOR, 'mr1 mr2-xl b black lh-copy f5 f4-ly')
        link = driver.find_element(By.CLASS_NAME, 'absolute w-100 h-100 z-1 hide-sibling-opacity')
        item = {
            'site': 'Walmart',
            'link': 'f{link}',
            'item_title_name': title_element.text,
            'price': price_element.text
        }
        return item
    except Exception as e:
        print(f"Error fetching from Walmart: {e}")
    finally:
        driver.quit()
    return False