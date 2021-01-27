import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date

chrome_options = Options()
chrome_options.add_argument('--headless')
# 模拟浏览器打开网站
# browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
duration = 365
name_list = ['学号']
password_list = ['密码']


for idx in range(duration):
    # getting the current date
    current_date = date.today()
    year = current_date.year
    month = current_date.month
    day = current_date.day

    for i in range(len(name_list)):
        date_string = str(year) + "年" + str(month) + "月" + str(day) + "日"
        browser = webdriver.Chrome(options=chrome_options,
                                   # 替换以下chromedriver执行路径
                                   executable_path=r'chromedriver的路径')
        browser.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange')
        # 将窗口最大化
        browser.maximize_window()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[1]/input").send_keys(
            name_list[i])

        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[2]/input[1]").send_keys(
            password_list[i])

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[1]/div[5]/a[2]").click()  # 每日上报

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a[1]/div").click()  # 新增
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[7]/input").click()  # 我已仔细阅读并同意
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[9]").click() # 提交

        time.sleep(1)
        print(name_list[i] + "   " + date_string + "   " + "上报成功")
        browser.quit()
    
    time.sleep(24*3600) # 间隔一天
