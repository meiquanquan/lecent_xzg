from .basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class CkxxPage(BasePage):
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    ckxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[10]/a')
    cktj_frame = (By.XPATH, '//*[@id="iframe0"]')
    cktj = (By.XPATH, '//*[@id="GoodsWarehouse_ListTable_Toolbar"]/a[1]')
    ckmc = (By.ID, 'GoodsWarehouseWF_Name')
    ckbh = (By.ID, 'GoodsWarehouseWF_Code')
    cklx_select = (By.ID, 'GoodsWarehouseWF_Type')
    psms_select = (By.ID, 'GoodsWarehouseWF_StockType')
    xsrq = (By.XPATH, '//*[@id="GoodsWarehouseWF_Tab"]/li[2]/a')
    ygrq = (By.XPATH, '//*[@id="GoodsWarehouseWF_Tab_2"]/div/div[1]/button[1]')
    ygrqxz = (By.NAME, 'GoodsWarehouseWF_DateAttr_IDS')
    ksrq = (By.NAME, 'GoodsWarehouse_DateAttr_StartDate[]')
    jzrq = (By.NAME, 'GoodsWarehouse_DateAttr_EndDate[]')
    xssj = (By.XPATH, '//*[@id="GoodsWarehouseWF_Tab"]/li[3]/a')
    ygsj = (By.XPATH, '//*[@id="GoodsWarehouseWF_Tab_3"]/div/div[1]/button[1]')
    ygsjxz = (By.NAME, 'GoodsWarehouseWF_TimeAttr_IDS')
    kssj = (By.NAME, 'GoodsWarehouse_TimeAttr_StartTime[]')
    jzsj = (By.NAME, 'GoodsWarehouse_TimeAttr_EndTime[]')
    bcnr = (By.ID, 'GoodsWarehouseWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_ckxxgl(self):
        self.find_element(*self.ckxxgl).click()

    def switch_cktj(self):
        self.switch_frame(*self.cktj_frame)

    def click_cktj(self):
        self.find_element(*self.cktj).click()

    def input_ckmc(self, ckmc1):
        self.find_element(*self.ckmc).send_keys(ckmc1)

    def input_ckbh(self, ckbh1):
        self.find_element(*self.ckbh).send_keys(ckbh1)

    def select_cklx(self, cklx1):
        self.q1 = self.find_element(*self.cklx_select)
        self.Select(self.q1).select_by_value(cklx1)

    def select_psms(self, psms1):
        self.q2 = self.find_element(*self.psms_select)
        self.Select(self.q2).select_by_value(psms1)

    def click_xsrq(self):
        self.find_element(*self.xsrq).click()

    def click_ygrq(self):
        self.find_element(*self.ygrq).click()

    def click_ygrqxz(self):
        self.find_element(*self.ygrqxz).click()

    def input_ksrq(self, ksrq1):
        self.find_element(*self.ksrq).send_keys(ksrq1)

    def input_jzrq(self, jzrq1):
        self.find_element(*self.jzrq).send_keys(jzrq1)

    def xssj_click(self):
        self.find_element(*self.xssj).click()

    def click_ygsj(self):
        self.find_element(*self.ygsj).click()

    def click_ygsjxz(self):
        self.find_element(*self.ygsjxz).click()

    def input_kssj(self, kssj1):
        self.find_element(*self.kssj).send_keys(kssj1)

    def input_jzsj(self, jzsj1):
        self.find_element(*self.jzsj).send_keys(jzsj1)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()