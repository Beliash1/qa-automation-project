from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_google():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.google.com")

    time.sleep(3)

    assert "Google" in driver.title

    driver.quit()