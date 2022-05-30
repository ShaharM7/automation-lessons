from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_search_automation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.google.co.il/?hl=iw")
    driver.maximize_window()

    search_bar_element = driver.find_element(by=By.NAME, value="q")
    search_bar_element.send_keys("Automation is nice")