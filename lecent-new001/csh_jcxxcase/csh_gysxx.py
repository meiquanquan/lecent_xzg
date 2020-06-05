from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.gysxxpage import GysxxPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/gysxx_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1
mark2 = 1
gyslx1 = '经销商'

class TestGysxx(unittest.TestCase):
    dr = webdriver.Firefox()
    def setUp(self, driver=dr):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)
        self.accept_next_alert = True
        time.sleep(2)
        self.dl = LoginPage(self.driver, Select)
        self.gys = GysxxPage(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1

    def testcase1(self):
        '''用例1，新增1号供应商成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(3)
        self.dl.click_login()
        time.sleep(3)
        self.gys.click_jcxxgl()
        time.sleep(3)
        self.gys.click_gysxxgl()
        time.sleep(3)
        self.gys.switch_gysxxgl()
        time.sleep(3)
        self.gys.click_gystj()
        time.sleep(3)
        self.gys.input_gysmc(data2[mark1][1])
        time.sleep(3)
        self.gys.input_gysbh(data2[mark1][2])
        time.sleep(3)
        self.gys.select_gyslx(gyslx1)
        time.sleep(3)
        self.gys.click_gysbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase2(self):
        '''用例2，新增2号供应商成功'''
        self.gys.click_jcxxgl()
        time.sleep(3)
        self.gys.click_gysxxgl()
        time.sleep(3)
        self.gys.switch_gysxxgl()
        time.sleep(3)
        self.gys.click_gystj()
        time.sleep(3)
        self.gys.input_gysmc(data2[mark1][1])
        time.sleep(3)
        self.gys.input_gysbh(data2[mark1][2])
        time.sleep(3)
        self.gys.select_gyslx(gyslx1)
        time.sleep(3)
        self.gys.click_gysbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase3(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()