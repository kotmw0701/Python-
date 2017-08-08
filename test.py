'''
Created on 2017/08/07

@author: Kotmw0701
'''
# -*- coding: utf-8 -*-

import random

def kiyoshi():
    test_list = [u'ズン', u'ドコ']
    i = 0
    while True:
        random.shuffle(test_list)
        print(test_list[0])
        if test_list[0] == 'ズン':
            i += 1
        elif test_list[0] == 'ドコ':
            if i >= 4:
                print(u'キ・ヨ・シ！')
                break
            i = 0

kiyoshi()

'''
class test:
    
    def __init__(self, name, test):
        self.name = name
        self.test = test
    
    def setName(self, name):
        self.name = name

test1 = test("Kotmw","test")
print(test1.name)
test1.name = "Motlof"
print(test1.name)
for i in range(5):
    print(random.randint(1,5))
'''
