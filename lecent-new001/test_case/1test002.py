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
web = co.getbrowsername('Web')
cklx11 = '普通仓库'
psms11 = '2'
mark1 = 1
mark2 = 1

class TestCkxx(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        web_list = web.strip(',').split(',')

        for w in web_list:
            js = 'window.open("%s")' % w
            self.driver.execute_script(js)
            time.sleep(5)
            print('当前句柄：', self.driver.current_window_handle)
            print('所有的句柄： ', self.driver.window_handles)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(5)
            print('当前句柄：', self.driver.current_window_handle)
            print('当前title：', self.driver.title)

        all_handles = self.driver.window_handles
        print(all_handles)
        self.driver.switch_to.window(all_handles[1])  # 9081[1]、9086[2]
        time.sleep(5)
        self.dl = LoginPage(self.driver, Select)
        self.ck = CkxxPage(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1
        #self.driver.quit()

    def testcase1(self):
        '''用例1，新增仓库成功'''
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

if __name__=='__main__':
    unittest.main()