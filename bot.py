from config import keys
from selenium import webdriver
import time

def order():
    # add to cart
    driver.find_element_by_name('commit').click()

    # wait for checkout button element to load
    time.sleep(.5)
    checkout_element = driver.find_element_by_class_name('checkout')
    checkout_element.click()

    # fill out checkout screen fields
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])

    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
    process_payment.click()



if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys['product_url'])
    order()