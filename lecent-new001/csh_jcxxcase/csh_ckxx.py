from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.ckxxpage import CkxxPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/ckxx_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
cklx11 = '普通仓库'
psms11 = '2'
mark1 = 1
mark2 = 1

class TestCkxx(unittest.TestCase):
    dr = webdriver.Firefox()
    def setUp(self,driver = dr):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)
        self.verificationErrors = []
        self.accept_next_alert = True
        time.sleep(2)
        self.dl = LoginPage(self.driver, Select)
        self.ck = CkxxPage(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1

    def testcase1(self):
        '''用例1，新增所外配送仓库01成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(3)
        self.dl.click_login()
        time.sleep(3)
        self.ck.click_jcxxgl()
        time.sleep(3)
        self.ck.click_ckxxgl()
        time.sleep(3)
        self.ck.switch_cktj()
        time.sleep(3)
        self.ck.click_cktj()
        time.sleep(3)
        self.ck.input_ckmc(data2[mark1][1])
        time.sleep(3)
        self.ck.input_ckbh(data2[mark1][2])
        time.sleep(3)
        self.ck.select_cklx(cklx11)
        time.sleep(3)
        self.ck.select_psms(psms11)
        time.sleep(3)
        self.ck.click_xsrq()
        time.sleep(3)
        self.ck.click_ygrq()
        time.sleep(3)
        self.ck.click_ygrqxz()
        time.sleep(3)
        self.ck.input_ksrq(data2[mark1][3])
        time.sleep(3)
        self.ck.input_jzrq(data2[mark1][4])
        time.sleep(3)
        self.ck.xssj_click()
        time.sleep(3)
        self.ck.click_ygsj()
        time.sleep(3)
        self.ck.click_ygsjxz()
        time.sleep(3)
        self.ck.input_kssj(data2[mark1][5])
        time.sleep(3)
        self.ck.input_jzsj(data2[mark1][6])
        time.sleep(3)
        self.ck.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

    def testcase2(self):
        '''用例2，新增所外配送仓库02成功'''
        self.ck.click_jcxxgl()
        time.sleep(3)
        self.ck.click_ckxxgl()
        time.sleep(3)
        self.ck.switch_cktj()
        time.sleep(3)
        self.ck.click_cktj()
        time.sleep(3)
        self.ck.input_ckmc(data2[mark1][1])
        time.sleep(3)
        self.ck.input_ckbh(data2[mark1][2])
        time.sleep(3)
        self.ck.select_cklx(cklx11)
        time.sleep(3)
        self.ck.select_psms(psms11)
        time.sleep(3)
        self.ck.click_xsrq()
        time.sleep(3)
        self.ck.click_ygrq()
        time.sleep(3)
        self.ck.click_ygrqxz()
        time.sleep(3)
        self.ck.input_ksrq(data2[mark1][3])
        time.sleep(3)
        self.ck.input_jzrq(data2[mark1][4])
        time.sleep(3)
        self.ck.xssj_click()
        time.sleep(3)
        self.ck.click_ygsj()
        time.sleep(3)
        self.ck.click_ygsjxz()
        time.sleep(3)
        self.ck.input_kssj(data2[mark1][5])
        time.sleep(3)
        self.ck.input_jzsj(data2[mark1][6])
        time.sleep(3)
        self.ck.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

    def testcase3(self):#最后一个测试用例，实现了只进行一次退出浏览器
        '''关闭浏览器'''
        self.driver.quit()

if __name__=='__main__':
    unittest.main()