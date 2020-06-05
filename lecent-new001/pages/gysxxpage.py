from .basepage import BasePage
from selenium.webdriver.common.by import By
import time
class GysxxPage(BasePage):
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    gysxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[11]/a')
    gysxxgl_frame = (By.XPATH, '//*[@id="iframe0"]')
    gystj = (By.XPATH, '//*[@id="GoodsSupplier_ListTable_Toolbar"]/a[1]')
    gysmc = (By.ID, 'GoodsSupplierWF_Name')
    gysbh = (By.ID, 'GoodsSupplierWF_Code')
    gyslx_select = (By.ID, 'GoodsSupplierWF_Type')
    gysbc = (By.ID, 'GoodsSupplierWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_gysxxgl(self):
        self.find_element(*self.gysxxgl).click()

    def switch_gysxxgl(self):
        self.switch_frame(*self.gysxxgl_frame)

    def click_gystj(self):
        self.find_element(*self.gystj).click()

    def input_gysmc(self, gysmc1):
        self.find_element(*self.gysmc).send_keys(gysmc1)

    def input_gysbh(self, gysbh1):
        self.find_element(*self.gysbh).send_keys(gysbh1)

    def select_gyslx(self, gyslx1):
        self.g =self.find_element(*self.gyslx_select)
        self.Select(self.g).select_by_value(gyslx1)


    def click_gysbc(self):
        self.find_element(*self.gysbc).click()