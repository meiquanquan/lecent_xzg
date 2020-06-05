from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SpxxPage(BasePage):

    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    spxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[9]/a')
    sptj_frame = (By.XPATH, '//*[@id="iframe0"]')
    sptj = (By.XPATH, '//*[@id="Goods_ListTable_Toolbar"]/a[1]')
    spmc = (By.ID, 'GoodsWF_Name')
    spfl = (By.XPATH, '//*[@id="GoodsWF_GoodsCategoryID_chosen"]/a/span')
    spfl_input = (By.XPATH, '//*[@id="GoodsWF_GoodsCategoryID_chosen"]/div/div/input')
    spbm = (By.ID, 'GoodsWF_QRCode')
    spbzq = (By.ID, 'GoodsWF_ShelfLife')
    spzhlx_select = (By.ID, 'GoodsWF_MoneyType')

    spsxgl = (By.XPATH, '//*[@id="GoodsWF_Tab"]/li[2]/a')
    ygsx = (By.XPATH, '//*[@id="GoodsWF_Tab_2"]/div[2]/div[1]/button[1]')
    ygsxxz = (By.NAME, 'GoodsWF_GoodsAttr_IDS')
    spgg = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[2]/div/a/span')
    spgg_input = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[2]/div/div/div/input')
    spxh = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[3]/div/a/span')
    spxh_input = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[3]/div/div/div/input')
    spdw = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[4]/div/a/span')
    spdw_input = (By.XPATH, '//table[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[4]/div/div/div/input')
    spcb = (By.NAME, 'GoodsWF_GoodsAttr_CostPrice[]')
    spls = (By.NAME, 'GoodsWF_GoodsAttr_SellingPrice[]')
    spkcyj = (By.NAME, 'GoodsWF_GoodsAttr_WarningValue[]')
    bcnr = (By.ID, 'GoodsWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_spxxgl(self):
        self.find_element(*self.spxxgl).click()

    def switch_sptj(self):
        self.switch_frame(*self.sptj_frame)

    def click_sptj(self):
        self.find_element(*self.sptj).click()

    def input_spmc(self, spmc1):
        self.find_element(*self.spmc).send_keys(spmc1)

    def click_spfl(self):
        self.find_element(*self.spfl).click()

    def input_spfl(self, spfl1):
        self.find_element(*self.spfl_input).send_keys(spfl1)
        self.find_element(*self.spfl_input).send_keys(Keys.ENTER)

    def input_spbm(self, spbm1):
        self.find_element(*self.spbm).send_keys(spbm1)

    def input_spbzq(self, spbzq1):
        self.find_element(*self.spbzq).send_keys(spbzq1)

    def select_spzhlx(self, spzhlx1):
        self.q1 = self.find_element(*self.spzhlx_select)
        self.Select(self.q1).select_by_value(spzhlx1)


    def click_spsxgl(self):
        self.find_element(*self.spsxgl).click()

    def click_ygsx(self):
        self.find_element(*self.ygsx).click()

    def click_ygsxxz(self):
        self.find_element(*self.ygsxxz).click()

    def click_spgg(self):
        self.find_element(*self.spgg).click()

    def input_spgg(self, spgg1):
        self.find_element(*self.spgg_input).send_keys(spgg1)
        self.find_element(*self.spgg_input).send_keys(Keys.ENTER)

    def click_spxh(self):
        self.find_element(*self.spxh).click()

    def input_spxh(self, spxh1):
        self.find_element(*self.spxh_input).send_keys(spxh1)
        self.find_element(*self.spxh_input).send_keys(Keys.ENTER)

    def click_spdw(self):
        self.find_element(*self.spdw).click()

    def input_spdw(self, spdw1):
        self.find_element(*self.spdw_input).send_keys(spdw1)
        self.find_element(*self.spdw_input).send_keys(Keys.ENTER)

    def input_spcb(self, spcb1):
        self.find_element(*self.spcb).send_keys(spcb1)

    def input_spls(self, spls1):
        self.find_element(*self.spls).send_keys(spls1)

    def input_spkcyj(self, spkcyj1):
        self.find_element(*self.spkcyj).send_keys(spkcyj1)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()

