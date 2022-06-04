from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Running from command line interface = cli: python my-store.py!
# syntax of selenium 4
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

print("------------", driver.current_url)

driver.close()
