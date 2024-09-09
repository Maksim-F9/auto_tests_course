from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(5)
    
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Button to add item to the page is not found"