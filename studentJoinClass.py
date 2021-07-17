# -*- encoding=utf8 -*-

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
import os
path=os.getcwd()
import requests
import json
import re
import urllib.parse

#driver.implicitly_wait(20)
auto_setup(__file__)
url_studentJoinClass = "http://xxx/api/zmbiz-csc-frontend-sale/outer/groupLesson/studentJoinClass"
studentJoinClassList=[6815449678662881320]

def sendCode(orderUrl,getCodeUrl, mobile,cookie,flag):
    options = webdriver.ChromeOptions()
    # '模拟iphoneX'
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
    options.add_argument('--headless')
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=options)
    time.sleep(2)
    driver.get(orderUrl)
    time.sleep(2)
    # 输入手机号
    driver.find_elements_by_css_selector(".item input")[0].send_keys(str(mobile))
    time.sleep(2)
    # 点击获取验证码
    for j in range(10):
        s=driver.find_elements_by_css_selector(".geetest_panel")
        if (len(s)==0 or len(s)==1):
            driver.find_elements_by_css_selector(".code")[0].click()
            time.sleep(2)   
        else:
            print(str(mobile)+"需要重新兑换课程")
            driver.close()
            flag=True
            return flag
            
    time.sleep(1)
    code=getCode(getCodeUrl, cookie, mobile)
    #输入密码
    driver.find_elements_by_css_selector(".item input")[1].send_keys(str(code))
    #选择同意协议
    driver.find_elements_by_css_selector(".van-icon")[0].click()
    driver.find_elements_by_css_selector(".submit")[0].click()
    time.sleep(5)
    print (driver.current_url)
    text=driver.current_url
    print(text)
    pattern = r'token=(.*)'
    #print('moren', re.findall(pattern, text))
    token=re.findall(pattern, text)[0]
    token_parse=urllib.parse.unquote(token)
    
    print(token)
    studentJoinClass(studentJoinClassList,token_parse,mobile)
    time.sleep(2)
    flag=False
    return flag
    driver.close()
  
def studentJoinClass(studentJoinClassList,token,mobile):
    for i in studentJoinClassList:
        payload = {
            "classId": i,
            "token": token
        }

        payload_json = json.dumps(payload, ensure_ascii=False).encode("utf-8").decode("latin1")

        headers = {
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
          'Content-Type': 'application/json;charset=UTF-8'
        }

        response = requests.request("POST", url_studentJoinClass, headers=headers, data=payload_json)
        

        print(str(mobile)+":"+str(i)+response.text)                                    

def getCode(getCodeUrl, cookie, mobile):
    payload = {
        "mobile": mobile
    }
    payload_json = json.dumps(payload, ensure_ascii=False).encode("utf-8").decode("latin1")
    headers = {
        'content-type': 'application/json;charset=UTF-8',
        'cookie': cookie
    }
    response = requests.request("POST", getCodeUrl, headers=headers, data=payload_json)
    response_text = response.text
    print(response_text)
    print('验证码为:' + response_text[41:47])
    code=response_text[41:47]
    return code



# mobile1 = [18886666667,18354323985,19983280445,17825391533,18300396987,18305367101,18382281887,18321868725,18321868726,18321868728]
mobile1 = [17157415129,17157415130,17157415131,17157415132,17157415133,17157415134,17157415135,17157415136,17157415137,17157415138]
for z in mobile1:

    orderUrl1 = 'http://xxx/lesson/smallClass/record'
    getCodeUrl1 = "https://xxx/sms/code/getCurrentCode"
    cookie1 = 'xxx'
    flag = True
    while flag:
        flag=sendCode(orderUrl1,getCodeUrl1,z,cookie1,flag)
    
        
    time.sleep(3)
    
