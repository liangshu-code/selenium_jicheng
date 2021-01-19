import unittest
from selenium.common.exceptions import NoSuchElementException
from utils.jietu import *
from utils.log_cn import load_log


def duan_in(driver,yuqi,shiji,Cname):
    try:
        unittest.TestCase().assertIn(yuqi,shiji)
    except NoSuchElementException as e:
        jietu(driver, Cname)
        print("元素定位错误")
    except AssertionError as e:
        jietu(driver, Cname)
        print("预期结果与实际结果不相符,断言失败")
    except Exception as e:
        jietu(driver, Cname)
        print("未知错误")
    else:
        print("用例执行通过")

def duan_equal(driver,yuqi,shiji,Cname):
    try:
        unittest.TestCase().assertEqual(yuqi,shiji)
    except NoSuchElementException as e:
        jietu(driver, Cname)
        load_log("元素定位错误")
        raise NoSuchElementException
    except AssertionError as e:
        jietu(driver, Cname)
        load_log("预期结果: %r 实际结果:%r ,断言失败"% (yuqi, shiji))
        raise AssertionError
    except Exception as e:
        jietu(driver, Cname)
        load_log("未知错误")
        raise Exception
    else:
        load_log("预期结果: %r 实际结果:%r ,断言成功"% (yuqi, shiji))

