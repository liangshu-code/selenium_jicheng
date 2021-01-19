import time, os


# 创建report目录并创建测试报告以及断言出错的屏幕截图目录
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path + "/html")
        os.makedirs(path + "/png")


# 将测试用例断言信息写入log日志中
def load_log(info):
    now = time.strftime("%y-%m-%d")
    now_1 = time.strftime("%y-%m-%d %H-%M-%S")
    with open("./log/" + now + ".log", "a", encoding="UTF-8") as fp:
        fp.write(now_1 + ":" + info)
        fp.write("\n")
