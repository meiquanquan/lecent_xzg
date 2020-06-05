from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Xfgk1xfedPage(BasePage):

    #消费额度规则设置页面
    zfxfgk = (By.XPATH, '//*[@id="side-menu"]/li[10]/a/span[1]')
    xfed = (By.XPATH, '//*[@id="side-menu"]/li[10]/ul/li[2]/a')
    xfed_frame = (By.XPATH, '//*[@id="iframe0"]')
    xfedtj = (By.XPATH, '//*[@id="ControlAmount_ListTable_Toolbar"]/a[1]')
    #切out
    xfedgb = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
    #切
    xfedgzmc_input = (By.ID, 'ControlAmountForm_Name')
    xfedyxj_select = (By.ID, 'ControlAmountForm_Level')
    xfeddyyx = (By.XPATH, '//*[@id="ControlAmountForm_ValidTypeBtn1"]/label')
    xfedtdzf = (By.ID, 'ControlAmountForm_LPTypeBtn3')
    xfedxzzf = (By.ID, 'ControlAmountForm_ChoosePrisonerButton')
    zf_input = (By.ID,'ControlAmountAddPrisonerWF_PrisonerKW')
    zfcx = (By.XPATH, '//*[@id="ControlAmountAddPrisonerWF"]/div[1]/div/div/span/button/li')
    zfgx = (By.XPATH, '//*[@id="ControlAmountAddPrisonerWF_ListTable"]/tbody/tr[2]/td[7]/button/li')
    zfxzgb = (By.XPATH, '//*[@id="layui-layer1"]/span[1]/a[3]')
    #消费额度限制
    xfedxz = (By.ID, 'ControlAmountForm_LATypeBtn1')
    #消费额度上浮
    xfedsf = (By.ID, 'ControlAmountForm_LATypeBtn2')
    #消费额度下调
    xfedxt = (By.ID, 'ControlAmountForm_LATypeBtn3')

    xfedzebsz = (By.XPATH, '//*[@id="ControlAmountForm_AmountTotal_IsLimit1"]')
    xfedzesz = (By.XPATH, '//*[@id="ControlAmountForm_AmountTotal_IsLimit2"]')
    xfedze_input = (By.ID, 'ControlAmountForm_AmountTotal')

    xfedabsz = (By.XPATH, '//*[@id="ControlAmountForm_AmountA_IsLimit1"]')
    xfedasz = (By.XPATH, '//*[@id="ControlAmountForm_AmountA_IsLimit2"]')
    xfeda_input = (By.ID, 'ControlAmountForm_AmountA')

    xfedbbsz = (By.XPATH, '//*[@id="ControlAmountForm_AmountB_IsLimit1"]')
    xfedbsz = (By.XPATH, '//*[@id="ControlAmountForm_AmountB_IsLimit1"]')
    xfedb_input = (By.ID, 'ControlAmountForm_AmountB')

    xfedcsbsz = (By.XPATH, '//*[@id="ControlAmountForm_ShoppingCount_IsLimit1"]')
    xfedcssz = (By.XPATH, '//*[@id="ControlAmountForm_ShoppingCount_IsLimit2"]')
    xfedcs_input = (By.ID, 'ControlAmountForm_ShoppingCount')

    xfedbc = (By.ID, 'ControlAmountForm_SubmitButton')

    def click_zfxfgk(self):
        self.find_element(*self.zfxfgk).click()

    def click_xfed(self):
        self.find_element(*self.xfed).click()

    def switch_xfed(self):
        self.switch_frame(*self.xfed_frame)

    def click_xfedtj(self):
        self.find_element(*self.xfedtj).click()

    def switch_outframe(self):
        self.switch_out()

    def click_xfedgb(self):
        self.find_element(*self.xfedgb).click()

    def input_xfedgzmc(self, gzmc1):
        self.find_element(*self.xfedgzmc_input).send_keys(gzmc1)

    def select_xfedyxj(self, value1):
        self.f1 = self.find_element(*self.xfedyxj_select)
        self.Select(self.f1).select_by_value(value1)

    def click_xfeddyyx(self):
        self.find_element(*self.xfeddyyx).click()

    def click_xfedtdzf(self):
        self.find_element(*self.xfedtdzf).click()

    def click_xfedxzzf(self):
        self.find_element(*self.xfedxzzf).click()

    def input_zfmc(self, zfmc1):
        self.find_element(*self.zf_input).send_keys(zfmc1)

    def click_zfcx(self):
        self.find_element(*self.zfcx).click()

    def click_zfgx(self):
        self.find_element(*self.zfgx).click()

    def click_zfxzgb(self):
        self.find_element(*self.zfxzgb).click()

    #限制
    def click_xfedxz(self):
        self.find_element(*self.xfedxz).click()
    #上浮
    def click_xfedsf(self):
        self.find_element(*self.xfedsf).click()
    #下调
    def click_xfedxt(self):
        self.find_element(*self.xfedxt).click()
    #总额
    def click_xfedzebsz(self):
        self.find_element(*self.xfedzebsz).click()
    def ckicl_xfedzesz(self):
        self.find_element(*self.xfedzesz).click()
    def input_xfedze(self, ze1):
        self.find_element(*self.xfedze_input).send_keys(ze1)
    #A账户
    def click_xfedabsz(self):
        self.find_element(*self.xfedabsz).click()
    def click_xfedasz(self):
        self.find_element(*self.xfedasz).click()
    def input_xfeda(self, a1):
        self.find_element(*self.xfeda_input).send_keys(a1)
    #B账户
    def click_xfedbbsz(self):
        self.find_element(*self.xfedbbsz).click()
    def click_xfedsz(self):
        self.find_element(*self.xfedbsz).click()
    def input_xfedb(self, b1):
        self.find_element(*self.xfedb_input).send_keys(b1)
    #购物次数
    def click_gwcsbsz(self):
        self.find_element(*self.xfedcsbsz).click()
    def click_gwcssz(self):
        self.find_element(*self.xfedcssz).click()
    def input_gwcs(self):
        self.find_element(*self.xfedcs_input).send_keys()

    def click_xfedbc(self):
        self.find_element(*self.xfedbc).click()