import requests
from selenium import  webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


def calculate(driver, price, number,cover,cover_number):
    driver.find_element_by_xpath('//*[@id="P1"]').send_keys(price)
    driver.find_element_by_xpath('//*[@id="P2"]').send_keys(number)
    driver.find_element_by_xpath('//*[@id="P3"]').send_keys(cover)
    driver.find_element_by_xpath('//*[@id="P4"]').send_keys(cover_number)
    driver.find_element_by_xpath('//*[@id="cent"]/div[10]/a[1]').click()
    final_price = driver.find_element_by_xpath('//*[@id="D1"]').get_attribute('value')
    final_number = driver.find_element_by_xpath('//*[@id="D2"]').get_attribute('value')
    return[final_price,final_number]

def print_(a, b):
    print('最终价格为：%s, 最终数量为%s' % (a, b))

if __name__ == '__main__':
    url = 'http://www.yingjia360.com/jisuanqi/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)#executable_path=chrome_driver, 
    driver.get((url))
    # sleep(3)
    result = calculate(driver, '2.13', '100', '1.15', '200')
    print_(*result)
