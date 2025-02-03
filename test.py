from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

__author__ = "uechan"

import time

options = UiAutomator2Options()
options.load_capabilities({
	"appium:language": "ja",
	"appium:locale": "JP",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
    "appPackage": <app_id>,
    "appActivity": "io.branch.unity.BranchUnityActivity",
    "appium:noReset": True,
    "appium:fullReset": False,
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(6)

auto_setup(__file__)

# WebView操作
el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"開催期間\")")
el1.click()
time.sleep(1)
el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"終了したイベントを含める\")")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"開催中\").instance(1)")
el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"絞り込みを適用\")")
el4.click()
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.TextView\").instance(2)")
el5.click()

time.sleep(5)
auto_setup(__file__, logdir=True, devices=["android:///",])

poco = UnityPoco()
poco("FooterContents").offspring("MyPage").child("SelectButton").click()

time.sleep(5)
driver.quit()