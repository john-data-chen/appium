import time
from appium import webdriver
from selenium.webdriver.common.by import By

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    desired_caps = {}  # 空字典 需要給予測試手機相關資訊
    desired_caps['platformName'] = 'Android'  # 測試的平台
    desired_caps['platformVersion'] = '13'  # 手機os版本
    desired_caps['deviceName'] = 'XXXXXXXXXXX'  # 從 adb devices 得到的字串
    desired_caps['automationName'] = "UiAutomator2"  # 一定要的！
    desired_caps['autoGrantPermissions'] = True  # 自動同意授權
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
    desired_caps['noReset'] = False  # 改成 True，會保留原先資料，但自動化腳本會失敗
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    agree_btn_ele = driver.find_element(By.ID, 'com.android.chrome:id/terms_accept')  # 取得 接受並繼續 元素
    print('點擊: {0}'.format(agree_btn_ele.get_attribute('text')))  # 取得 接受並繼續 元素的文字
    agree_btn_ele.click()
    time.sleep(3)  # 等待3秒

    negative_btn_ele = driver.find_element(By.ID, 'com.android.chrome:id/negative_button')  # 取得不用了，謝謝 元素
    print('點擊: {0}'.format(negative_btn_ele.get_attribute('text')))  # 取得 不用了，謝謝 元素的文字
    negative_btn_ele.click()
    print("進入到Google首頁")
    time.sleep(3)  # 等待3秒

    search_box_text_ele = driver.find_element(By.ID, 'com.android.chrome:id/search_box_text')  # 取得搜尋框 元素
    print('點擊: {0}'.format(search_box_text_ele.get_attribute('text')))  # 取得搜尋框 元素的文字
    print('輸入網址: https://m.facebook.com/')
    search_box_text_ele.send_keys("https://m.facebook.com/")  # 輸入字串
    driver.press_keycode(66)  # 按下 Enter Key
    print("進入到Facebook登入頁面")
    driver.quit()


