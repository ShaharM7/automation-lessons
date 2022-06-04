from selenium import webdriver

# Running from command line interface = cli: python sauce-demo.py!
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

print("------------", driver.current_url)

driver.close()
