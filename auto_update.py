import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date

chrome_options = Options()
chrome_options.add_argument('--headless')
# 模拟浏览器打开网站
# browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
duration = 365
name_list = ['学号1'， '学号2'， '学号n']
password_list = ['密码1', '密码2', '密码n']


for idx in range(duration):
    # getting the current date
    current_date = date.today()
    year = current_date.year
    month = current_date.month
    day = current_date.day

    for i in range(3, len(name_list)):
        date_string = str(year) + "年" + str(month) + "月" + str(day) + "日"
        browser = webdriver.Chrome(options=chrome_options,
                                   # 替换以下chromedriver执行路径
                                   executable_path=r'/home/wangshuo/Downloads/chromedriver_linux64/chromedriver')
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
        try:
            browser.find_element_by_xpath("/html/body/div[3]/button").click()
        except:
            time.sleep(1)

        browser.find_element_by_xpath("/html/body/div[1]/div[6]/a[2]").click()  # 每日上报

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[17]/div[2]/div/div/span").click()  # location
        time.sleep(1)

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[63]").click()
        time.sleep(1)

        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[64]/div[1]/div[1]").click()  # location
        time.sleep(1)

        print(name_list[i] + "   " + date_string + "   " + "上报成功")
        browser.quit()
    
    time.sleep(24*3600) # 间隔一天

