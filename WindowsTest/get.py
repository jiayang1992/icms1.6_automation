#coding=utf-8
import sys
from peopleDic import people
# 一个使用get()的简单数据库
# 在这里插入代码清单4-1中的数据库（字典people）
labels = {   'phone': 'phone number',    'addr': 'address' }
name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
key = request
# 如果request既不是'p'也不是'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))