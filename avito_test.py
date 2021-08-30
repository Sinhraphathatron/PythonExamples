# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pytesseract
from pytesseract import image_to_string
from PIL import Image
import os
import base64
from io import BytesIO

f=open('Result.csv', 'a', encoding='1251')
e=2
e=int(e)

urls=[]

browser=webdriver.Chrome("C:\selenium\chromedriver.exe")
browser.get("https://www.avito.ru/novosibirsk") 
time.sleep(1)
elem=browser.find_element_by_id('search')
time.sleep(1)
elem.send_keys('lego ')
time.sleep(1)
fnd=browser.find_element_by_class_name('index-button-2q4Wv')
time.sleep(1)
fnd.click()
time.sleep(1)
ctgr=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/select/option[48]')
time.sleep(1)
ctgr.click()
time.sleep(1)
prc=browser.find_element_by_class_name('input-input-25uCh')
time.sleep(1)
prc.send_keys('10000')
time.sleep(1)
shw=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/button')
time.sleep(1)
shw.click()
try:
	cp=browser.find_element_by_class_name('page-title-count-1oJOc').get_attribute('outerText')
	cp=int(cp)
	
	for i in range(0, cp):
		link=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div/div[1]/div['+str(e)+']/div/div[2]/div[1]/div[1]/h3/a')
		link.click()
		time.sleep(3)
		browser.switch_to.window(browser.window_handles[1])
		time.sleep(1)
		prc=browser.find_element_by_class_name('js-item-price').get_attribute('outerText')
		time.sleep(1)
		ttl=browser.find_element_by_class_name('title-info-title-text').get_attribute('outerText')
		time.sleep(1)
		name=browser.find_element_by_class_name('seller-info-name').get_attribute('outerText')
		time.sleep(1)
		addrs=browser.find_element_by_class_name('item-address__string').get_attribute('outerText')
		time.sleep(1)
		metro=browser.find_element_by_class_name('item-address-georeferences-item__content').get_attribute('outerText')
		time.sleep(3)
		phone=browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/span/span/button').click()
		time.sleep(3)
		number=browser.find_element_by_xpath('/html/body/div[14]/div/div/span/div[1]/div[2]/div/img').get_attribute('src')
		image_base64=number.split(',')[1]
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		phone=pytesseract.image_to_string(Image.open(BytesIO(base64.b64decode(image_base64))))
		time.sleep(1)
		urls.append(' Заголовок: '+ttl)
		urls.append(' Ссылка на товар: '+browser.current_url)
		urls.append(' Стоимость: '+prc)
		urls.append(' Имя продавца: '+name)
		urls.append(' Адрес: '+addrs)
		urls.append(' Метро: '+metro)
		urls.append(' Телефон: '+phone)
		f.write(str(urls) + '\n' + '\n')
		urls.clear()
		browser.close()
		time.sleep(1)
		browser.switch_to.window(browser.window_handles[0])
		e=e+1
		time.sleep(1)
finally:
	browser.close()
quit()