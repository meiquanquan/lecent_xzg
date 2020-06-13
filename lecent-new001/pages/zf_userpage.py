from .basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class UserPagezf(BasePage):
    # 1、新增罪犯功能
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    zfxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[3]/a')
    zftj_frame = (By.XPATH, '//*[@id="iframe0"]')
    zftj = (By.XPATH, '//*[@id="Prisoner_ListTable_Toolbar"]/button[1]')
    ssjq = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/a/span')
    ssjq_input = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/div/div/input')
    zfxm = (By.ID, 'PrisonerWF_Name')
    zfbh = (By.ID, 'PrisonerWF_Code')
    zfxb = (By.XPATH, '//*[@id="PrisonerWF_Sex_chosen"]/a/span')
    zfxb_input = (By.XPATH, '//*[@id="PrisonerWF_Sex_chosen"]/div/div/input')
    cydj = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/a/span')
    cydj_input = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/div/div/input')
    srlb = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/a/span')
    srlb_input = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/div/div/input')
    zflx = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/a/span')
    zflx_input = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/div/div/input')
    bcnr = (By.ID, 'PrisonerWF_SubmitButton')


    # 2、转监区功能
    zfxxglcxbhsrk_input = (By.ID, 'PrisonerSF_Keyword')
    zfxxglcx = (By.XPATH, '//*[@id="PrisonerSF"]/div[2]/button[1]')
    zfxxglgxzf = (By.XPATH, '//*[@id="Prisoner_ListTable"]/tbody/tr[1]/td[1]/label/input')
    plzjq = (By.XPATH, '//*[@id="Prisoner_ListTable_Toolbar"]/button[5]')
    gbzfxxgl = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')

    zjqzfbhsrk = (By.ID, 'PrisonAreaTransferWF_Keyword')
    xzzrjq_select = (By.NAME, 'PrisonAreaTransfer_ToPrisonAreaID[]')
    zjqxyb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[2]/a')

    ddcjsbtknr = (By.XPATH, '/html/body/div[6]/div[2]')

    # 3、罪犯转级功能
    plzcydj = (By.XPATH, '//*[@id="Prisoner_ListTable_Toolbar"]/button[6]')
    zcydjzfbhsrk = (By.ID, 'TreatLevelTransferWF_Keyword')
    xzzcydj_select = (By.NAME, 'TreatLevelTransfer_ToTreatLevelID[]')
    zcydjxyb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[2]')


    # 1、新增罪犯功能
    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_zfxxgl(self):
        self.find_element(*self.zfxxgl).click()

    def switch_zftj(self):
        self.switch_frame(*self.zftj_frame)

    def switch_outframe(self):
        self.switch_out()

    def click_zftj(self):
        self.find_element(*self.zftj).click()

    def click_ssjq(self):
        self.find_element(*self.ssjq).click()

    def input_ssjq(self, ssjq1):
        self.find_element(*self.ssjq_input).send_keys(ssjq1)
        self.find_element(*self.ssjq_input).send_keys(Keys.ENTER)

    def input_zfxm(self, zfname):
        self.find_element(*self.zfxm).send_keys(zfname)

    def input_zfbh(self, zfnumb):
        self.find_element(*self.zfbh).send_keys(zfnumb)

    def click_zfxb(self):
        self.find_element(*self.zfxb).click()

    def input_zfxbsr(self, zfxb1):
        self.find_element(*self.zfxb_input).send_keys(zfxb1)
        self.find_element(*self.zfxb_input).send_keys(Keys.ENTER)

    def click_cydj(self):
        self.find_element(*self.cydj).click()

    def input_cydj(self, cydj1):
        self.find_element(*self.cydj_input).send_keys(cydj1)
        self.find_element(*self.cydj_input).send_keys(Keys.ENTER)

    def click_srlb(self):
        self.find_element(*self.srlb).click()

    def input_srlb(self, srlb1):
        self.find_element(*self.srlb_input).send_keys(srlb1)
        self.find_element(*self.srlb_input).send_keys(Keys.ENTER)

    def click_zflx(self):
        self.find_element(*self.zflx)

    def input_zflx(self, zflx1):
        self.find_element(*self.zflx_input).send_keys(zflx1)
        self.find_element(*self.zflx_input).send_keys(Keys.ENTER)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()

    # 2、转监区功能
    def input_zfxxcxbhsrk(self, zfbh2):
        self.find_element(*self.zfxxglcxbhsrk_input).send_keys(zfbh2)

    def click_zfxxglcxan(self):
        self.find_element(*self.zfxxglcx).click()

    def click_zfxxglgx(self):
        self.find_element(*self.zfxxglgxzf).click()

    def click_zfplzjq(self):
        self.find_element(*self.plzjq).click()

    def click_gbzfxxgl(self):
        self.find_element(*self.gbzfxxgl).click()

    def input_zjqzfbhsrk(self, zfbh3):
        self.find_element(*self.zjqzfbhsrk).send_keys(zfbh3)
        self.find_element(*self.zjqzfbhsrk).send_keys(Keys.DOWN)
        self.find_element(*self.zjqzfbhsrk).send_keys(Keys.ENTER)

    def select_zrjq(self, jqmc1):
        self.q1 = self.find_element(*self.xzzrjq_select)
        self.Select(self.q1).select_by_value(jqmc1)

    def click_zfzjqxyb(self):
        self.find_element(*self.zjqxyb).click()

    def gett_ddcjsbtknr(self):
        self.c = self.find_element(*self.ddcjsbtknr).get_attribute('textContent')
        return self.c

    # 3、罪犯转级功能
    def click_zfplzcydj(self):
        self.find_element(*self.plzcydj).click()

    def input_zfzcydjbhsrk(self, zfbh4):
        self.find_element(*self.zcydjzfbhsrk).send_keys(zfbh4)
        self.find_element(*self.zcydjzfbhsrk).send_keys(Keys.DOWN)
        self.find_element(*self.zcydjzfbhsrk).send_keys(Keys.ENTER)

    def select_xzcydj(self, cydjmc1):
        self.z1 = self.find_element(*self.xzzcydj_select)
        self.Select(self.z1).select_by_visible_text(cydjmc1)

    def click_zcydjxyb(self):
        self.find_element(*self.zcydjxyb).click()



