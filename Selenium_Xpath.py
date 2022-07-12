from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/embed/6N16loeNilo')

