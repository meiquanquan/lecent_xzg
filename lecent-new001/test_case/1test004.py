
from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest,re
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.xfgk1cyed1xfedpage import Cyed1xfedPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/cyed_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1

class TestCyed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(url)
        time.sleep(2)
        cls.dl = LoginPage(cls.driver, Select)
        cls.cyed1 = Cyed1xfedPage(cls.driver, Select)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        global mark1
        mark1 += 1
        self.driver.refresh()

    def testcase1(self):

        self.dl.input_name(52525252)
        time.sleep(2)
        self.dl.input_pwd(123456)
        time.sleep(2)
        self.dl.click_login()
        time.sleep(2)
        #供应站购物
        # 第三次购买同一A商品
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_gyzxs()
        time.sleep(3)
        self.cyed1.switch_gyzxs()
        time.sleep(3)
        self.cyed1.input_gyzzfxm(3653001)
        time.sleep(3)
        self.cyed1.click_cksrk()
        time.sleep(3)
        self.cyed1.input_cksrk('所外配送仓库01')
        time.sleep(3)
        self.cyed1.input_spbh(566301)
        time.sleep(3)
        self.cyed1.click_spxsjz()
        time.sleep(3)
        self.cyed1.click_qrjz()
        time.sleep(2)
        self.cyed1.switch_outframe()
        #self.cyed1.click_tkqr()
        self.b = self.cyed1.gett_tknr()
        print(self.b)
        #目前的断言有点不得吃
        try:
            self.assertIn('购买失败', self.b)  # 断言，判断页面URL中是否包含emails
        except:
            self.cyed1.get_img(ut.IMG_PATH + '/1test_%d.png' % (mark1))  # 断言失败截图
            raise Exception  # 手动抛出异常，确保测试结果的正确性



if __name__=='__main__':
    unittest.main()



'''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.maximize_window()
url = 'http://zg.lecent.cn:9081/admin/index'
driver.get(url)
time.sleep(3)
driver.find_element_by_id('UserName').send_keys('52525252')
time.sleep(3)
driver.find_element_by_id('Password').send_keys('123456')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="LoginForm"]/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/ul/li[2]/a').click()
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="iframe0"]'))
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys('3653001')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys(Keys.DOWN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/div/div/input').send_keys('	所外配送仓库01')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys('566301')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys(Keys.DOWN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_SubmitButton"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Modal_SaleSettyle"]').click()
time.sleep(3)
driver.switch_to.default_content()
a = driver.find_element_by_css_selector('html body.fixed-nav.fixed-sidebar.full-height-layout.gray-bg div#layui-layer4.layui-layer.layui-layer-dialog.layer-ext-moon div.layui-layer-content.layui-layer-padding').text          #get_attribute('textContent')
print(a)
'''

