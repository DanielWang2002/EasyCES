import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=option)

print('='*80)

driver.get('https://ceq.nkust.edu.tw/')

time.sleep(0.1)

# 讓使用者手動進行驗證，最多等待600秒
wait = WebDriverWait(driver, 600)
wait.until(EC.url_to_be("https://ceq.nkust.edu.tw/StuFillIn/Default"))

# 登入後自動轉向課程問卷頁面
driver.get('https://ceq.nkust.edu.tw/StuFillIn')
print("已進入https://ceq.nkust.edu.tw/StuFillIn")
print('='*80)

# 計算課程數量
table = driver.find_element(By.ID, 'dataTable')
rows = table.find_elements(By.TAG_NAME, 'tr')
course_count = len(rows) - 1

# 問卷題號
question_list = ['11_', '12_', '13_', '14_', '15_', '16_', '21_', '22_', '23_', '24_', '31_', '32_', '33_', '41_', '42_', '43_', '51_', '52_', '53_', '61_', '62_', '63_', '71_', '81_', '82_']

for i in range(1, course_count + 1):

    # 使用 try except 避免問卷已填寫過
    try:

        # 印出當前課程名稱
        print("當前課程：", driver.find_element(By.XPATH, f'/html/body/div/div/section[2]/div[3]/div/div/div[2]/table/tbody/tr[{i}]/td[1]').text)

        # 進入指定課程問卷網站
        btn = driver.find_element(By.XPATH, f'/html/body/div/div/section[2]/div[3]/div/div/div[2]/table/tbody/tr[{i}]/td[2]/button')
        btn.click()
        
        for question_num in question_list:
            # 題號1開頭的選項順序與其他的不同
            if question_num[0] == '1':
                question = driver.find_element(By.ID, question_num + '1')
            # 題號8-1預設填教學平台
            elif question_num == '81_':
                question = driver.find_element(By.ID, question_num + '6')
            else:
                question = driver.find_element(By.ID, question_num + '5')
            question.click()
        
        # 填完問卷後點擊送出
        submit = driver.find_element(By.ID, 'Send')
        print(submit.text)
        submit.click()

        time.sleep(3)

    except: 
        print("此課程已填寫過")
    print('='*80)

print("所有問卷已填寫完成，3秒後程式自動關閉...")
print('='*80)
time.sleep(3)
driver.quit()