from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('window-size=1280,800')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
navegador = webdriver.Chrome(options=options)

navegador.get('https://olhardigital.com.br/')


poupNot = navegador.find_element(By.ID, 'onesignal-slidedown-cancel-button')
poupNot.click()
sleep(1)
elemement = navegador.find_element(By.CLASS_NAME, 'search-button')
elemement.click()

inputSearch = navegador.find_element(By.ID, 'mainSearchInput')
inputSearch.send_keys('Tecnologia')
inputSearch.submit()



