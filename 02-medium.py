#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	FUNCTION (return more than one value)
print('\n\t***** FUNCITON *****')
def foo(x, y):
   return x**2, y**2
a, b = 2, 3
print(f"pre: {a,b}")
a, b = foo(a, b)  # a == 4; b == 9
print(f"after foo(): {a,b}")

# LIST (like array)
print('\n\t***** LIST (like array) *****')
ls = [6,"john",1.3,True]
print(ls)
	#by reference
def add(num):
	num[0]+=1
add(ls)
print(ls)
ls.append('newelement')
ls.append('newelement2')
ls.pop()
print(ls)

# TUPLE ( unmutable list , 宣告是如何就是如何 只能唯讀)
print('\n***** TUPLE (unmutable list) *****')
t = (3,6,7)
print(t, t[1])


# DICTIONARY
print('\n***** DICTIONARY *****')
dic = {
	'key1':'value1',
	'key2':'value2'
	}
print(dic)
print(dic['key2'])
	#add key/value
dic['newKey']='newValue'
	#delete key/value
del dic['key1']
print(dic)

# SET (無重複元素容器)
print('\n***** SET (無重複元素容器) *****')
st = {
	'pig',
	'cat',
	'cat'
}
print(st) #it will be: {'cat', 'pig'}



