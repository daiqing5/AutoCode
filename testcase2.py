import time
from selenium import webdriver
from PIL import Image
import pytesseract


def test1():
    browser = webdriver.Chrome()
    browser.get("http://www.jpress.io/user/register")
    browser.maximize_window()
    time.sleep(3)
    # 获取图片验证码
    t = time.time()
    picture_name1 = str(t) + '.png'
    browser.save_screenshot(picture_name1)
    print('获取到的图片信息：', picture_name1)
    ce = browser.find_element_by_id("captchaimg")
    # 获取改元素的横纵坐标
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    # 抠图
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = str(t) + '.png'
    # 获取截取验证，码图片
    img.save(picture_name2)
    print('获取抠图的图片信息：', picture_name2)
    browser.close()


def test2():
    image1 = Image.open('123.png')
    stria = pytesseract.image_to_string(image1)
    print(stria)
