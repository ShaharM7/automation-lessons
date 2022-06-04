from selenium import webdriver

# Running from command line interface = cli: python cypress-website.py!

chrome_options = webdriver.ChromeOptions()

# For MAC or Linux:
# chrome_options.add_argument('--kiosk')

# For Windows:
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
driver.get("https://www.cypress.io/")

print("------------", driver.current_url)

driver.close()
