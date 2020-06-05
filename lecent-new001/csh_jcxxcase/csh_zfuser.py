from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.zf_userpage import UserPagezf
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/zfuser_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1
mark2 = 1
zfxb1v = '男'

class TestUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)
        self.dl = LoginPage(self.driver, Select)
        self.zfuser = UserPagezf(self.driver, Select)

    def tearDown(self):
        global mark1, mark2
        mark1 += 1
        mark2 += 1
        self.driver.quit()

    def testcase1(self):
        '''用例1，新增罪犯成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(2)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(3)
        self.dl.click_login()
        time.sleep(3)
        self.zfuser.click_jcxxgl()
        time.sleep(3)
        self.zfuser.click_zfxxgl()
        time.sleep(3)
        self.zfuser.switch_zftj()
        time.sleep(3)
        self.zfuser.click_zftj()
        time.sleep(3)
        self.zfuser.click_ssjq()
        time.sleep(3)
        self.zfuser.input_ssjq(data2[mark1][1])
        time.sleep(3)
        self.zfuser.input_zfxm(data2[mark1][2])
        time.sleep(3)
        self.zfuser.input_zfbh(data2[mark1][3])
        time.sleep(3)
        self.zfuser.select_zfxb(zfxb1v)
        time.sleep(3)
        self.zfuser.click_cydj()
        time.sleep(3)
        self.zfuser.input_cydj(data2[mark1][4])
        time.sleep(3)
        self.zfuser.click_srlb()
        time.sleep(3)
        self.zfuser.input_srlb(data2[mark1][5])
        time.sleep(3)
        self.zfuser.click_zflx()
        time.sleep(3)
        self.zfuser.input_zflx(data2[mark1][6])
        time.sleep(3)
        self.zfuser.click_bcnr()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()