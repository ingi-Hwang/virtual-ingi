import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

'''--------------- use selenium ------------------'''
def get_tour_tag(name):
    driver = webdriver.Chrome('chromedriver')
    url = 'https://www.visitbusan.net/index.do?menuCd=DOM_000000201001000000&ucc2_seq=&search_keyword=&list_type=TYPE_SMALL_CARD&order_type=NEW&listCntPerPage2=16'
    driver.get(url)

    element = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/form/div/div/div[2]/div[1]/input')))
    element.send_keys(name)
    element.send_keys(Keys.RETURN)
    element = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#containernew > div > div > div > div > div.trvList.food_new > div > div > div.info > p > a'))).click()

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    parse = soup.find_all('li')
    tag = list()
    tag.append(name)
    for index in parse:
        tag_name = index.get_text()
        print(tag_name)
        if "#" in tag_name:
            tag_name = tag_name[1:]
            if "힐링" in tag_name:
                tag.append(tag_name)
            if "산책" in tag_name:
                tag.append(tag_name)
            if "공원" in tag_name:
                tag.append(tag_name)
            if "박물관" in tag_name:
                tag.append(tag_name)
            if "야경" in tag_name:
                tag.append(tag_name)
            if "스포츠" in tag_name:
                tag.append(tag_name)
            if "문화" in tag_name:
                tag.append(tag_name)
            if "바다" in tag_name:
                tag.append(tag_name)
            if "사찰" in tag_name:
                tag.append(tag_name)
            if "사진" in tag_name:
                tag.append(tag_name)
    return tag
