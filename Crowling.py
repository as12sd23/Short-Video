from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Crowling:
    def __ini__(self):
        #드라이버 세팅
        chrome_options =webdriver.ChromeOptions()
        driver = webdriver.Chrome(service = Service(
            ChromeDriverManager().install()),
            options = chrome_options)
        
        #크롤링 할 주소
        url = "https://www.fmkorea.com/index.php?mid=lol&sort_index=pop&order_type=desc"
        #주소 가져오기
        driver.get(url)
        #딜레이 거는거
        #driver.implicitly_wait(3)

        webpage = driver.page_source

        count = driver.find_elements(By.CLASS_NAME, 'li  li_best2_pop0 li_best2_hotdeal0')
        
        for i in count:
            print(i)
        