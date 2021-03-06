#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/16
# @Author  : lfr

import time
from appium import webdriver
from b_page.basepage import BasePage
from b_page.login import LoginPage
from b_page.start_page import StartPage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from common.base_driver import BaseDriver

class UpdatePopup(BasePage):
    '''版本更新弹窗、通知弹窗'''
    update_loc = (By.ID, 'com.qekj.merchant:id/ll_update')

    cancel_el = 'com.qekj.merchant:id/iv_cancel'
    cancel_loc = (By.ID, cancel_el)

    def notice_cancel_opera(self):
        '''判断是否有通知弹窗'''

    def update_opera(self):
        '''更新版本'''
        return self.update_btn().click()

    def cancel_opera(self):
        '''取消更新'''
        return self.driver.find_element_by_id(self.cancel_el).click()

    def update_btn(self)->WebElement:
        '''立即更新按钮'''
        upd_ele = self.driver.get_visible_element(self.update_loc)
        return upd_ele

    def cancel_btn(self)->WebElement:
        '''取消更新按钮'''
        upd_ele = self.driver.get_visible_element(self.cancel_loc)
        return upd_ele

if __name__ == '__main__':
    cancel_el = 'com.qekj.merchant:id/iv_cancel'
    driver = BaseDriver().android_driver()
    StartPage(driver).swipe_start()
    LoginPage(driver).login_opera('18768124236', '123456')
    UpdatePopup(driver).cancel_opera()
    time.sleep(3)
    boo = UpdatePopup(driver).is_exist_element(cancel_el)
    print(boo)