# - * - coding:utf-8 - * -
#author:wudasheng time:2018/9/4

from appium import webdriver
from time import sleep
desired_caps = {
    'platformName' : 'Android',
    'deviceName' : '127.0.0.1:62001',
    'platformVersion' : '7.0',
    'appPackage': 'com.taobao.taobao',
    'appActivity' : 'com.taobao.tao.welcome.Welcome',
    # 输入中文，添加unicodeKeyboard，resetKeyboard两个参数
    'unicodeKeyboard' : 'True',
    'resetKeyboard' : 'True'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# time.sleep(5)
# driver.swipe(696, 480, 34, 480)
# driver.swipe(500, 301, 500, 755)
def swipRight(driver):
    driver.swipe(696, 480, 34, 480)
    # l = driver.get_window_size()
    # x1 = l['width'] * 696
    # y1 = l['height'] * 480
    # x2 = l['width'] * 34
    # # for i in range(n):
    # #     driver.swipe(x1, y1, x2, y1, t)
    # driver.swipe(x1, y1, x2, y1, t)

if __name__ == "__main__":
    print(driver.get_window_size())
    sleep(10)
    swipRight(driver)