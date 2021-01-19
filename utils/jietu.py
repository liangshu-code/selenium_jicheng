import time

def jietu(driver, Cname):
    now = time.strftime("%y-%m-%d")
    now_1 = time.strftime("%y-%m-%d %H_%M_%S")[9:]
    driver.get_screenshot_as_file(".\\report\\" + now + "\\png\\" + Cname + "_" + now_1 + ".png")

