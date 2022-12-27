from pathlib import Path
from time import sleep
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser

if __name__ == '__main__':
    browser = make_chrome_browser()
    browser.get('https://suap.ifrn.edu.br/')

    username = browser.find_element(By.NAME,"username")
    username.clear()
    username.send_keys("pycon")
    password = browser.find_element(By.NAME, "password")
    password.send_keys("pycon")
    
    password.send_keys(Keys.RETURN)
    sleep(5)
    assert "Por favor, entre com usuário e senha válidos"
    browser.quit()
    

