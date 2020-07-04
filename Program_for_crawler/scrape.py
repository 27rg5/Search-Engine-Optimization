from general import *

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
def base(base_url):
    chromedriver="C:/Users/admin/Desktop/chromedriver_win32/chromedriver"
    driver= webdriver.Chrome(chromedriver)
    driver.get(base_url)
    source=driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    result=BeautifulSoup(source,'lxml')
    make_file("sourcefile.html",str(result))
#print(result.prettify())