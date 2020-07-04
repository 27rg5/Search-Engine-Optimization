from bs4 import BeautifulSoup
import requests
from urllib import parse
from selenium import webdriver


class parsing():

    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def find_links(self,fileName):
        if(fileName.split('.')[-1]=='html'):
            with open(fileName)as html_file :
                source=BeautifulSoup(html_file,'lxml')
            for match in source.find_all('a'):
                if(match.has_attr('href')):
                    p=match['href']
                    url = parse.urljoin(self.base_url, p)
                    self.links.add(url)
        else:
            chromedriver="C:/Users/admin/Desktop/chromedriver_win32/chromedriver"
            driver= webdriver.Chrome(chromedriver)
            driver.get(fileName)
            source=driver.execute_script("return document.documentElement.outerHTML")
            driver.quit()
            result=BeautifulSoup(source,'lxml')
            for match in result.find_all('a'):
                if(match.has_attr('href')):
                    p=match['href']
                    url = parse.urljoin(self.base_url, p)
                    self.links.add(url)


    def page_links(self):
        return self.links
