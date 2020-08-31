import config
from config import keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def order():
    # add to cart
    driver.find_element_by_name('commit').click()

    # wait for checkout button element to load
    time.sleep(.5)
    checkout_element = driver.find_element_by_class_name('checkout')
    checkout_element.click()

    # Have to check the terms and conditions box as soon as checkout screen pops

    # fill out checkout screen fields
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(keys['state'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(keys['card_month'])
    driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(keys['card_year'])
    
    # Terms and conditions
    checkBoxes = driver.find_elements_by_class_name('iCheck-helper')
    checkBoxes[1].click()

    process_payment = driver.find_element_by_class_name('button ')
    process_payment.click()



if __name__ == "__main__":
    urlLink = ""
    while urlLink == "":
        urlLink = input("URL LINK OF ITEM: ")

    keys['product_url'] = urlLink

    driver = webdriver.Chrome('/path/to/chromedriver/file')

    driver.get(keys['product_url'])
    order()
