from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys,time,unittest,re
import common.ReadConfig as co
sys.path.append('..')
from pages.loginpage import LoginPage
from pages.zf_userpage import UserPagezf
from pages.jqxxpage import JqxxPage
from pages.xfgk1cyed1xfedpage import Cyed1xfedPage
import utils.util as ut
file1 = ut.DATA_PATH+'/user_data.csv'
data1 = ut.get_data(file1)
file2 = ut.DATA_PATH+'/zfzjq_data.csv'
data2 = ut.get_data(file2)
url = co.getbrowsername('Url')
mark1 = 1

class TestCyed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get(url)
        time.sleep(3)
        cls.dl = LoginPage(cls.driver, Select)
        cls.zfuser = UserPagezf(cls.driver, Select)
        cls.jqxx = JqxxPage(cls.driver, Select)
        cls.cyed1 = Cyed1xfedPage(cls.driver, Select)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        global mark1
        mark1 += 1
        self.driver.refresh()

    def testcase01(self):
        '''用例1，原监区不在销售时间-新监区在销售时间，罪犯在原监区购物失败，转新监区后购物成功'''
        self.dl.input_name(data1[mark1][0])
        time.sleep(3)
        self.dl.input_pwd(data1[mark1][1])
        time.sleep(3)
        self.dl.click_login()
        time.sleep(3)

        #1、修改A监区一分监区的销售日期【可购物】
        self.jqxx.click_jcxxgl()
        time.sleep(3)
        self.jqxx.click_jqxxgl()
        time.sleep(3)
        self.jqxx.switch_jqtj()
        time.sleep(3)
        self.jqxx.click_jqxxxga()
        time.sleep(3)
        self.jqxx.click_xsrq()
        time.sleep(3)
        self.jqxx.input_ksrq(data2[mark1][1])
        time.sleep(3)
        self.jqxx.input_jzrq(data2[mark1][2])
        time.sleep(3)
        self.jqxx.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

        #2、修改B监区一分监区的销售日期【不可购物】
        self.jqxx.click_jcxxgl()
        time.sleep(3)
        self.jqxx.click_jqxxgl()
        time.sleep(3)
        self.jqxx.switch_jqtj()
        time.sleep(3)
        self.jqxx.click_jqxxxgb()
        time.sleep(3)
        self.jqxx.click_xsrq()
        time.sleep(3)
        self.jqxx.input_ksrq(data2[mark1][3])
        time.sleep(3)
        self.jqxx.input_jzrq(data2[mark1][4])
        time.sleep(3)
        self.jqxx.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

        #3、新增罪犯关联【不可购物监区】
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
        self.zfuser.input_ssjq(data2[mark1][6])
        time.sleep(3)
        self.zfuser.input_zfxm(data2[mark1][7])
        time.sleep(3)
        self.zfuser.input_zfbh(data2[mark1][8])
        time.sleep(3)
        self.zfuser.click_zfxb()
        time.sleep(3)
        self.zfuser.input_zfxbsr(data2[mark1][9])
        time.sleep(3)
        self.zfuser.click_cydj()
        time.sleep(3)
        self.zfuser.input_cydj(data2[mark1][10])
        time.sleep(3)
        self.zfuser.click_srlb()
        time.sleep(3)
        self.zfuser.input_srlb(data2[mark1][11])
        time.sleep(3)
        self.zfuser.click_bcnr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        #4、罪犯资金上账【A账户】
        self.cyed1.click_zjywgl()
        time.sleep(3)
        self.cyed1.click_zjsz()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_xzsz()
        time.sleep(3)
        self.cyed1.switch_outframe()
        time.sleep(3)
        self.cyed1.click_zjszgb()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_szzjfl()
        time.sleep(3)
        self.cyed1.input_szzjfl(data2[mark1][12])
        time.sleep(3)
        self.cyed1.click_szzjlx()
        time.sleep(3)
        self.cyed1.input_szzjlx(data2[mark1][13])
        time.sleep(3)
        self.cyed1.input_szzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.input_szje(data2[mark1][14])
        time.sleep(3)
        self.cyed1.click_qbsz()
        time.sleep(3)
        self.cyed1.click_szxyb()
        time.sleep(3)
        self.cyed1.click_szxyb()
        time.sleep(3)
        self.cyed1.click_szgb()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_zjywgl()
        time.sleep(3)
        self.cyed1.click_zjsz()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_tjsz()
        time.sleep(3)
        self.cyed1.click_qrsz()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        #5、修改关联处遇额度
        self.cyed1.click_zfxfgk()
        time.sleep(3)
        self.cyed1.click_cyed()
        time.sleep(3)
        self.cyed1.switch_cyed()
        time.sleep(3)
        self.cyed1.click_ze1bxz()
        time.sleep(3)
        self.cyed1.click_a1bxz()
        time.sleep(3)
        self.cyed1.click_b1bxz()
        time.sleep(3)
        self.cyed1.click_gwcsbxz()
        time.sleep(3)

        # ------【一级处遇等级{高}】
        self.cyed1.click_a1xz()
        time.sleep(3)
        self.cyed1.input_a1(data2[mark1][15])
        time.sleep(3)

        self.cyed1.click_cyedbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        #6、初始化指定商品类型改价【修改A-1、A-2】
        self.cyed1.click_jcxxgl()
        time.sleep(3)
        self.cyed1.click_ckxxgl()
        time.sleep(3)
        self.cyed1.switch_ckxxgl()
        time.sleep(3)
        self.cyed1.click_ck1zcck()  # 一关
        time.sleep(3)
        self.cyed1.click_cktkqr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_zsspgl()
        time.sleep(3)
        self.cyed1.switch_zsspgl()
        time.sleep(4)
        self.cyed1.click_spyjtj()
        time.sleep(3)
        self.cyed1.switch_outframe()
        time.sleep(3)
        self.cyed1.click_zsspgb()
        time.sleep(3)
        self.cyed1.switch_zsspgl()
        time.sleep(3)
        self.cyed1.click_xzsp()
        time.sleep(3)
        # 商品1
        self.cyed1.input_spbhsrk(data2[mark1][17])
        time.sleep(3)
        self.cyed1.click_cpcx()
        time.sleep(3)
        self.cyed1.click_xzspgx()
        time.sleep(3)
        # 商品2
        self.cyed1.input_spbhsrk(data2[mark1][20])
        time.sleep(3)
        self.cyed1.click_cpcx()
        time.sleep(3)
        self.cyed1.click_xzspgx()
        time.sleep(3)

        self.cyed1.click_gbspxz()
        time.sleep(3)
        # 商品一新临售
        self.cyed1.input_sp1xls(data2[mark1][18])
        time.sleep(3)
        # 商品二新临售
        self.cyed1.input_sp2xls(data2[mark1][21])
        time.sleep(3)
        self.cyed1.click_tjtj()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_jcxxgl()
        time.sleep(3)
        self.cyed1.click_ckxxgl()
        time.sleep(3)
        self.cyed1.switch_ckxxgl()
        time.sleep(3)
        self.cyed1.click_ck1zcck()  # 二开
        time.sleep(3)
        self.cyed1.click_cktkqr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        #7、供应站销售购物失败
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_gyzxs()
        time.sleep(3)
        self.cyed1.switch_gyzxs()
        time.sleep(3)
        self.cyed1.input_gyzzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.click_cksrk()
        time.sleep(3)
        self.cyed1.input_cksrk(data2[mark1][22])
        time.sleep(3)
        self.cyed1.input_spbh(data2[mark1][17])
        time.sleep(3)
        self.cyed1.click_spxsjz()
        time.sleep(3)
        self.cyed1.click_qrjz()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        #8、罪犯转监区【可购物监区】
        self.zfuser.click_jcxxgl()
        time.sleep(3)
        self.zfuser.click_zfxxgl()
        time.sleep(3)
        self.zfuser.switch_zftj()
        time.sleep(3)
        self.zfuser.input_zfxxcxbhsrk(data2[mark1][8])
        time.sleep(3)
        self.zfuser.click_zfxxglcxan()
        time.sleep(3)
        self.zfuser.click_zfxxglgx()
        time.sleep(3)
        self.zfuser.click_zfplzjq()
        time.sleep(3)
        self.zfuser.switch_outframe()
        time.sleep(3)
        self.zfuser.click_gbzfxxgl()
        time.sleep(3)
        self.zfuser.switch_zftj()
        time.sleep(3)
        self.zfuser.select_zrjq('143')  #A监区value=143
        time.sleep(3)
        self.zfuser.click_zfzjqxyb()
        time.sleep(3)
        self.zfuser.click_zfzjqxyb()
        time.sleep(3)
        self.driver.refresh()

        #9、供应站销售购物成功
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_gyzxs()
        time.sleep(3)
        self.cyed1.switch_gyzxs()
        time.sleep(3)
        self.cyed1.input_gyzzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.click_cksrk()
        time.sleep(3)
        self.cyed1.input_cksrk(data2[mark1][22])
        time.sleep(3)
        self.cyed1.input_spbh(data2[mark1][20])
        time.sleep(3)
        self.cyed1.click_spxsjz()
        time.sleep(3)
        self.cyed1.click_qrjz()
        self.cyed1.switch_outframe()
        self.b = self.cyed1.gett_gwtknr()
        try:
            self.assertIn('销售成功', self.b)
        except:
            self.cyed1.get_img(ut.IMG_PATH + '/罪犯转监区模块_%d.png' % (mark1))
            raise Exception

    def testcase02(self):
        '''用例2，原监区在销售时间-新监区不在销售时间，罪犯在原监区购物成功，转新监区后购物失败'''

        # 1、修改A监区一分监区的销售日期【可购物】
        self.jqxx.click_jcxxgl()
        time.sleep(3)
        self.jqxx.click_jqxxgl()
        time.sleep(3)
        self.jqxx.switch_jqtj()
        time.sleep(3)
        self.jqxx.click_jqxxxga()
        time.sleep(3)
        self.jqxx.click_xsrq()
        time.sleep(3)
        self.jqxx.input_ksrq(data2[mark1][1])
        time.sleep(3)
        self.jqxx.input_jzrq(data2[mark1][2])
        time.sleep(3)
        self.jqxx.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

        # 2、修改B监区一分监区的销售日期【不可购物】
        self.jqxx.click_jcxxgl()
        time.sleep(3)
        self.jqxx.click_jqxxgl()
        time.sleep(3)
        self.jqxx.switch_jqtj()
        time.sleep(3)
        self.jqxx.click_jqxxxgb()
        time.sleep(3)
        self.jqxx.click_xsrq()
        time.sleep(3)
        self.jqxx.input_ksrq(data2[mark1][3])
        time.sleep(3)
        self.jqxx.input_jzrq(data2[mark1][4])
        time.sleep(3)
        self.jqxx.click_bcnr()
        time.sleep(3)
        self.driver.refresh()

        # 3、新增罪犯关联【可购物监区】
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
        self.zfuser.input_ssjq(data2[mark1][5])
        time.sleep(3)
        self.zfuser.input_zfxm(data2[mark1][7])
        time.sleep(3)
        self.zfuser.input_zfbh(data2[mark1][8])
        time.sleep(3)
        self.zfuser.click_zfxb()
        time.sleep(3)
        self.zfuser.input_zfxbsr(data2[mark1][9])
        time.sleep(3)
        self.zfuser.click_cydj()
        time.sleep(3)
        self.zfuser.input_cydj(data2[mark1][10])
        time.sleep(3)
        self.zfuser.click_srlb()
        time.sleep(3)
        self.zfuser.input_srlb(data2[mark1][11])
        time.sleep(3)
        self.zfuser.click_bcnr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        # 4、罪犯资金上账【A账户】
        self.cyed1.click_zjywgl()
        time.sleep(3)
        self.cyed1.click_zjsz()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_xzsz()
        time.sleep(3)
        self.cyed1.switch_outframe()
        time.sleep(3)
        self.cyed1.click_zjszgb()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_szzjfl()
        time.sleep(3)
        self.cyed1.input_szzjfl(data2[mark1][12])
        time.sleep(3)
        self.cyed1.click_szzjlx()
        time.sleep(3)
        self.cyed1.input_szzjlx(data2[mark1][13])
        time.sleep(3)
        self.cyed1.input_szzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.input_szje(data2[mark1][14])
        time.sleep(3)
        self.cyed1.click_qbsz()
        time.sleep(3)
        self.cyed1.click_szxyb()
        time.sleep(3)
        self.cyed1.click_szxyb()
        time.sleep(3)
        self.cyed1.click_szgb()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_zjywgl()
        time.sleep(3)
        self.cyed1.click_zjsz()
        time.sleep(3)
        self.cyed1.switch_zjsz()
        time.sleep(3)
        self.cyed1.click_tjsz()
        time.sleep(3)
        self.cyed1.click_qrsz()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        # 5、修改关联处遇额度
        self.cyed1.click_zfxfgk()
        time.sleep(3)
        self.cyed1.click_cyed()
        time.sleep(3)
        self.cyed1.switch_cyed()
        time.sleep(3)
        self.cyed1.click_ze1bxz()
        time.sleep(3)
        self.cyed1.click_a1bxz()
        time.sleep(3)
        self.cyed1.click_b1bxz()
        time.sleep(3)
        self.cyed1.click_gwcsbxz()
        time.sleep(3)

        # ------【一级处遇等级{高}】
        self.cyed1.click_a1xz()
        time.sleep(3)
        self.cyed1.input_a1(data2[mark1][15])
        time.sleep(3)

        self.cyed1.click_cyedbc()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        # 6、初始化指定商品类型改价【修改A-1、A-2】
        self.cyed1.click_jcxxgl()
        time.sleep(3)
        self.cyed1.click_ckxxgl()
        time.sleep(3)
        self.cyed1.switch_ckxxgl()
        time.sleep(3)
        self.cyed1.click_ck1zcck()  # 一关
        time.sleep(3)
        self.cyed1.click_cktkqr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_zsspgl()
        time.sleep(3)
        self.cyed1.switch_zsspgl()
        time.sleep(4)
        self.cyed1.click_spyjtj()
        time.sleep(3)
        self.cyed1.switch_outframe()
        time.sleep(3)
        self.cyed1.click_zsspgb()
        time.sleep(3)
        self.cyed1.switch_zsspgl()
        time.sleep(3)
        self.cyed1.click_xzsp()
        time.sleep(3)
        # 商品1
        self.cyed1.input_spbhsrk(data2[mark1][17])
        time.sleep(3)
        self.cyed1.click_cpcx()
        time.sleep(3)
        self.cyed1.click_xzspgx()
        time.sleep(3)
        # 商品2
        self.cyed1.input_spbhsrk(data2[mark1][20])
        time.sleep(3)
        self.cyed1.click_cpcx()
        time.sleep(3)
        self.cyed1.click_xzspgx()
        time.sleep(3)

        self.cyed1.click_gbspxz()
        time.sleep(3)
        # 商品一新临售
        self.cyed1.input_sp1xls(data2[mark1][18])
        time.sleep(3)
        # 商品二新临售
        self.cyed1.input_sp2xls(data2[mark1][21])
        time.sleep(3)
        self.cyed1.click_tjtj()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.cyed1.click_jcxxgl()
        time.sleep(3)
        self.cyed1.click_ckxxgl()
        time.sleep(3)
        self.cyed1.switch_ckxxgl()
        time.sleep(3)
        self.cyed1.click_ck1zcck()  # 二开
        time.sleep(3)
        self.cyed1.click_cktkqr()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        # 7、供应站销售购物成功
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_gyzxs()
        time.sleep(3)
        self.cyed1.switch_gyzxs()
        time.sleep(3)
        self.cyed1.input_gyzzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.click_cksrk()
        time.sleep(3)
        self.cyed1.input_cksrk(data2[mark1][22])
        time.sleep(3)
        self.cyed1.input_spbh(data2[mark1][17])
        time.sleep(3)
        self.cyed1.click_spxsjz()
        time.sleep(3)
        self.cyed1.click_qrjz()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

        # 8、罪犯转监区【不可购物监区】
        self.zfuser.click_jcxxgl()
        time.sleep(3)
        self.zfuser.click_zfxxgl()
        time.sleep(3)
        self.zfuser.switch_zftj()
        time.sleep(3)
        self.zfuser.input_zfxxcxbhsrk(data2[mark1][8])
        time.sleep(3)
        self.zfuser.click_zfxxglcxan()
        time.sleep(3)
        self.zfuser.click_zfxxglgx()
        time.sleep(3)
        self.zfuser.click_zfplzjq()
        time.sleep(3)
        self.zfuser.switch_outframe()
        time.sleep(3)
        self.zfuser.click_gbzfxxgl()
        time.sleep(3)
        self.zfuser.switch_zftj()
        time.sleep(3)
        self.zfuser.select_zrjq('145')  #B监区value=145
        time.sleep(3)
        self.zfuser.click_zfzjqxyb()
        time.sleep(3)
        self.zfuser.click_zfzjqxyb()
        time.sleep(3)
        self.driver.refresh()
        
        # 9、供应站销售购物失败
        self.cyed1.click_xsywgl()
        time.sleep(3)
        self.cyed1.click_gyzxs()
        time.sleep(3)
        self.cyed1.switch_gyzxs()
        time.sleep(3)
        self.cyed1.input_gyzzfxm(data2[mark1][8])
        time.sleep(3)
        self.cyed1.click_cksrk()
        time.sleep(3)
        self.cyed1.input_cksrk(data2[mark1][22])
        time.sleep(3)
        self.cyed1.input_spbh(data2[mark1][20])
        time.sleep(3)
        self.cyed1.click_spxsjz()
        time.sleep(3)
        self.cyed1.click_qrjz()
        self.cyed1.switch_outframe()
        self.b = self.zfuser.gett_ddcjsbtknr()
        try:
            self.assertIn('订单创建失败', self.b)
        except:
            self.cyed1.get_img(ut.IMG_PATH + '/罪犯转监区模块_%d.png' % (mark1))
            raise Exception


if __name__=='__main__':
    unittest.main()
