# EasyCES

---

# 一款使用Selenium撰寫的自動化程式，輕鬆填寫NKUST的期末調查問卷

## Usage

### 安裝Selenium
```
pip install selenium
pip install webdriver_manager
```

### 執行
因為教學意見調查系統有使用reCaptcha  
如果要自動辨識的話，現有的方法幾乎都要錢，例如`2Captcha`或`YesCaptcha`  
所以這邊我設計成讓使用者手動登入後再自動執行填寫問卷

- 輸入`學號`、`密碼`以及完成`reCaptcha的驗證`後登入網站
- 程式會自動將網站導向[https://ceq.nkust.edu.tw/StuFillIn](https://ceq.nkust.edu.tw/StuFillIn)並開始填寫問卷，如果有已經填過的問卷也會略過

### 需要注意以下幾點
- 每題都預設會填「非常同意」，最後三題填空題則不填
- 有關線上上課的題目(8-1)，預設是填寫教學平台，需要更改的人可以自行修改程式碼，教學平台的id是6，改成5就是Office365 + MS Teams，依此類推
- 偶爾開啟程式後會有不能輸入學號密碼的問題，目前還找不到問題點，但重開可以解決