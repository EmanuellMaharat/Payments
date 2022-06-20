import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class setup:
        @pytest.fixture(scope='session')
        def setup(self):
                browser = webdriver.Chrome()
                browser.maximize_window()
                browser.get('https://qa.trado.co.il/')
                browser.implicitly_wait(30)
                checkout = browser.find_element(By.CLASS_NAME, "store_saveBtn")
                checkout.send_keys(Keys.ENTER)
                browser.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                browser.find_element(By.XPATH,"//div[contains(@class,'fullProduct_productsHedaer')]//i[contains(@class,'micon-plus icon_icon')]").click()
                checkout = browser.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
                checkout.click()
                phone = browser.find_element(By.XPATH, "//input[contains(@type,'tel')]")
                phone.click()
                phone.send_keys("0549767689")
                signin = browser.find_element(By.XPATH, "//input[@value='התחברות']")
                signin.click()
                # OTP HERE
                payment_checkout = browser.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
                payment_checkout.click()
                return browser





