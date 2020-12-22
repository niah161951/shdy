#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 13:18
import os
import pytest ,allure

@allure.feature('这里是一级标签')
class Ttest_Calass:
    def test_003(self):
        assert 1!=1
    @allure.title("用例标题0")
    @allure.story("这里是第一个二级标签")
    @pytest.mark.parametrize('param', ['青铜', '白银', '黄金'])
    def test_0(self, param):
        allure.attach('附件内容是： '+param, '我是附件名', allure.attachment_type.TEXT)

    @allure.title("用例标题1")
    @allure.story("这里是第二个二级标签")
    def test_1(self):
        allure.attach.file(r'E:\Myproject\pytest-allure\test\test_1.jpg', '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)

    @allure.title("用例标题2")
    @allure.story("这里是第三个二级标签")
    @allure.severity(allure.severity_level.NORMAL)
    def test_2(self):
        pass

def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====")

def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====")

def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")

def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("three")

    def test_four(self):
        print("four")

if __name__ == '__main__':
    # #运行指定模块
    # pytest.main('-v -s pytests.py')
    # #运行批量文件夹（运行当前文件夹包括子文件夹所有用例）
    # pytest.main('-v -s ./')
    # #运行指定文件夹（tmp目录下面所有用例）
    # pytest.main('-v -s tmp/ ')
    # #运行模块中指定用例 （运行模块中test_001_spec用例）
    # pytest.main("-v -s pytests.py::Test_Class::test_003")
    # #模糊匹配运行用例（匹配当前目录下面包含）
    # # 运行spec_001_modul_test模块中用例名称包含spec的用例
    # pytest.main("-v -s -k py pytests.py")
    # # 运行当前文件夹匹配Test_Class的用例，类文件下面的用例
    # pytest.main('-s -v -k Test_Class')
    report = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    report = os.path.join(report, 'report')
    pytest.main(['-s', '-q',  '--alluredir=report'])
    os.system('allure serve report')
    pytest.main(["-q", "-s", "-ra", "pytests.py"])




