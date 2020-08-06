from selenium import webdriver
import requests
from time import sleep


class getCookie():
    def cookie(self):
        cookie_dict = []
        driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
      #  driver = webdriver.PhantomJS()
        url = 'http://unit11.bestwehotel.com/newStore/index.html?redirect=http%3A%2F%2Fhyttest.bestwehotel.com'
        driver.get(url)
        driver.find_element_by_xpath("html/body/div/main/section/div[2]/div/input").send_keys("13750047510")
        driver.find_element_by_xpath("html/body/div/main/section/div[2]/div[2]/button").click()
        driver.find_element_by_xpath("html/body/div/main/section/div[2]/div[2]/input").send_keys("111111")
        driver.find_element_by_xpath("html/body/div/main/section/div[2]/button").click()
        print('登录成功')
        sleep(6)
    #    driver.find_element_by_xpath("html/body/div/div/div/aside/ul/li[5]").click()
        move = driver.find_element_by_xpath("html/body/div/div/div/div/aside/ul/div/li[5]/ul/div/li[4]")
        print('找到元素')
        webdriver.ActionChains(driver).move_to_element(move).perform()
        move.click()
        print('点击成功')

        cookie_list = driver.get_cookies()
        for cookie in cookie_list:
                cookie_dict[cookie['name']]=cookie['value']
                print(cookie_dict)

if __name__ =='__main__':
    run = getCookie()
    run.cookie()
