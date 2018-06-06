#coding = utf-8
import csv
import sys
#访问本地文件
my_file= 'D:\\Phyon\\pycharm_code\\idle_file_code\\表单参数化\\userinfo.csv'
data=csv.reader(open(my_file,"r"))

#user表示读取表中第一列名字，user表示读取表中第二列邮箱以此类推
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
    print(user[3])


