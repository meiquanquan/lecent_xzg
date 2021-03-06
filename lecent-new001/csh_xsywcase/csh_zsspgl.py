from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.zsspglpage import ZsspPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/zsspgl_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1


class TestZsspgl(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(url)
        time.sleep(2)
        cls.dl = LoginPage(cls.driver, Select)
        cls.zssp = ZsspPage(cls.driver, Select)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        global mark1
        mark1 += 1
        self.driver.refresh()


    def testcase1(cls):
        '''用例1，新增负库存A-1商品成功'''
        cls.dl.input_name(data1[mark1][0])
        time.sleep(2)
        cls.dl.input_pwd(data1[mark1][1])
        time.sleep(3)
        cls.dl.click_login()
        time.sleep(3)
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase2(cls):
        '''用例2，新增负库存A-2商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase3(cls):
        '''用例3，新增负库存B-1商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)


    def testcase4(cls):
        '''用例4，新增负库存B-2商品成功'''
        time.sleep(3)
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase5(cls):
        '''用例5，新增负库存AB-1商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase6(cls):
        '''用例6，新增负库存AB-2商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase7(cls):
        '''用例7，新增负库存BA-1商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase8(cls):
        '''用例8，新增负库存BA-2商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase9(cls):
        '''用例9，新增负库存无-1商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

    def testcase10(cls):
        '''用例10，新增负库存无-2商品成功'''
        cls.zssp.click_xsywgl()
        time.sleep(3)
        cls.zssp.click_zsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_sjxsp()
        time.sleep(3)
        cls.zssp.switch_outframe()
        time.sleep(3)
        cls.zssp.click_gbzsspgl()
        time.sleep(3)
        cls.zssp.switch_zsspgl()
        time.sleep(3)
        cls.zssp.click_xzck()
        time.sleep(3)
        cls.zssp.input_xzck(data2[mark1][1])
        time.sleep(3)
        cls.zssp.click_xzgys()
        time.sleep(3)
        cls.zssp.input_xzgys(data2[mark1][2])
        time.sleep(3)
        cls.zssp.click_sptj()
        time.sleep(5)
        cls.zssp.input_spmcsr(data2[mark1][3])
        time.sleep(3)
        cls.zssp.click_spqrgx()
        time.sleep(3)
        cls.zssp.click_sptjgb()
        time.sleep(3)
        cls.zssp.click_tjsj()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()