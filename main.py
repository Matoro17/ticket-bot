import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pygame

def monitor_page(url, initial_button_id, target_page_buttons_xpath_1, target_page_buttons_xpath_2, element_id, target_string, headless=True ):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_cookies_button.click()

        # Click the initial button to navigate to a specific page
        initial_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, initial_button_id))
        )
        initial_button.click()


        # Click the other buttons on the target page if needed
        if target_page_buttons_xpath_1:
            target_page_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, target_page_buttons_xpath_1))
            )
            for button in target_page_buttons:
                button.click()

        # Click the other buttons on the target page if needed
        if target_page_buttons_xpath_2:
            target_page_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, target_page_buttons_xpath_2))
            )
            for button in target_page_buttons:
                button.click()

        # Wait for the element to be present on the page
        target_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )

        # Get the text content of the target element
        current_text = target_element.text

        # Check if the target string is present in the element's text content
        if target_string in current_text:
            print(f"O ingresso para Jonas Brothers Ainda está '{target_string}'")
        else:
            pygame.mixer.init()
            pygame.mixer.Sound("smw_1-up.wav").play()
            time.sleep(5)

        driver.refresh()

    except Exception as e:
        return e
        print(f"An error occurred: {e}")

    finally:
        driver.refresh()


if __name__ == "__main__":
    url = "https://www.ticketmaster.com.br/event/jonas-brothers-venda-geral-sp"
    initial_button_id = "buyButton"
    target_page_button_xpath = "//*[@id=\"pickerContent\"]/div/div[1]"  # Set to None if not needed
    target_page_button_xpath_2 = "//*[@id=\"pickerContent\"]/div/div"  # Set to None if not needed
    element_id = "rates"
    target_string = "ESGOTADO"
    trys = 0
    while True:
        headless = True
        print(f"Attemp:{trys}")
        trys += 1
        data = monitor_page(url, initial_button_id, target_page_button_xpath, target_page_button_xpath_2, element_id, target_string, headless )
        if data:
            headless = False
        else: 
            headless = True
