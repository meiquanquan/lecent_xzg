from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys, time, unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.spxx_xhggpage import SpxxxhggPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/spxxxhgg_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1
mark2 = 1

class TestSpxhgg(unittest.TestCase):
    dr = webdriver.Firefox()
    def setUp(self, driver=dr):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)
        self.accept_next_alert = True
        time.sleep(2)
        self.dl = LoginPage(self.driver, Select)
        self.spxx = SpxxxhggPage(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1

    def testcase1(self):
        '''用例1、新增商品规格1/型号1成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(2)
        self.dl.click_login()
        time.sleep(3)
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spgg()
        time.sleep(3)
        self.spxx.click_spggtj()
        time.sleep(3)
        self.spxx.input_spggmc(data2[mark1][1])
        time.sleep(3)
        self.spxx.click_spggbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spxh()
        time.sleep(3)
        self.spxx.click_spxhtj()
        time.sleep(3)
        self.spxx.input_spxhmc(data2[mark1][2])
        time.sleep(3)
        self.spxx.click_spxhbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase2(self):
        '''用例2、新增商品规格2/型号2成功'''
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spgg()
        time.sleep(3)
        self.spxx.click_spggtj()
        time.sleep(3)
        self.spxx.input_spggmc(data2[mark1][1])
        time.sleep(3)
        self.spxx.click_spggbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spxh()
        time.sleep(3)
        self.spxx.click_spxhtj()
        time.sleep(3)
        self.spxx.input_spxhmc(data2[mark1][2])
        time.sleep(3)
        self.spxx.click_spxhbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase3(self):
        '''用例3、新增商品规格3/型号3成功'''
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spgg()
        time.sleep(3)
        self.spxx.click_spggtj()
        time.sleep(3)
        self.spxx.input_spggmc(data2[mark1][1])
        time.sleep(3)
        self.spxx.click_spggbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spxh()
        time.sleep(3)
        self.spxx.click_spxhtj()
        time.sleep(3)
        self.spxx.input_spxhmc(data2[mark1][2])
        time.sleep(3)
        self.spxx.click_spxhbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase4(self):
        '''用例4、新增商品规格4/型号4成功'''
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spgg()
        time.sleep(3)
        self.spxx.click_spggtj()
        time.sleep(3)
        self.spxx.input_spggmc(data2[mark1][1])
        time.sleep(3)
        self.spxx.click_spggbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.spxx.click_jcxxgl()
        time.sleep(3)
        self.spxx.click_spxxgl()
        time.sleep(3)
        self.spxx.switch_spxx()
        time.sleep(3)
        self.spxx.click_spxh()
        time.sleep(3)
        self.spxx.click_spxhtj()
        time.sleep(3)
        self.spxx.input_spxhmc(data2[mark1][2])
        time.sleep(3)
        self.spxx.click_spxhbc()
        time.sleep(3)
        self.driver.refresh()

    def testcase5(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()