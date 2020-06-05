from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SpxxxhggPage(BasePage):
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    spxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[9]/a')
    spxx_frame = (By.XPATH, '//*[@id="iframe0"]')
    spgg = (By.XPATH, '/html/body/div[1]/div[1]/div/ul/li[4]/a[1]')
    spggtj = (By.XPATH, '//*[@id="GoodsSpec_ListTable_Toolbar"]/a[1]')
    spggmc = (By.ID, 'GoodsSpecWF_Name')
    spggbc = (By.ID, 'GoodsSpecWF_SubmitButton')
    spxh = (By.XPATH, '/html/body/div/div[1]/div/ul/li[5]/a[1]')
    spxhtj = (By.XPATH, '//*[@id="GoodsType_ListTable_Toolbar"]/a[1]')
    spxhmc = (By.ID, 'GoodsTypeWF_Name')
    spxhbc = (By.ID, 'GoodsTypeWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_spxxgl(self):
        self.find_element(*self.spxxgl).click()

    def switch_spxx(self):
        self.switch_frame(*self.spxx_frame)

    def click_spgg(self):
        self.find_element(*self.spgg).click()

    def click_spggtj(self):
        self.find_element(*self.spggtj).click()

    def input_spggmc(self, spggmc1):
        self.find_element(*self.spggmc).send_keys(spggmc1)

    def click_spggbc(self):
        self.find_element(*self.spggbc).click()

    def click_spxh(self):
        self.find_element(*self.spxh).click()

    def click_spxhtj(self):
        self.find_element(*self.spxhtj).click()

    def input_spxhmc(self, spxhmc1):
        self.find_element(*self.spxhmc).send_keys(spxhmc1)

    def click_spxhbc(self):
        self.find_element(*self.spxhbc).click()