__author__ = "jiajia"

from airtest.core.api import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
name=58
mobile=183xxxxxx
driver.get("xxx.com")
driver.find_elements_by_class_name("el-input__inner")[0].send_keys('1xxxxx')
driver.find_elements_by_class_name("el-input__inner")[1].send_keys('1xxxxx')
driver.find_elements_by_class_name("el-button")[0].click()
sleep(3.0)
for i in range(60):
#输入姓名
    driver.find_elements_by_class_name("el1-input__inner")[4].send_keys('学生'+str(name+i))
#输入手机号
    driver.find_elements_by_class_name("el1-input__inner")[6].send_keys(str(mobile+i))
#选择性别
    driver.find_elements_by_class_name("el1-radio")[0].click()
#缩放
# driver.execute_script("document.body.style.zoom='0.55'")
# print("缩放成功")
# driver.maximize_window()
    sleep(1.0)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    print("滚动到最下方")
#点击提交
    driver.find_elements_by_class_name("el1-button")[16].click()
    print('学生'+str(name+i)+':'+str(mobile+i)+'登记成功！')
#滚动到最上方
    sleep(1.0)
    driver.execute_script("window.scrollTo(0,0);")
    print("滚动到最上方")
