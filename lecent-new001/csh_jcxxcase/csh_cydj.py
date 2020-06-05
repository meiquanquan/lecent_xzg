from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys, time, unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.cydjpage import CydjPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/cydj_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1
mark2 = 1

class TestJqxx(unittest.TestCase):
    dr = webdriver.Firefox()
    def setUp(self, driver=dr):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)
        self.verificationErrors = []
        self.accept_next_alert = True
        time.sleep(2)
        self.dl = LoginPage(self.driver, Select)
        self.cydj = CydjPage(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1

    def testcase1(self):
        '''用例1、新增罪犯一级处遇等级成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(2)
        self.dl.click_login()
        time.sleep(3)
        self.cydj.click_jqxxgl()
        time.sleep(3)
        self.cydj.click_zfzjgl()
        time.sleep(5)
        self.cydj.swatch_djsz()
        time.sleep(3)
        self.cydj.click_djsz()
        time.sleep(3)
        self.cydj.click_djtj()
        time.sleep(3)
        self.cydj.input_djmc(data2[mark2][1])
        time.sleep(3)
        self.cydj.input_djbh(data2[mark2][2])
        time.sleep(3)
        self.cydj.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

    def testcase2(self):
        '''用例2、新增罪犯二级处遇等级成功'''
        self.cydj.click_jqxxgl()
        time.sleep(3)
        self.cydj.click_zfzjgl()
        time.sleep(5)
        self.cydj.swatch_djsz()
        time.sleep(3)
        self.cydj.click_djsz()
        time.sleep(3)
        self.cydj.click_djtj()
        time.sleep(3)
        self.cydj.input_djmc(data2[mark2][1])
        time.sleep(3)
        self.cydj.input_djbh(data2[mark2][2])
        time.sleep(3)
        self.cydj.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

    def testcase3(self):
        '''关闭浏览器'''
        self.driver.quit()

if __name__=='__main__':
    unittest.main()