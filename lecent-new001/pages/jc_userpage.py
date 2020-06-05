from .basepage import BasePage
from selenium.webdriver.common.by import By
value1='31'
value2='133'
class UserPage(BasePage):

    jcxxgl=(By.XPATH,'//*[@id="side-menu"]/li[2]/a')
    yhxxgl=(By.XPATH,'//*[@id="side-menu"]/li[2]/ul/li[1]/a')
    yhtj_frame=(By.XPATH,'//*[@id="iframe0"]')
    yhtj=(By.XPATH,'//*[@id="User_ListTable_Toolbar"]/button[1]')
    bm_select=(By.ID,'UserWF_DepID')
    gw_slsect=(By.ID,'UserWF_RoleID')
    yhxm=(By.ID,'UserWF_Name')
    yhbh=(By.ID,'UserWF_Code')
    dlzh=(By.ID,'UserWF_UserName')
    dlmm=(By.ID,'UserWF_Password')
    qrmm=(By.ID,'UserWF_Password2')
    bcqr=(By.ID,'UserWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_yhxxgl(self):
        self.find_element(*self.yhxxgl).click()

    def switch_yhtj(self):
        self.switch_frame(*self.yhtj_frame)

    def click_yhtj(self):
        self.find_element(*self.yhtj).click()

    def select_bm(self):
        self.a1=self.find_element(*self.bm_select)
        self.Select(self.a1).select_by_value(value1)

    def select_gw(self):
        self.a2=self.find_element(*self.gw_slsect)
        self.Select(self.a2).select_by_value(value2)

    def input_yhxm(self, name):
        self.find_element(*self.yhxm).send_keys(name)

    def input_yhbh(self, usernub):
        self.find_element(*self.yhbh).send_keys(usernub)

    def input_dlzh(self, id_nub):
        self.find_element(*self.dlzh).send_keys(id_nub)

    def input_dlmm(self, id_mm1):
        self.find_element(*self.dlmm).send_keys(id_mm1)

    def input_qrmm(self, id_mm2):
        self.find_element(*self.qrmm).send_keys(id_mm2)

    def click_submit(self):
        self.find_element(*self.bcqr).click()


