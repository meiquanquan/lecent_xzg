from .basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class ZjlxPage(BasePage):
    zjywgl = (By.XPATH, '//*[@id="side-menu"]/li[6]/a/span[1]')
    zjlx = (By.XPATH, '//*[@id="side-menu"]/li[6]/ul/li[1]/a')
    zjlxtj_frame = (By.XPATH, '//*[@id="iframe0"]')
    zjlxtj = (By.XPATH, '//*[@id="PrisonerMoneyType_ListTable_Toolbar"]/button[1]')
    sjzjlx = (By.XPATH, '//*[@id="PrisonerMoneyTypeWF_UpTypeID_chosen"]/a/span')
    sjzjlxmc_input = (By.XPATH, '//*[@id="PrisonerMoneyTypeWF_UpTypeID_chosen"]/div/div/input')
    zjlxmc = (By.ID, 'PrisonerMoneyTypeWF_Name')
    zjlxbh = (By.ID, 'PrisonerMoneyTypeWF_Code')
    sxzlx_select = (By.ID, 'PrisonerMoneyTypeWF_Type')
    sfgk_select = (By.ID, 'PrisonerMoneyTypeWF_IsControl')
    sfjrxftj_select = (By.ID, 'PrisonerMoneyTypeWF_IsConsumptionStatistics')
    sfkycz_select = (By.ID, 'PrisonerMoneyTypeWF_IsReverse')
    Azhbl = (By.ID, 'PrisonerMoneyTypeWF_AccountA')
    Bzhbl = (By.ID, 'PrisonerMoneyTypeWF_AccountB')
    Czhbl = (By.ID, 'PrisonerMoneyTypeWF_AccountC')
    bcnr = (By.ID, 'PrisonerMoneyTypeWF_SubmitButton')

    def click_zjywgl(self):
        self.find_element(*self.zjywgl).click()

    def click_zjlx(self):
        self.find_element(*self.zjlx).click()

    def switch_zjlxtj(self):
        self.switch_frame(*self.zjlxtj_frame)

    def click_zjlxtj(self):
        self.find_element(*self.zjlxtj).click()

    def click_sjzjlx(self):
        self.find_element(*self.sjzjlx).click()

    def input_sjzjlxmc(self, sjzjlxmc1):
        self.find_element(*self.sjzjlxmc_input).send_keys(sjzjlxmc1)
        self.find_element(*self.sjzjlxmc_input).send_keys(Keys.ENTER)

    def input_zjlxmc(self, zjlxmc1):
        self.find_element(*self.zjlxmc).send_keys(zjlxmc1)

    def input_zjlxbh(self, zjlxbh1):
        self.find_element(*self.zjlxbh).send_keys(zjlxbh1)

    def select_sxzlx(self, sxzlx1):
        self.w1 = self.find_element(*self.sxzlx_select)
        self.Select(self.w1).select_by_value(sxzlx1)

    def select_sfgk(self, sfgk1):
        self.w2 = self.find_element(*self.sfgk_select)
        self.Select(self.w2).select_by_value(sfgk1)

    def select_sfjrxftj(self, sfjrxftj1):
        self.w3 = self.find_element(*self.sfjrxftj_select)
        self.Select(self.w3).select_by_value(sfjrxftj1)

    def select_sfkycz(self, sfkycz1):
        self.w4 = self.find_element(*self.sfkycz_select)
        self.Select(self.w4).select_by_value(sfkycz1)

    def input_A(self, aa1):
        self.find_element(*self.Azhbl).send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        self.find_element(*self.Azhbl).send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        self.find_element(*self.Azhbl).send_keys(aa1)

    def input_B(self, bb1):
        self.find_element(*self.Bzhbl).send_keys(bb1)

    def input_C(self, cc1):
        self.find_element(*self.Czhbl).send_keys(cc1)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()
