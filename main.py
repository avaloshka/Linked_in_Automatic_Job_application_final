from selenium import webdriver
import time
import os
from selenium.common.exceptions import NoSuchElementException

LINKED_IN_USERNAME = os.environ["USERNAME"]
LINKED_IN_PASSWORD = os.environ["PASSWORD"]

driver = webdriver.Chrome("C:\Development\chromedriver.exe")
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
driver.maximize_window()

driver.find_element_by_class_name("nav__button-secondary").click()
time.sleep(1)

username = driver.find_element_by_id("username")
username.send_keys(LINKED_IN_USERNAME)
password = driver.find_element_by_id("password")
password.send_keys(LINKED_IN_PASSWORD)

driver.find_element_by_css_selector(".login__form_action_container button").click()

time.sleep(2)
# Job alert to switch on
# driver.find_element_by_id("ember181").click()
# driver.find_element_by_class_name("jobs-save-button").click()

# find all_listings. (Only some listings are visible. Find proper path)
all_listings = driver.find_elements_by_css_selector(".job-card-container__metadata-wrapper")
# selecting a listing
for listing in all_listings:
    listing.click()
    time.sleep(2)
    # press Apply button on a listing
    try:
        apply_button = driver.find_element_by_css_selector(".artdeco-button__text")
        apply_button.click()
    except NoSuchElementException:
        print("The exception was raised. I could not locate the Apply button")
        continue

time.sleep(2)
driver.quit()