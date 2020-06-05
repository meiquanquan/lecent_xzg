from .basepage import BasePage
from selenium.webdriver.common.by import By

class CydjPage(BasePage):

    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    zfzjgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[6]/a')
    djsz_frame = (By.XPATH, '//*[@id="iframe0"]')
    djsz = (By.XPATH, '/html/body/div/div[1]/div/ul/li[2]/a[1]')
    djtj = (By.XPATH, '//*[@id="TreatLevel_ListTable_Toolbar"]/button[1]')
    djmc = (By.ID, 'TreatLevelWF_Name')
    djbh = (By.ID, 'TreatLevelWF_Code')
    bcnr = (By.ID, 'TreatLevelWF_SubmitButton')

    def click_jqxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_zfzjgl(self):
        self.find_element(*self.zfzjgl).click()

    def swatch_djsz(self):
        self.switch_frame(*self.djsz_frame)

    def click_djsz(self):
        self.find_element(*self.djsz).click()

    def click_djtj(self):
        self.find_element(*self.djtj).click()

    def input_djmc(self, djmcname):
        self.find_element(*self.djmc).send_keys(djmcname)

    def input_djbh(self, djbhnumb):
        self.find_element(*self.djbh).send_keys(djbhnumb)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()
