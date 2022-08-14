import time
from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
# 被测试的手机系统
desired_caps['platformName'] = 'Android'
# 被测试的手机版本,可以写部分版本号,但是不能写错
desired_caps['platformVersion'] = '5.1.1'
# 设备名称，可以随便写，但是不能不写
desired_caps['deviceName'] = '192.168.56.101:5555'
# 获取包名界面名:adb shell dumpsys window | findstr mCurrentFocus
# adb shell dumpsys window windows | findstr mFocusedApp
# 被测试的APP的包名
desired_caps['appPackage'] = 'com.android.settings'
# 被测试的APP的界面名
desired_caps['appActivity'] = '.Settings'
# 不重置APP的缓存
desired_caps['noReset'] = True
# 中文配置
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True



# 创建驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐性等待
driver.implicitly_wait(5)
#需求:获取手机分辨率
print(driver.get_window_size())
#获取当前打开页面截图
driver.get_screenshot_as_file(f"./img/{time.strftime('%Y%m%d%H%M%S')}-test.png")



# ④.等待3s，关闭app
time.sleep(5)
# 关闭驱动对象
driver.quit()
