# Implementation of Selenium test automation for this Selenium Python Tutorial
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    chrome_driver.find_element(by=By.NAME, value="li1").click()
    chrome_driver.find_element(by=By.NAME, value="li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element(by=By.ID, value="sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    chrome_driver.find_element(by=By.ID, value="addbutton").click()
    sleep(5)

    output_str = chrome_driver.find_element(by=By.NAME, value="li6").text
    sys.stderr.write(output_str)

    sleep(2)
    chrome_driver.close()
