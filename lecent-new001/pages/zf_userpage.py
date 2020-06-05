from .basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class UserPagezf(BasePage):
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    zfxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[3]/a')
    zftj_frame = (By.XPATH, '//*[@id="iframe0"]')
    zftj = (By.XPATH, '//*[@id="Prisoner_ListTable_Toolbar"]/button[1]')
    ssjq = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/a/span')
    ssjq_input = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/div/div/input')
    zfxm = (By.ID, 'PrisonerWF_Name')
    zfbh = (By.ID, 'PrisonerWF_Code')
    zfxb_select = (By.ID, 'PrisonerWF_Sex')
    cydj = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/a/span')
    cydj_input = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/div/div/input')
    srlb = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/a/span')
    srlb_input = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/div/div/input')
    zflx = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/a/span')
    zflx_input = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/div/div/input')
    bcnr = (By.ID, 'PrisonerWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_zfxxgl(self):
        self.find_element(*self.zfxxgl).click()

    def switch_zftj(self):
        self.switch_frame(*self.zftj_frame)

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

    def select_zfxb(self, zfxb1):
        self.a2 = self.find_element(*self.zfxb_select)
        self.Select(self.a2).select_by_value(zfxb1)

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



