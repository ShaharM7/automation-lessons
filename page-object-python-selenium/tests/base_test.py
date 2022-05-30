import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

@pytest.fixture(autouse=True)
def set_up(self):
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--start-fullscreen")
    options.add_argument('--disable-gpu')

    self.driver = webdriver.Chrome(executable_path=".", options=options)
    # self.driver = webdriver.Firefox()
    self.driver.get("http://www.amazon.com")


def tearDown(self):
    self.driver.close()
