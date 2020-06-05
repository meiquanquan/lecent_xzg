from .basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class ZsspPage(BasePage):
    xsywgl = (By.XPATH, '//*[@id="side-menu"]/li[4]/a/span[1]')
    zsspgl = (By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li[1]/a')
    zsspgl_frame = (By.XPATH, '//*[@id="iframe0"]')
    sjxsp = (By.XPATH, '//*[@id="GoodsSaleSetting_ListTable_Toolbar"]/a[1]')
    #out_frame
    #关闭在售商品管理页面
    #切frame
    gbzsspgl = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
    xzck = (By.XPATH, '//*[@id="GoodsSaleSettingForm_GoodsWarehouseID_chosen"]/a/span')
    xzck_input = (By.XPATH, '//*[@id="GoodsSaleSettingForm_GoodsWarehouseID_chosen"]/div/div/input')
    #ENTER
    xzgys = (By.XPATH, '//*[@id="GoodsSaleSettingForm_GoodsSupplierID_chosen"]/a/span')
    xzgys_input = (By.XPATH, '//*[@id="GoodsSaleSettingForm_GoodsSupplierID_chosen"]/div/div/input')
    # ENTER
    sptj = (By.XPATH, '//*[@id="GoodsSaleSettingForm"]/div[1]/div[3]/div/button[1]')
    spmcsr_input = (By.ID, 'GoodsSaleSettingAddWF_Keyword')
    spqrgx = (By.XPATH, '//*[@id="GoodsSaleSettingAddWF_Goods_ListTable"]/tbody/tr[2]/td[7]/button')
    sptjgb = (By.XPATH, '//*[@id="layui-layer1"]/span[1]/a[3]')
    tjsj = (By.ID, 'GoodsSaleSettingForm_SubmitButton')

    def click_xsywgl(self):
        self.find_element(*self.xsywgl).click()

    def click_zsspgl(self):
        self.find_element(*self.zsspgl).click()

    def switch_zsspgl(self):
        self.switch_frame(*self.zsspgl_frame)

    def click_sjxsp(self):
        self.find_element(*self.sjxsp).click()

    def switch_outframe(self):
        self.switch_out()

    def click_gbzsspgl(self):
        self.find_element(*self.gbzsspgl).click()

    def click_xzck(self):
        self.find_element(*self.xzck).click()

    def input_xzck(self, xzck1):
        self.find_element(*self.xzck_input).send_keys(xzck1)
        time.sleep(3)
        self.find_element(*self.xzck_input).send_keys(Keys.ENTER)

    def click_xzgys(self):
        self.find_element(*self.xzgys).click()

    def input_xzgys(self, xzgys1):
        self.find_element(*self.xzgys_input).send_keys(xzgys1)
        self.find_element(*self.xzgys_input).send_keys(Keys.ENTER)

    def click_sptj(self):
        self.find_element(*self.sptj).click()

    def input_spmcsr(self, spmc1):
        self.find_element(*self.spmcsr_input).send_keys(spmc1)

    def click_spqrgx(self):
        self.find_element(*self.spqrgx).click()

    def click_sptjgb(self):
        self.find_element(*self.sptjgb).click()

    def click_tjsj(self):
        self.find_element(*self.tjsj).click()