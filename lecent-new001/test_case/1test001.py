from selenium import webdriver
from assertpy import assert_that
import time
driver1 = webdriver.Firefox()
driver2 = webdriver.Firefox()
url1 = 'https://mail.qq.com/'
url2 = 'https://mail.sina.com.cn/'
driver1.get(url1)
time.sleep(3)
print('driver1-qq的句柄:', driver1.current_window_handle)
driver1.get(url2)
time.sleep(3)
print('driver2-新浪的句柄:', driver1.current_window_handle)



'''
#实现指定多个url同时打开
web = ['https://mail.163.com/', 'https://mail.qq.com/', 'https://www.baidu.com/', 'https://mail.sina.com.cn/']
for w in web:
    js = 'window.open("%s")' % w
    driver.execute_script(js)
    print('--------------' * 6)
    print(w)
    print(web.index(w))
    print('当前句柄：', driver.current_window_handle)
    print('所有的句柄： ', driver.window_handles)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    print('当前句柄：', driver.current_window_handle)
    print('当前title：', driver.title)
    print('--------------' * 6)
time.sleep(1)
driver.quit()

################################
#实现断言：unittest框架自带assert断言/非框架的需引入第三方包assertpy,各自的断言方法不一致
driver.get("https://www.baidu.com")
print(driver.current_url)

#尝试第三方包
try:
    assert_that(driver.current_url).contains('baidu')# 断言，判断页面URL中是否包含emails
except:
    raise Exception  # 手动抛出异常，确保测试结果的正确性
driver.quit()


###########=======================
#unittest自带断言
try:
    self.assertIn('emails', self.ro.get_url())  # 断言，判断页面URL中是否包含emails
except:
    self.ro.get_img(ut.IMG_PATH + '/reg_%d.png' % (mark))  # 断言失败截图
    raise Exception  # 手动抛出异常，确保测试结果的正确性
    
######################################
#执行每条用例后仅重载页面，不退出。最后一条用例推出浏览器
def test_zzz_quit(self):#最后一个测试用例，实现了只进行一次退出浏览器
    self.driver.quit()
 
def tearDown(self):
    try:
        self.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
    except ConnectionRefusedError as e:
        print(e)
    finally:
        self.assertEqual([], self.verificationErrors)
'''