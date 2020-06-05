
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://zg.lecent.cn:9081/admin/index')

############资金业务-资金下账
zjywgl = (By.XPATH, '//*[@id="side-menu"]/li[6]/a/span[1]')
zjxz = (By.XPATH, '//*[@id="side-menu"]/li[6]/ul/li[3]/a')
zjxz_frame = (By.XPATH, '//*[@id="iframe0"]')
tjxz = (By.XPATH, '//*[@id="PrisonerMoneyOut_ListTable_Toolbar"]/button[1]')
#留意是否切frame
zjxzgb = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
tjxz_frame = (By.XPATH, '//*[@id="iframe0"]')
xzzjfl = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen"]/a/span')
xzzjfl_input = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen"]/div/div/input')
#enter
xzzjlx = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen"]/a/span')
xzzjlx_input = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen"]/div/div/input')
#enter
xzzfxm_input = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_Keyword"]')
#down
#enter
xzdqje = (By.XPATH, '//*[@id="PrisonerSelect_ListTable"]/tbody/tr[2]/td[5]')
#ctrl a
#ctrl c
xzje = (By.XPATH, '//*[@id="PrisonerMoneyOutWF_Amount_vuw3m"]')
##################供应站销售
xsywgl = (By.XPATH, '//*[@id="side-menu"]/li[4]/a/span[1]')
gyzxs = (By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li[2]/a')
gyzxs_frame = (By.XPATH, '//*[@id="iframe0"]')
zfxm_input = (By.XPATH, '//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]')
# down
#enter
cksrk = (By.XPATH, '//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/a/span')
cksrk_input = (By.XPATH, '//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/div/div/input')
#enter
spbh_input = (By.XPATH, '//*[@id="GoodsOrderSaleForm_Keyword"]')
# down
# enter
gyzxsjz = (By.XPATH, '//*[@id="GoodsOrderSaleForm_SubmitButton"]')
qrjz = (By.XPATH, '//*[@id="Modal_SaleSettyle"]')

########################################################################################################################
time.sleep(3)
driver.find_element_by_id('UserName').send_keys('528138')
time.sleep(3)
driver.find_element_by_id('Password').send_keys('123456')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="LoginForm"]/div[4]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/ul/li[2]/a').click()
time.sleep(3)
qa1 = driver.find_element_by_xpath('//*[@id="iframe0"]')
time.sleep(3)
driver.switch_to.frame(qa1)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys('设王锡')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys(Keys.DOWN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Prisoner_Keyword"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/div/div/input').send_keys('所外仓库')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_GoodsWarehouseID_chosen"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys('095')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys(Keys.DOWN)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_Keyword"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="GoodsOrderSaleForm_SubmitButton"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Modal_SaleSettyle"]').click()
time.sleep(3)
driver.switch_to.parent_frame()
time.sleep(3)
#qw1 = driver.find_element_by_xpath('/html/body/div[6]/div[2]').text()
#time.sleep(3)
#print(qw1)
driver.find_element_by_xpath('/html/body/div[6]/div[3]/a').click()
time.sleep(3)
'''
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen"]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen"]/div/div/input').send_keys('亲情电话')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_TopPrisonerMoneyTypeID_chosen"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen"]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen"]/div/div/input').send_keys('亲情电话')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="PrisonerMoneyOutWF_ChildPrisonerMoneyTypeID_chosen"]/div/div/input').send_keys(Keys.ENTER)
time.sleep(3)
'''
'''
#############
#获取所有的tr

self.tr1 = self.driver.find_elements_by_tag_name("tr")[1]  #获取第一个tr
self.td4 = self.tr1.find_elements_by_tag_name('td')[4]     #获取tr中第4个td
self.tdtextlist = [self.td4.text]                          #读取指定td中的文本内容
self.newtdtextlist = [float(re.sub("[^0-9.\-]", "", x)) for x in self.tdtextlist]  #读取内容为带单位的数量时遍历文本仅获取数据
print(self.newtdtextlist[0])
'''
'''
#########
trlist=driver.find_elements_by_tag_name("tr") #获取所有tr
for tr in trlist:
    #获取tr中的所有td
    tdlist=tr.find_elements_by_tag_name("td")
    if len(tdlist)>0:
        #获取td[4]的文本
        text=tr.find_elements_by_tag_name("td")[4].text
        #当td[0]的内容为小李时，获取当前tr的id属性
        print(text)

driver.quit()

########################
text1 = '12.6元'
import re
myList = [text1]

newlist = [float(re.sub("[^0-9.\-]","",x)) for x in myList]

print(newlist[0])
'''
