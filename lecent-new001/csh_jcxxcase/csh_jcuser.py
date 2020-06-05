from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.jc_userpage import UserPage
import utils.util as ut
file1=ut.DATA_PATH+'/user_data.csv'
data1=ut.get_data(file1)
url=co.getbrowsername('Url')
#dri=co.getbrowsername('BrowserName')
mark1=1
class TestUser(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)
        self.dl=LoginPage(self.driver,Select)
        self.user=UserPage(self.driver,Select)

    def tearDown(self):
        global mark1
        mark1+=1
        self.driver.quit()

    def testcase1(self):
        '''用例1，新增用户成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(2)
        self.dl.click_login()
        time.sleep(4)
        self.user.click_jcxxgl()
        self.user.click_yhxxgl()
        time.sleep(4)
        self.user.switch_yhtj()
        time.sleep(4)
        self.user.click_yhtj()
        time.sleep(2)
        self.user.select_bm()
        self.user.select_gw()
        self.user.input_yhxm(data1[mark1][2])
        self.user.input_yhbh(data1[mark1][3])
        self.user.input_dlzh(data1[mark1][4])
        self.user.input_dlmm(data1[mark1][5])
        self.user.input_qrmm(data1[mark1][6])
        time.sleep(5)
        self.user.click_submit()
        time.sleep(5)

        try:
            self.assertIn('emails', self.user.get_url())  # 断言，判断页面URL中是否包含emails
        except:
            self.user.get_img(ut.IMG_PATH+'/reg_%d.png' % (mark1))  # 断言失败截图
            raise Exception  # 手动抛出异常，确保测试结果的正确性

if __name__=='__main__':
    unittest.main()


