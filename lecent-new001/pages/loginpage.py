#登录页
from .basepage import BasePage
from selenium.webdriver.common.by import By    #导入selenium自带的元素方法by
class LoginPage(BasePage):     #封装页面登录类
    #定位器
    user=(By.ID,'UserName')   #用户名
    password=(By.ID,'Password')   #密码
    button=(By.XPATH,'//*[@id="LoginForm"]/div[4]/button')    #登录按钮


    #封装元素操作方法
    #输入用户名
    def input_name(self,name):
        self.find_element(*self.user).send_keys(name)
    #输入密码
    def input_pwd(self,pwd):
        self.find_element(*self.password).send_keys(pwd)
    #点击登录按钮
    def click_login(self):
        self.find_element(*self.button).click()


