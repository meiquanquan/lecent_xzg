from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class JqxxPage(BasePage):
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    jqxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[2]/a')
    jqtj_frame = (By.XPATH, '//*[@id="iframe0"]')
    jqtj = (By.XPATH, '//*[@id="PrisonArea_ListTable_Toolbar"]/a[1]')
    sjjq = (By.XPATH, '//*[@id="PrisonAreaWF_UpPrisonAreaID_chosen"]/a/span')
    sjjq_input = (By.XPATH, '//*[@id="PrisonAreaWF_UpPrisonAreaID_chosen"]/div/div/input')
    zflx = (By.XPATH, '//*[@id="PrisonAreaWF_Tab_1"]/div[2]/div/div/button/div/div/div')
    zflxqx = (By.XPATH, '//*[@id="PrisonAreaWF_Tab_1"]/div[2]/div/div/div/div[2]/div/button[1]')
    jqmc = (By.ID, 'PrisonAreaWF_Name')
    jqbh = (By.ID, 'PrisonAreaWF_Code')
    xsrq = (By.XPATH, '//*[@id="PrisonAreaWF_Tab"]/li[2]/a')
    ygrq = (By.XPATH, '//*[@id="PrisonAreaWF_Tab_2"]/div/div[1]/button[1]')
    ygrqxz = (By.NAME, 'PrisonAreaWF_SaleDateAttr_IDS')
    ksrq = (By.NAME, 'PrisonArea_SaleDateAttr_StartDate[]')
    jzrq = (By.NAME, 'PrisonArea_SaleDateAttr_EndDate[]')
    xssj = (By.XPATH, '//*[@id="PrisonAreaWF_Tab"]/li[3]/a')
    ygsj = (By.XPATH, '//*[@id="PrisonAreaWF_Tab_3"]/div/div[1]/button[1]')
    ygsjxz = (By.NAME, 'PrisonAreaWF_SaleTimeAttr_IDS')
    kssjxz = (By.NAME, 'PrisonArea_SaleTimeAttr_StartTime[]')
    kssjqr = (By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div/span[3]')
    jzsjxz = (By.NAME, 'PrisonArea_SaleTimeAttr_EndTime[]')
    jzsj23 = (By.XPATH, '//*[@id="layui-laydate2"]/div[1]/div[2]/ul/li[1]/ol/li[24]')
    jzsjqr = (By.XPATH, '//*[@id="layui-laydate2"]/div[2]/div/span[3]')
    bcnr = (By.ID, 'PrisonAreaWF_SubmitButton')

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_jqxxgl(self):
        self.find_element(*self.jqxxgl).click()

    def switch_jqtj(self):
        self.switch_frame(*self.jqtj_frame)

    def click_jqtj(self):
        self.find_element(*self.jqtj).click()

    def click_sjjq(self):
        self.find_element(*self.sjjq).click()

    def input_sjjq(self, sjjq1):
        self.find_element(*self.sjjq_input).send_keys(sjjq1)
        self.find_element(*self.sjjq_input).send_keys(Keys.ENTER)

    def click_zflx(self):
        self.find_element(*self.zflx).click()

    def click_zflxqx(self):
        self.find_element(*self.zflxqx).click()


    def input_jqmc(self, jqname):
        self.find_element(*self.jqmc).send_keys(jqname)

    def input_jqbh(self, jqnumber):
        self.find_element(*self.jqbh).send_keys(jqnumber)

    def click_xsrq(self):
        self.find_element(*self.xsrq).click()

    def click_ygrq(self):
        self.find_element(*self.ygrq).click()

    def click_ygrqxz(self):
        self.find_element(*self.ygrqxz).click()

    def input_ksrq(self, ksrqnumber):
        self.find_element(*self.ksrq).send_keys(ksrqnumber)

    def input_jzrq(self, jzrqnumber):
        self.find_element(*self.jzrq).send_keys(jzrqnumber)

    def click_xssj(self):
        self.find_element(*self.xssj).click()

    def click_ygsj(self):
        self.find_element(*self.ygsj).click()

    def click_ygsjxz(self):
        self.find_element(*self.ygsjxz).click()

    def input_kssj(self, kssjnumb):
        self.find_element(*self.kssjxz).send_keys(kssjnumb)

    def input_jzsj(self, jzsjnumb):
        self.find_element(*self.jzsjxz).send_keys(jzsjnumb)

    def click_bcnr(self):
        self.find_element(*self.bcnr).click()