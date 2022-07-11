from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.google.com.br')

inputGoogle = navegador.find_element(By.TAG_NAME, 'input')
button = navegador.find_element(By.LINK_TEXT, 'Fazer login')
button.click()
inputOk = navegador.find_element(By.TAG_NAME, 'input')
inputOk.send_keys('Your email')

buttonProx = navegador.find_element(By.ID, 'identifierNext')
buttonProx.click()
sleep(3)
inputPass = navegador.find_element(By.NAME, 'password')


inputPass.send_keys('Your pass')
buttonSenha = navegador.find_element(By.ID, 'passwordNext')
buttonSenha.click()

