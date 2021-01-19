import unittest
from selenium import webdriver
from time import sleep
from utils.duan_yan import *

class MyTestCase(unittest.TestCase):

    driver = None

    """"百度搜索用例"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # print("start")
        self.driver.get("https://baidu.com/")
        self.driver.maximize_window()

    def tearDown(self):
        sleep(3)
        # print("end")

    def test_1zhongwen(self):
        """中文搜索"""
        self.driver.find_element_by_id("kw").send_keys("五星红旗")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        duan_equal(self.driver, "五星红旗_百度搜索", self.driver.title, "中文搜索用例")
        # self.assertEqual("五星红旗_百度搜索", self.driver.title, msg="实际结果与预期结果不符")

    def test_2english(self):
        """英文搜索"""
        self.driver.find_element_by_id("kw").send_keys("Demo")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        duan_equal(self.driver, "Demo_百度搜索", self.driver.title, "英文搜索用例")
        # self.assertEqual("Demo_百度搜索", self.driver.title, msg="实际结果与预期结果不符")

    def test_3pinyin(self):
        """"拼音搜索"""
        self.driver.find_element_by_id("kw").send_keys("laohu")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        # self.assertEqual("laohu_百度搜索", self.driver.title, msg="实际结果与预期结果不符")
        # self.assertIn("laohu", self.driver.page_source)
        # self.assertTrue("laohu" in self.driver.page_source)
        duan_equal(self.driver, "laohu_百度搜索", self.driver.title, "拼音搜索用例")



if __name__ == '__main__':
    unittest.main()
