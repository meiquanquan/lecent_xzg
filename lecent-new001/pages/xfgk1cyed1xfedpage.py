from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Cyed1xfedPage(BasePage):

    #1、初始化创建罪犯
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    zfxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[3]/a')
    zftj_frame = (By.XPATH, '//*[@id="iframe0"]')
    zftj = (By.XPATH, '//*[@id="Prisoner_ListTable_Toolbar"]/button[1]')
    ssjq = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/a/span')
    ssjq_input = (By.XPATH, '//*[@id="PrisonerWF_PrisonAreaID_chosen"]/div/div/input')
    zfxm = (By.ID, 'PrisonerWF_Name')
    zfbh = (By.ID, 'PrisonerWF_Code')
    zfxb = (By.XPATH, '//*[@id="PrisonerWF_Sex_chosen"]/a/span')
    zfxb_input = (By.XPATH, '//*[@id="PrisonerWF_Sex_chosen"]/div/div/input')
    cydj = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/a/span')
    cydj_input = (By.XPATH, '//*[@id="PrisonerWF_TreatLevelID_chosen"]/div/div/input')
    srlb = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/a/span')
    srlb_input = (By.XPATH, '//*[@id="PrisonerWF_DetainTypeID_chosen"]/div/div/input')
    zflx = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/a/span')
    zflx_input = (By.XPATH, '//*[@id="PrisonerWF_Kind_chosen"]/div/div/input')
    bcnr = (By.ID, 'PrisonerWF_SubmitButton')

    #2、初始化罪犯资金下账(监狱配置-下账自动提交)
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
    xzje = (By.XPATH, '//*[@id="PrisonerSelect_ListTable"]/tbody/tr[1]/td[5]/div[1]/input[1]')
    #ctrl v
    xzxyb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[2]/a')
    #click two
    xzgb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[3]/a')

    #3、初始化罪犯资金上账(切、监狱配置-上账手动提交)
    zjywgl = (By.XPATH, '//*[@id="side-menu"]/li[6]/a/span[1]')
    zjsz = (By.XPATH, '//*[@id="side-menu"]/li[6]/ul/li[2]/a')
    zjsz_frame = (By.XPATH, '//*[@id="iframe0"]')
    xzsz = (By.XPATH, '//*[@id="PrisonerMoneyIn_ListTable_Toolbar"]/button[1]')
    zjszgb = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
    # 留意是否切frame
    szzjfl = (By.XPATH, '//*[@id="PrisonerMoneyInWF_TopPrisonerMoneyTypeID_chosen"]/a/span')
    szzjfl_input = (By.XPATH, '//*[@id="PrisonerMoneyInWF_TopPrisonerMoneyTypeID_chosen"]/div/div/input')
    # enter
    szzjlx = (By.XPATH, '//*[@id="PrisonerMoneyInWF_ChildPrisonerMoneyTypeID_chosen"]/a/span')
    szzjlx_input = (By.XPATH, '//*[@id="PrisonerMoneyInWF_ChildPrisonerMoneyTypeID_chosen"]/div/div/input')
    # enter
    szzfxm_input = (By.XPATH, '//*[@id="PrisonerMoneyInWF_Keyword"]')
    # down
    # enter
    #szje_input = (By.XPATH, '//*[@id="PrisonerMoneyInVueApp"]/div[4]/div/div[1]/table/tbody/tr[2]/td[7]/div/input')
    szje_input = (By.XPATH, '//*[@id="PrisonerMoneyInWF_AllAmountInput"]')
    qbsz = (By.ID, 'PrisonerMoneyInWF_AllAmountInputButton')
    szxyb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[2]/a')
    # click two
    szgb = (By.XPATH, '//*[@id="wizard"]/div[3]/ul/li[3]/a')
    #提交上账
    tjsz = (By.XPATH, '//*[@id="PrisonerMoneyIn_ListTable"]/tbody/tr/td[10]/a[2]')
    qrsz = (By.XPATH, '/html/body/div[3]/div[7]/button[2]')

    #4、初始化修改关联处遇额度(切)
    zfxfgk = (By.XPATH, '//*[@id="side-menu"]/li[10]/a/span[1]')
    cyed = (By.XPATH, '//*[@id="side-menu"]/li[10]/ul/li[1]/a')
    cyed_frame = (By.XPATH, '//*[@id="iframe0"]')
    '''对应处遇额度'''
    # 【一级处遇等级{高}】
    ze1_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_NoLimit127"]')
    ze1_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_Limit127"]')
    ze1_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_Input127"]')
    ze1bxz = (By.XPATH, '//*[@id="ControlTreatLevel_ListTable"]/tbody/tr[9]/td[2]/div/a[1]')

    a1_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_NoLimit127"]')
    a1_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_Limit127"]')
    a1_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_Input127"]')
    a1bxz = (By.XPATH, '//*[@id="ControlTreatLevel_ListTable"]/tbody/tr[9]/td[3]/div/a[1]')

    b1_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_NoLimit127"]')
    b1_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_Limit127"]')
    b1_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_Input127"]')
    b1bxz = (By.XPATH, '//*[@id="ControlTreatLevel_ListTable"]/tbody/tr[9]/td[4]/div/a[1]')

    gwcs1_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_NoLimit127"]')
    gwcs1_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_Limit127"]')
    gwcs1_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_Input127"]')
    gwcs1bxz = (By.XPATH, '//*[@id="ControlTreatLevel_ListTable"]/tbody/tr[9]/td[5]/div/a[1]')
    #【二级处遇等级{底}】
    ze2_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_NoLimit128"]')
    ze2_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_Limit128"]')
    ze2_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountTotal_Input128"]')

    a2_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_NoLimit128"]')
    a2_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_Limit128"]')
    a2_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountA_Input128"]')

    b2_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_NoLimit128"]')
    b2_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_Limit128"]')
    b2_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_AmountB_Input128"]')

    gwcs2_bxz = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_NoLimit128"]')
    gwcs2_xz = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_Limit128"]')
    gwcs2_input = (By.XPATH, '//*[@id="ControlTreatLevelSF_ShoppingCount_Input128"]')

    cyedbc = (By.XPATH, '//*[@id="ControlTreatLevelDiv"]/div/button')

    #5、初始化指定商品类型改价(切)【===修改商品信息处价格无效===】
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a/span[1]')
    spxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[8]/a')
    spbhsrk_frame = (By.XPATH, '//*[@id="iframe0"]')
    spbhsrk_input = (By.XPATH, '//*[@id="GoodsSF_Keyword"]')
    #enter
    spxxxg = (By.XPATH, '//*[@id="Goods_ListTable"]/tbody/tr[1]/td[13]/a[2]')
    spsxgl = (By.XPATH, '//*[@id="GoodsWF_Tab"]/li[2]/a')
    splsjg = (By.XPATH, '//*[@id="GoodsWF_GoodsAttr_ListTable"]/tbody/tr[2]/td[6]/input')
    spbcnr = (By.XPATH, '//*[@id="GoodsWF_SubmitButton"]')

    #############在售商品管理处进行修改##############################
    #仓库设置
    jcxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/a')
    ckxxgl = (By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li[10]/a')
    ckxxgl_frame = (By.XPATH, '//*[@id="iframe0"]')
    ck1zcck = (By.XPATH, '//*[@id="GoodsWarehouse_ListTable"]/tbody/tr[2]/td[14]/a[4]')
    ck2zcck = (By.XPATH, '//*[@id="GoodsWarehouse_ListTable"]/tbody/tr[1]/td[14]/a[4]')
    tkqr = (By.XPATH, '/html/body/div[3]/div[7]/button[2]')
    #在售商品一键调价
    xsywgl = (By.XPATH, '//*[@id="side-menu"]/li[4]/a/span[1]')
    zsspgl = (By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li[1]/a')
    zsspgl_frame = (By.XPATH, '//*[@id="iframe0"]')
    spyjtj = (By.XPATH, '//*[@id="GoodsSaleSetting_ListTable_Toolbar"]/a[4]')
    zsspgb = (By.XPATH, '//*[@id="page-wrapper"]/div[1]/nav/div/a[2]/i')
    xxsj_input = (By.ID, 'AllSellingPriceSyn')
    xsjtb = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm"]/div/div[1]/div[4]/button')
    xzsp = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm"]/div/div[3]/div/button[1]')
    spbhsrk_input = (By.ID, 'GoodsSaleSettingBatchChangePriceWF_KeyWord')
    spcx = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceWF"]/div[1]/div[4]/div/span/button[1]')
    xzspgx = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceWF"]/div[1]/div[4]/div/span/button[2]')

    #商品一价格输入
    sp1xls = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm_ListTable"]/tbody/tr[2]/td[9]/div/input')
    # 商品二价格输入
    sp2xls = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm_ListTable"]/tbody/tr[4]/td[9]/div/input')
    # 商品三价格输入
    sp3xls = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm_ListTable"]/tbody/tr[6]/td[9]/div/input')
    # 商品四价格输入
    sp4xls = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm_ListTable"]/tbody/tr[8]/td[9]/div/input')
    # 商品五价格输入
    sp5xls = (By.XPATH, '//*[@id="GoodsSaleSettingBatchChangePriceForm_ListTable"]/tbody/tr[10]/td[9]/div/input')


    gbspxz = (By.XPATH, ' /html/body/div[2]/span[1]/a[3] ')
    tjtj = (By.ID, 'GoodsSaleSettingBatchChangePriceForm_SubmitButton')

    #6、供应站销售指定罪犯/指定商品/指定仓库（切） 均购买2两次
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
    spslsrk_input = (By.XPATH, '//*[@id="GoodsOrderSaleForm_Goods_ListTable"]/tbody/tr[2]/td[8]/div[1]/input')
    gyzxsjz = (By.XPATH, '//*[@id="GoodsOrderSaleForm_SubmitButton"]')
    qrjz = (By.XPATH, '//*[@id="Modal_SaleSettyle"]')

    tknr = (By.CSS_SELECTOR, 'html body.fixed-nav.fixed-sidebar.full-height-layout.gray-bg div#layui-layer4.layui-layer.layui-layer-dialog.layer-ext-moon div.layui-layer-content.layui-layer-padding')
    tkqr = (By.CSS_SELECTOR,'html body.fixed-nav.fixed-sidebar.full-height-layout.gray-bg div#layui-layer4.layui-layer.layui-layer-dialog.layer-ext-moon div.layui-layer-btn.layui-layer-btn- a.layui-layer-btn0')

    #1、初始化创建罪犯
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

    def click_zfxb(self):
        self.find_element(*self.zfxb).click()

    def input_zfxbsr(self, zfxb1):
        self.find_element(*self.zfxb_input).send_keys(zfxb1)
        self.find_element(*self.zfxb_input).send_keys(Keys.ENTER)


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

    '''
    # 2、初始化罪犯资金下账(监狱配置-下账自动提交)
    def click_zjywgl(self):
        self.find_element(*self.zjywgl).click()

    def click_zjxz(self):
        self.find_element(*self.zjxz).click()

    def switch_zjxz(self):
        self.switch_frame(*self.zjxz_frame)

    def click_tjxz(self):
        self.find_element(*self.tjxz).click()

    def switch_outframe(self):
        self.switch_out()

    def click_zjxzgb(self):
        self.find_element(*self.zjxzgb).click()

    def click_zjxzgb(self):
        self.find_element(*self.zjxzgb).click()

    def switch_tjxz(self):
        self.switch_frame(*self.tjxz_frame)

    def click_xzzjfl(self):
        self.find_element(*self.xzzjfl).click()

    def input_xzzjfl(self, xzzjfl1):
        self.find_element(*self.xzzjfl_input).send_keys(xzzjfl1)
        self.find_element(*self.xzzjfl_input).send_keys(Keys.ENTER)

    def click_xzzjlx(self):
        self.find_element(*self.xzzjlx).click()

    def input_xzzjlx(self, xzzjlx1):
        self.find_element(*self.xzzjlx_input).send_keys(xzzjlx1)
        self.find_element(*self.xzzjlx_input).send_keys(Keys.ENTER)

    def input_xzzfxm(self, xzzfxm1):
        self.find_element(*self.xzzfxm_input).send_keys(xzzfxm1)
        time.sleep(3)
        self.find_element(*self.xzzfxm_input).send_keys(Keys.DOWN)
        time.sleep(3)
        self.find_element(*self.xzzfxm_input).send_keys(Keys.ENTER)
        time.sleep(3)

    def input_xzxzje(self, xzje1):
        self.find_element(*self.xzje).send_keys(xzje1)

    def click_xzxyb(self):
        self.find_element(*self.xzxyb).click()

    def click_xzgb(self):
        self.find_element(*self.xzgb).click()
    
    '''

    ## 3、初始化罪犯资金上账(监狱配置-上账自动提交)
    def click_zjywgl(self):
        self.find_element(*self.zjywgl).click()

    def click_zjsz(self):
        self.find_element(*self.zjsz).click()

    def switch_zjsz(self):
        self.switch_frame(*self.zjsz_frame)

    def click_xzsz(self):
        self.find_element(*self.xzsz).click()

    def switch_outframe(self):
        self.switch_out()

    def click_zjszgb(self):
        self.find_element(*self.zjszgb).click()

    def click_szzjfl(self):
        self.find_element(*self.szzjfl).click()

    def input_szzjfl(self, szzjfl1):
        self.find_element(*self.szzjfl_input).send_keys(szzjfl1)
        self.find_element(*self.szzjfl_input).send_keys(Keys.ENTER)

    def click_szzjlx(self):
        self.find_element(*self.szzjlx).click()

    def input_szzjlx(self, szzjlx1):
        self.find_element(*self.szzjlx_input).send_keys(szzjlx1)
        self.find_element(*self.szzjlx_input).send_keys(Keys.ENTER)

    def input_szzfxm(self, szzfxm1):
        self.find_element(*self.szzfxm_input).send_keys(szzfxm1)
        time.sleep(3)
        self.find_element(*self.szzfxm_input).send_keys(Keys.DOWN)
        time.sleep(3)
        self.find_element(*self.szzfxm_input).send_keys(Keys.ENTER)
        time.sleep(3)

    def input_szje(self, szje1):
        self.find_element(*self.szje_input).send_keys(szje1)

    def click_qbsz(self):
        self.find_element(*self.qbsz).click()

    def click_szxyb(self):
        self.find_element(*self.szxyb).click()

    def click_szgb(self):
        self.find_element(*self.szgb).click()

    def click_tjsz(self):
        self.find_element(*self.tjsz).click()

    def click_qrsz(self):
        self.find_element(*self.qrsz).click()


    #4、初始化修改关联处遇额度
    def click_zfxfgk(self):
        self.find_element(*self.zfxfgk).click()

    def click_cyed(self):
        self.find_element(*self.cyed).click()

    def switch_cyed(self):
        self.switch_frame(*self.cyed_frame)

    def click_ze1bxz(self):
        self.find_element(*self.ze1bxz).click()

    def click_a1bxz(self):
        self.find_element(*self.a1bxz).click()

    def click_b1bxz(self):
        self.find_element(*self.b1bxz).click()

    def click_gwcsbxz(self):
        self.find_element(*self.gwcs1bxz).click()

    # ------【一级处遇等级{高}】
    def click_ze1bzx(self):
        self.find_element(*self.ze1_bxz).click()

    def click_ze1xz(self):
        self.find_element(*self.ze1_xz).click()

    def input_zed1(self, zed1):
        self.find_element(*self.ze1_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.ze1_input).send_keys(zed1)

    def click_a1bzx(self):
        self.find_element(*self.a1_bxz).click()

    def click_a1xz(self):
        self.find_element(*self.a1_xz).click()

    def input_a1(self, ad1):
        self.find_element(*self.a1_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.a1_input).send_keys(ad1)

    def click_b1bzx(self):
        self.find_element(*self.b1_bxz).click()

    def click_b1xz(self):
        self.find_element(*self.b1_xz).click()

    def input_b1(self, bd1):
        self.find_element(*self.b1_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.b1_input).send_keys(bd1)

    def click_gwcs1xz(self):
        self.find_element(*self.gwcs1_xz).click()

    def input_gwcs1xz(self, gwcs1xz1):
        self.find_element(*self.gwcs1_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.gwcs1_input).send_keys(gwcs1xz1)

    # -----【二级处遇等级{底}】
    def click_ze2bzx(self):
        self.find_element(*self.ze2_bxz).click()

    def click_ze2xz(self):
        self.find_element(*self.ze2_xz).click()

    def input_zed2(self, zed2):
        self.find_element(*self.ze2_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.ze2_input).send_keys(zed2)

    def click_a2bzx(self):
        self.find_element(*self.a2_bxz).click()

    def click_a2xz(self):
        self.find_element(*self.a2_xz).click()

    def input_a2(self, ad2):
        self.find_element(*self.a2_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.a2_input).send_keys(ad2)

    def click_b2bzx(self):
        self.find_element(*self.b2_bxz).click()

    def click_b2xz(self):
        self.find_element(*self.b2_xz).click()

    def input_b2(self, bd2):
        self.find_element(*self.b2_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.b2_input).send_keys(bd2)

    def click_cyedbc(self):
        self.find_element(*self.cyedbc).click()

    def click_gwcs2xz(self):
        self.find_element(*self.gwcs2_xz).click()

    def input_gwcs2xz(self, gwcs2xz1):
        self.find_element(*self.gwcs2_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.gwcs2_input).send_keys(gwcs2xz1)

    '''
    #5、初始化指定商品类型改价【===修改商品信息处价格无效===】
    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_spxxgl(self):
        self.find_element(*self.spxxgl).click()

    def switch_spxxgl(self):
        self.switch_frame(*self.spbhsrk_frame)

    def input_spbhsrk(self, spbh1):
        self.find_element(*self.spbhsrk_input).send_keys(spbh1)
        self.find_element(*self.spbhsrk_input).send_keys(Keys.ENTER)

    def click_spxxxg(self):
        self.find_element(*self.spxxxg).click()

    def click_spsxgl(self):
        self.find_element(*self.spsxgl).click()

    def input_splsjg(self, splsjg1):
        self.find_element(*self.splsjg).send_keys(Keys.CONTROL, 'a')
        time.sleep(3)
        self.find_element(*self.splsjg).send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        self.find_element(*self.splsjg).send_keys(splsjg1)

    def click_spxxbc(self):
        self.find_element(*self.spbcnr).click()

    #############在售商品管理处进行修改##############################
    '''
    # 仓库设置

    def click_jcxxgl(self):
        self.find_element(*self.jcxxgl).click()

    def click_ckxxgl(self):
        self.find_element(*self.ckxxgl).click()

    def switch_ckxxgl(self):
        self.switch_frame(*self.ckxxgl_frame)

    def click_ck1zcck(self):
        self.find_element(*self.ck1zcck).click()

    def click_ck2zcck(self):
        self.find_element(*self.ck2zcck).click()

    def click_tkqr(self):
        self.find_element(*self.tkqr).click()

    def click_xsywgl(self):
        self.find_element(*self.xsywgl).click()

    def click_zsspgl(self):
        self.find_element(*self.zsspgl).click()

    def switch_zsspgl(self):
        self.switch_frame(*self.zsspgl_frame)

    def click_spyjtj(self):
        self.find_element(*self.spyjtj).click()

    def switch_outframe(self):
        self.switch_out()

    def click_zsspgb(self):
        self.find_element(*self.zsspgb).click()

    def input_xxsj(self, xxsj1):
        self.find_element(*self.xxsj_input).send_keys(Keys.CONTROL ,'a')
        self.find_element(*self.xxsj_input).send_keys(xxsj1)

    def click_xzsp(self):
        self.find_element(*self.xzsp).click()

    def input_spbhsrk(self, spbh1):
        self.find_element(*self.spbhsrk_input).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.spbhsrk_input).send_keys(spbh1)

    def click_cpcx(self):
        self.find_element(*self.spcx).click()

    def click_xzspgx(self):
        self.find_element(*self.xzspgx).click()

    def click_gbspxz(self):
        self.find_element(*self.gbspxz).click()

    def input_sp1xls(self, sp1xls1):
        self.find_element(*self.sp1xls).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.sp1xls).send_keys(sp1xls1)

    def input_sp2xls(self, sp2xls1):
        self.find_element(*self.sp2xls).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.sp2xls).send_keys(sp2xls1)

    def input_sp3xls(self, sp3xls1):
        self.find_element(*self.sp3xls).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.sp3xls).send_keys(sp3xls1)

    def input_sp4xls(self, sp4xls1):
        self.find_element(*self.sp4xls).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.sp4xls).send_keys(sp4xls1)

    def input_sp5xls(self, sp5xls1):
        self.find_element(*self.sp5xls).send_keys(Keys.CONTROL, 'a')
        self.find_element(*self.sp5xls).send_keys(sp5xls1)

    def click_xsjtb(self):
        self.find_element(*self.xsjtb).click()

    def click_tjtj(self):
        self.find_element(*self.tjtj).click()


    # 6、供应站销售指定罪犯/指定商品/指定仓库（切） 均购买2两次
    def click_xsywgl(self):
        self.find_element(*self.xsywgl).click()

    def click_gyzxs(self):
        self.find_element(*self.gyzxs).click()

    def switch_gyzxs(self):
        self.switch_frame(*self.gyzxs_frame)

    def input_gyzzfxm(self, zfxm1):
        self.find_element(*self.zfxm_input).send_keys(zfxm1)
        time.sleep(4)
        self.find_element(*self.zfxm_input).send_keys(Keys.DOWN)
        time.sleep(3)
        self.find_element(*self.zfxm_input).send_keys(Keys.ENTER)
        time.sleep(3)

    def click_cksrk(self):
        self.find_element(*self.cksrk).click()

    def input_cksrk(self, ckmc1):
        self.find_element(*self.cksrk_input).send_keys(ckmc1)
        self.find_element(*self.cksrk_input).send_keys(Keys.ENTER)

    def input_spbh(self, sbh2):
        self.find_element(*self.spbh_input).send_keys(sbh2)
        time.sleep(3)
        self.find_element(*self.spbh_input).send_keys(Keys.DOWN)
        time.sleep(3)
        self.find_element(*self.spbh_input).send_keys(Keys.ENTER)
        time.sleep(3)

    def input_spslsrk(self, spsl1):
        self.find_element(*self.spslsrk_input).send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        self.find_element(*self.spslsrk_input).send_keys(spsl1)

    def click_spxsjz(self):
        self.find_element(*self.gyzxsjz).click()

    def click_qrjz(self):
        self.find_element(*self.qrjz).click()

    def gett_tknr(self):
        self.b = self.find_element(*self.tknr).get_attribute('textContent')
        return self.b

    def click_tkqr(self):
        self.find_element(*self.tkqr).click()
        



























