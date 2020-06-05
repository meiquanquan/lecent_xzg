#创建最基类
class BasePage:
    #重写构造方法，在创建对象时传入浏览器对象driver
    def __init__(self,driver,Select):
        self.driver=driver
        self.Select=Select
    #封装元素查找方法，*loc表示传入的元素为元祖
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    #封装返回页面标题方法
    def get_title(self):
        return self.driver.title
    #封装返回页面URL方法
    def get_url(self):
        return self.driver.current_url
    #封装截图方法
    def get_img(self,path):
        self.driver.get_screenshot_as_file(path)
    #封装iframe框架切换方法
    def switch_frame(self,*g):
        s=self.driver.find_element(*g)
        self.driver.switch_to.frame(s)

    #封装iframe框架切换至最外层框架
    def switch_out(self):
        self.driver.switch_to.default_content()

    #封装返回一组元素的方法
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
