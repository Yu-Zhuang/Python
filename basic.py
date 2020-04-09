#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# === variable announcement ===
print('\t************* variable announcement / print() / input() *************')
str_1 = "hello"
num = 6
# print function
print(str_1)
# input function
num = int(input("請輸入數字: "))

# === if/ elif / else ===
print('\t************* if / elif / else *************')
if num>0:
	print('num>0')
elif num==0:
	print('num=0')
else:
	print('num<0')

# =====  LOOP =====
# 可搭配 break / continue 使用.
# for loop
print('\t************* for / while loop *************')
for i in range(3):
	print(i)

for k in str_1:
	print(k)

for u in range(0,10,2): 
	print(u)
# while loop
count = 0
while num>0:
	num-=1
	count+=1
print(num, count)

# ====== function ======
# def 函数名(参数1，参数2....参数n):
#     函数体
#     return 语句
print('\t************* function *************')
def add(num_1, num_2):
	ret = num_1+num_2
	return ret
print("add(5,3)=", add(5,3))



