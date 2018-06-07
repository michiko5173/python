from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
url='https://ks.wjx.top/jq/24573761.aspx'
xingming_  = "郑东"
yuangongbianhao_  = "22426899"
anser={'3':'4','4':'2','5':'3','6':'3','7':'1','8':'4','9':'4','10':'1','11':'3','12':'3'}
browser=webdriver.Chrome()
browser.get(url)
#选择部门，填写基本信息
classSelectValue = "15"
Select(browser.find_element_by_tag_name("select")).select_by_value(classSelectValue)
xingming = browser.find_element_by_xpath('//*[@id="divquestion2"]/table/tbody/tr[1]/td/div/textarea')
yuangongbianhao = browser.find_element_by_xpath('//*[@id="divquestion2"]/table/tbody/tr[2]/td/div/textarea')
xingming.clear()
xingming.send_keys(xingming_)
yuangongbianhao.clear()
yuangongbianhao.send_keys(yuangongbianhao_)
#延时
time.sleep(18)
# 答题
for k,v in anser.items():
    sub_btn = browser.find_element_by_xpath('//*[@id="divquestion'+k+'"]/ul/li['+v+']/label')
    sub_btn.click()
#点击提交
sub_tj = browser.find_element_by_xpath('//*[@id="submit_button"]')
sub_tj.click()

