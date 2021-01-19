import unittest
import time
from utils.log_cn import *
from TestRunner import HTMLTestRunner

#测试套件

suite = unittest.defaultTestLoader.discover(start_dir="./test_case/", pattern="unit*.py")
# suite = unittest.TestSuite()
# suite.addTest(MyTestCase("test_baidu"))
# suite.addTest(MyTestCase("test_sougou"))

if __name__ == "__main__":
    # print(__name__)
    now = time.strftime("%y-%m-%d %H_%M_%S")
    path = "./report/" + now[:-9]
    mkdir(path)

    filename = path + "/html/result_" + now[9:] + ".html"
    print(filename)
    with open(filename, "wb") as fe:
        # 测试运行器
        runner = HTMLTestRunner(
            stream=fe,
            title="My Project 测试报告",
            description="Python Test"
        )
        runner.run(suite)
