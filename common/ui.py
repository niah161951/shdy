#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/6/28 12:29
import time,os
from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.logs import Log


class WebBase:
    '''
    封装浏览器
    '''
    def get_base(self, name, url):
        try:
            chromedriver = os.path.join(os.path.dirname(__file__), '../configs/chromedriver.exe')
            if name in ['chrome','CHROME','ch']:
                driver = webdriver.Chrome(executable_path=chromedriver)
                Log().info('启动谷歌浏览器成功')
            elif name in ['ff','FF']:
                driver = webdriver.Firefox()
                Log().info('启动火狐浏览器成功')

            driver.get(url)
            driver.maximize_window()
            return driver
        except Exception as e:
            Log().error(f'异常原因：{e}')

class WebuiKeys(WebBase):
    '''selenium 二次封装'''
    def __init__(self, name, url):
        '''
        初始化
        :param name:
        :param url:
        '''
        self.driver = self.get_base(name, url)

    def element(self, locator_type, locator):
        '''
        元素
        :param locator_type:
        :param locator:
        :return:
        '''
        loc_dict = {
            "id": By.ID,
            "xpath": By.XPATH,
            "name": By.NAME,
            "css": By.CSS_SELECTOR
        }
        try:
            if  locator is not None:
                find_element = self.driver.find_element(loc_dict.get(locator_type), locator)
                Log().info(f'请输入定位元素：{locator_type},{locator}')
                return find_element
            else:
                self.get_screenshots('数据为空')
                self.driver.quit()
                Log().error(f'输入数据为空{locator}')

        except NoSuchElementException as error:
            Log().error(f'未找到元素原因：{error}')

    def get_add_cookie(self,lists=None):
        '''
        cookie 操作
        :param date:
        :return:
        '''
        try:
            for l in lists:
                self.driver.add_cookie(l)
                self.sleep(1)
                cooks = self.driver.get_cookies()
                Log().info(f'新增cookies成功，值：\n{cooks}')
                self.get_refresh()
                return cooks
        except Exception as e:
            Log().error(f'异常原因{e}')

    def get_screenshots(self, name):
        '''
        对当前屏幕进行全屏截图
        :return:
        '''

        self.time_fs = time.strftime("%Y%m%d%H%M%S")
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(file_path, 'imgs')
        if not os.path.exists(path):
            os.makedirs(path)
        names = name + time.strftime(self.time_fs + '.png')
        path = os.path.join(path, names)
        try:
            self.sleep(2)
            self.driver.get_screenshot_as_file(path)
            Log().info('截图成功')
        except OSError as error:
            Log().error(f'截图失败:{error}')

    def click(self, locator_type, locator):
        '''
        根据定位进行点击
        :param locator_type:
        :param locator:
        :return:
        '''
        try:
            self.element(locator_type, locator).click()
            Log().info(f'点击成功：{locator_type},{locator},click')
        except Exception as e:
            self.get_screenshots('点击失败')
            Log().error(f'异常原因：{e}')

    def clear(self, locator_type, locator):
        '''
        根据定位进行清除数据
        :param locator_type:
        :param locator:
        :return:
        '''
        try:
            self.element(locator_type, locator).clear()
            Log().info('清除数据成功')
        except Exception as e:
            self.get_screenshots('清除数据失败')
            Log().error(f'异常原因{e}')

    def send_keys(self, locator_type, locator, text):
        '''
        根据定位元素输入值
        :param locator_type:
        :param locator:
        :param text:
        :return:
        '''

        if text is not None:
            self.element(locator_type, locator).send_keys(text)
            Log().info(f'数据输入为：{text}')
        else:
            Log().error('无输入数据,退出浏览器')
            self.get_screenshots('数据输入失败')
            self.quit()

    def right_click(self, locator_type, locator):
        '''
        对元素执行鼠标右键右击操作
        :param locator_type:
        :param locator:
        :return:
        '''
        right_click = self.element(locator_type, locator)
        ActionChains(self.driver).context_click(right_click).perform()

    def double_click(self, locator_type, locator):
        '''
        模拟鼠标双击操作
        :param locator_type:
        :param locator:
        :return:
        '''
        double_click = self.element(locator_type, locator)
        ActionChains(self.driver).double_click(double_click).perform()

    def drag_the(self, locator_type, locator, locator_types, locators):
        '''
        移动到指定位置
        :param locator_type:
        :param locator:
        :return:
        '''
        element = self.element(locator_type, locator)
        target = self.element(locator_types, locators)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def set_window(self, wide, high):
        """
        设置浏览器窗口宽和高.
        用法:
        driver.set_window(wide,high)
        """
        return self.driver.set_window_size(wide, high)

    def get_text(self, locator_type, locator):
        '''
        获取文本信息
        :param locator_type:
        :param locator:
        :return:
        '''
        try:
            texts = self.element(locator_type, locator).text
            Log().info(f'获取数据成功；结果{texts}')
            return texts
        except Exception as e:
            Log().error(f'获取数据失败；原因{e}')

    def get_select(self, locator_type, locator, texts, text):
        '''
        visible_text()      文本
        deselect_by_index()   下标
        select_by_value()   value
        :param locator_type:
        :param locator:
        :param text:
        :return:
        '''

        element = Select(self.element(locator_type, locator))
        if texts in 'text':
            element.select_by_visible_text(text)
        elif texts in 'index':
            element.deselect_by_index(text)
        elif texts in 'value':
            element.select_by_value(text)

    def get_attribute(self, locator_type, locator, value):
        '''
        返回元素value值
        :param locator_type:
        :param locator:
        :param value:
        :return:
        '''
        try:
            attribute = self.element(locator_type, locator).get_attribute(value)
            Log().info(f'获取{value}值成功，结果：{attribute}')
            return attribute
        except Exception as e:
            Log().error(f'获取值失败，原因：{e}')

    def get_size(self, locator_type, locator):
        '''
        获取输入框的尺寸
        :return:
        '''
        size = self.element(locator_type, locator).size
        return size

    def get_forward(self):
        '''
        前进
        :return:
        '''
        self.driver.forward()

    def get_handle(self):
        '''
        切换窗口
        :return:
        '''
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[0])

    def get_handles(self, integer):
        '''
        切换窗口并关闭旧窗口
        :return:
        '''
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to_window(handles[integer])

    def assert_text(self, locator_type, locator, text):
        '''
        获取元素进行断言
        :param locator_type:
        :param locator:
        :param text:
        :return:
        '''
        element_text = self.element(locator_type, locator).text
        try:
            if element_text in text:
                Log().info('数据对比成功')
            else:
                Log().error(f'数据对比失败：{element_text}')
        except Exception as error:
            Log().error(f'异常原因：{error}')

    def switch_to_frame(self, locator_type, locator):
        """
        嵌套使用
        :param locator_type:
        :param locator:
        :return:
        """
        self.driver.switch_to.frame(self.element(locator_type, locator))

    def switch_to_parent(self):
        """
        退出嵌套
        :return:
        """
        self.driver.switch_to.parent_frame()

    def get_refresh(self):
        '''
        刷新
        :return:
        '''
        self.driver.refresh()

    def get_upload(self, locator_type, locator, file):
        '''
        上传
        :param locator_type:
        :param locator:
        :return:
        '''
        self.element(locator_type, locator).send_keys(file)

    def sleep(self, seconds):
        '''
        定义强制等待
        :param seconds:
        :return:
        '''
        try:
            time.sleep(seconds)
            Log().info(f'线程等待{seconds}秒')
        except Exception as e:
            Log().error(f'异常原因：{e}')

    def wait(self, seconds):
        '''
        定义隐式等待
        :param seconds:
        :return:
        '''
        try:
            self.driver.implicitly_wait(seconds)
            Log().info(f'隐式等待{seconds}秒')
        except Exception as e:
            Log().error(f'异常原因：{e}')

    def back(self):
        '''
        浏览器返回窗口
        :return:
        '''
        self.driver.back()

    def get_title(self):
        '''
        获取title
        :return:
        '''
        try:
            title = self.driver.title
            Log().info(f'获取title: {title}')
            return title
        except Exception as e:
            Log().error(f'异常原因{e}')



    def click_alert(self):
        '''
        操作点击弹窗接受
        :return:
        '''
        alert = self.driver.switch_to.alert
        self.sleep(1)
        alert.accept()

    def click_dismiss(self):
        '''
        操作点击弹窗拒绝
        :return:
        '''
        alert = self.driver.switch_to.alert
        self.sleep(1)
        alert.dismiss()

    def alert_text(self):
        '''
        获取弹出框文本内容
        :return:
        '''
        alert = self.driver.switch_to.alert
        self.sleep(1)
        return alert.text

    def get_above(self, locator_type, locator):
        '''
        定位到元素执行悬停操作
        :param locator_type:
        :param locator:
        :return:
        '''
        above = self.element(locator_type, locator)
        ActionChains(self.driver).move_to_element(above).perform()

    def quit(self):
        '''
        退出
        :return:
        '''
        try:
            Log().info('立即退出浏览器')
            self.driver.quit()
        except NameError as error:
            Log().info(f'退出浏览器失败，原因:{error}')

    def close(self):
        """
        关闭浏览器
        """
        try:
            self.driver.close()
        except NameError as error:
            Log.error("关闭浏览器窗口失败 %s" % error)


class Key_Board(WebuiKeys):
    '''模拟键盘操作'''

    def key_check_all(self,locator_type,locator):
        '''
        模拟全选操作并输入内容
        :param locator_type:
        :param locator:
        :return:
        '''
        self.element(locator_type,locator).send_keys(Keys.CONTROL,'a')

    def key_shear(self,locator_type,locator):
        '''
        剪切并输入内容
        :param locator_type:
        :param locator:
        :return:
        '''
        self.element(locator_type, locator).send_keys(Keys.CONTROL, 'x')

    def key_paste(self,locator_type,locator):
        '''
        粘贴并输入内容
        :param locator_type:
        :param locator:
        :return:
        '''
        self.element(locator_type, locator).send_keys(Keys.CONTROL, 'v')

if __name__=="__main__":
    driver = WebuiKeys('chrome','https://cli.im/')
    driver.quit()

