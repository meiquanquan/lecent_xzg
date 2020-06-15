import os,sys
import csv
sys.path.append('..')
BASE_PATH=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]   #返回项目当前所在目录
'''
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.split(os.path.dirname(os.path.abspath(__file__))))
print(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
'''
COMMON_PATH=os.path.join(BASE_PATH,'common')
CONFIG_PATH=os.path.join(BASE_PATH,'config')
DATA_PATH=os.path.join(BASE_PATH,'data')
DRIVER_PATH=os.path.join(BASE_PATH,'driver')
IMG_PATH=os.path.join(BASE_PATH,'img')
PAGES_PATH=os.path.join(BASE_PATH,'pages')
REPORT_PATH=os.path.join(BASE_PATH,'report')
TESTCASE_PATH=os.path.join(BASE_PATH,'test_case')
UTILS_PATH=os.path.join(BASE_PATH,'utils')


#定义数据文件处理函数，file为数据文件路劲
def get_data(file):
    f=open(file)
    d=csv.reader(f)
    data=[]
    for i in d:
        data.append(i)
    return data

if __name__=='__main__':
    '''
    file1=DATA_PATH+'/user_data.csv'
    a=get_data(file1)
    print(a)
    print(a[1][0])
    b = 0
    for i in a:
        print(a[b])
        print(a[b][0])
        print(a[b][1])
        b += 1
    '''
    print(COMMON_PATH)