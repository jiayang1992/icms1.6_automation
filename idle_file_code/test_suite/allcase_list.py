#coding = mutf-8
import sys
sys.path.append('\test_suite')
from test_suite import youdao1,baidu1

#用例列表
def caselist():
    alltestcasenames = [baidu1.Baidu,youdao1.Youdao]
    return alltestcasenames