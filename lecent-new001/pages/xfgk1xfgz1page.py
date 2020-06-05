from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Xfgk1xfgzPage(BasePage):

    zfxfgk = (By.XPATH, '//*[@id="side-menu"]/li[10]/a/span[1]')
    xfgz = (By.XPATH, '//*[@id="side-menu"]/li[10]/ul/li[3]/a')
    xfgz_frame = (By.XPATH, '//*[@id="iframe0"]')
    xfgztj = (By.XPATH, '//*[@id="ControlGoods_ListTable_Toolbar"]/a[1]')
    #切
    xfgzgb = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
    #切
    xfgzmc_input = (By.ID, 'ControlGoodsWF_Name')
    xfgzyxj_select = (By.ID, 'ControlGoodsWF_Level')
    xfgzdyyx = (By.XPATH, '//*[@id="ControlGoodsWF_ValidDateTypeBtn1"]')
    xfgztdzf = (By.XPATH, '//*[@id="ControlGoodsWF_LPTypeBtn3"]/label')
    xzzf = (By.XPATH, '//*[@id="LPContent"]/div[1]/div/div/button')
    zfbhsrk_input = (By.ID, 'ControlGoodsAddPrisonerWF_PrisonerKW')
    cxzfan = (By.XPATH, '//*[@id="ControlGoodsAddPrisonerWF"]/div[1]/div/div/span/button')
    zfxzgx = (By.XPATH, '//*[@id="ControlGoodsAddPrisonerWF_ListTable"]/tbody/tr[2]/td[7]/button')
    zfxzgb = (By.XPATH, '/html/body/div[2]/span[1]/a[3]')

    # 特定商品
    tdsp = (By.ID, 'ControlGoodsWF_LGTypeBtn3')
    ##
    xzan = (By.XPATH, '//*[@id="LGContent"]/div[1]/div/div/button')
    xzsp_input = (By.ID, 'ControlGoodsAddGoodsWF_GoodsKW')
    xzspgx = (By.XPATH, '//*[@id="ControlGoodsAddGoodsWF_ListTable"]/tbody/tr[2]/td[6]/button')
    cxspan = (By.XPATH, '//*[@id="ControlGoodsAddGoodsWF"]/div[1]/div/div/span/button')
    xzspgb = (By.XPATH, '/html/body/div[3]/span[1]/a[3]')

    # 特定类别
    tdlb = (By.ID, 'ControlGoodsWF_LGTypeBtn2')
    ##
    qbxz = (By.XPATH, '//*[@id="ControlGoodsAddGoodsCategoryWF"]/div[1]/div[1]/button[1]')
    qran = (By.XPATH, '//*[@id="ControlGoodsWF_GoodsCategory_SubmitButton"]')


    # 限制
    xfgzxzgw = (By.ID, 'ControlGoodsWF_TypeBtn1')
    # 禁止
    xfgzjzgw = (By.ID, 'ControlGoodsWF_TypeBtn2')
    # 特许
    xfgztxgw = (By.ID, 'ControlGoodsWF_TypeBtn3')
    # 只能
    xfgzzngw = (By.ID, 'ControlGoodsWF_TypeBtn4')

    xfgzbxzje = (By.ID, 'ControlGoodsWF_Amount_IsLimit1')

    xfgzxzje = (By.ID, 'ControlGoodsWF_Amount_IsLimit2')
    srxzje_input = (By.XPATH, '//*[@id="ControlGoodsWF_Amount"]')

    xfgzbxzsl = (By.ID, 'ControlGoodsWF_Quantity_IsLimit1')

    xfgzxzsl = (By.ID, 'ControlGoodsWF_Quantity_IsLimit2')
    srxzsl_input = (By.XPATH, '//*[@id="ControlGoodsWF_Quantity"]')



    xfgzbc = (By.ID, 'ControlGoodsWF_SubmitButton')

    def click_zfxfgk(self):
        self.find_element(*self.zfxfgk).click()

    def click_xfgz(self):
        self.find_element(*self.xfgz).click()

    def switch_xfgz(self):
        self.switch_frame(*self.xfgz_frame)

    def click_xfgztj(self):
        self.find_element(*self.xfgztj).click()

    def switch_outframe(self):
        self.switch_out()

    def click_xfgzgb(self):
        self.find_element(*self.xfgzgb).click()

    def input_xfgzmc(self, xfgzmc1):
        self.find_element(*self.xfgzmc_input).send_keys(xfgzmc1)

    def slelct_xfgzyxj(self, q1):
        self.y1 = self.find_element(*self.xfgzyxj_select)
        self.Select(self.y1).select_by_value(q1)

    def click_xfgzdyyx(self):
        self.find_element(*self.xfgzdyyx).click()

    def click_xfgztdzf(self):
        self.find_element(*self.xfgztdzf).click()

    def click_xzzf(self):
        self.find_element(*self.xzzf).click()

    def input_xzzfbh(self, zfbh1):
        self.find_element(*self.zfbhsrk_input).send_keys(zfbh1)

    def click_cxzfan(self):
        self.find_element(*self.cxzfan).click()

    def click_zfxzgx(self):
        self.find_element(*self.zfxzgx).click()

    def click_zfzxzgb(self):
        self.find_element(*self.zfxzgb).click()
    # 特定商品
    def click_tdsp(self):
        self.find_element(*self.tdsp).click()

    def click_spxz(self):
        self.find_element(*self.xzan).click()

    def input_spbhsr(self, xzsp1):
        self.find_element(*self.xzsp_input).send_keys(xzsp1)

    def click_cxspan(self):
        self.find_element(*self.cxspan).click()

    def click_xzspgx(self):
        self.find_element(*self.xzspgx).click()

    def click_xzspgb(self):
        self.find_element(*self.xzspgb).click()

    # 特定类别
    def click_tdlb(self):
        self.find_element(*self.tdlb).click()

    def click_lbxz(self):
        self.find_element(*self.xzan).click()

    def click_qbxz(self):
        self.find_element(*self.qbxz).click()

    def click_qrlb(self):
        self.find_element(*self.qran).click()

    ###
    # 限制
    def click_xfgzxzgw(self):
        self.find_element(*self.xfgzxzgw).click()

    # 禁止
    def click_xfgzjzgw(self):
        self.find_element(*self.xfgzjzgw).click()

    # 特许
    def click_xfgztxgw(self):
        self.find_element(*self.xfgztxgw).click()

    #只能
    def click_xfgzzngm(self):
        self.find_element(*self.xfgzzngw).click()
    ###

    # 金额
    def click_xfgzbxzje(self):
        self.find_element(*self.xfgzbxzje).click()

    def click_xzgzxzje(self):
        self.find_element(*self.xfgzxzje).click()

    def input_xfgzxzje(self, xzje1):
        self.find_element(*self.srxzje_input).send_keys(xzje1)

    # 数量
    def click_xfgzbxzsl(self):
        self.find_element(*self.xfgzbxzsl).click()

    def click_xfgzxzsl(self):
        self.find_element(*self.xfgzxzsl).click()

    def input_xfgzxzsl(self, xzsl1):
        self.find_element(*self.srxzsl_input).send_keys(xzsl1)

    def click_xfgzbc(self):
        self.find_element(*self.xfgzbc).click()