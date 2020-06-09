#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/3
# @Author  : Soner
# @version : 1.0.0


import warnings
import time
import os
from appium import webdriver
from providers.common.logger import Logger

now = time.strftime("%Y-%m-%d")
#  获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def driver_setup():
    udid = "F2425EF2-D6B9-4636-9997-4D3CA592B0BD"
    log = Logger(udid + "_" + now).getlog()
    desired_caps = {
        "bundleId": "com.jindidata.SkyEyes",
        "platformName": "iOS",
        "platformVersion": "13.2",
        "deviceName": "iPhone XR",
        "automationName": "XCUITest",
        # # 会话结束时删除所有生成的文件
        "clearSystemFiles": True,
        "udid": udid,
        "app": "{}/app/NewSkyEyes.zip".format(BASE_DIR),
        "xcodeOrgId": "7Y32L5GA75",
        "xcodeSigningId": "J26G4D2GCV",
        # 执行完全重置
        "fullReset": False,
        # 获取权限
        "autoAcceptAlerts": True,
        # 设置键盘
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "wdaLocalPort": 8010,
        # 不与系统同步粘贴板,提高启动模拟器的性能
        "simulatorPasteboardAutomaticSync": "off",
        # 从WDA获取JSON源，并在Appium服务器上解析为XML，加快速度
        "useJSONSource": True,
    }
    warnings.simplefilter('ignore', ResourceWarning)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    log.info("设备：{}，启动成功，用例集开始执行".format(udid))
    return driver, udid, log


if __name__ == '__main__':
    driver_setup()
