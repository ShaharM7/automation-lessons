from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_to_netflix_account():
    chrome_driver = webdriver.Chrome(executable_path="chromedriver.exe")

    chrome_driver.get('https://www.netflix.com/il/login')
    chrome_driver.maximize_window()

    # Login page elements
    user_name_element = chrome_driver.find_element(by=By.ID, value="id_userLoginId")
    user_name_element.send_keys("Netalimo123@gmail.com")

    password_element = chrome_driver.find_element(by=By.ID, value="id_password")
    password_element.send_keys("1402Neta")

    login_button_element = chrome_driver.find_element(by=By.XPATH, value="//button[contains(text(),'היכנס')]")
    login_button_element.click()

    chrome_driver.close()
