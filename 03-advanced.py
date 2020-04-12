#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CLASS and OBJECT
print('***** Class and Object *****')
	#class
class student(object):
	def __init__(self, name, grade, address): #物件的建構子
		self.name = name
		self.grade = grade
		self.__address = address #私有成員
	def printStudent(self): #物件的方法
		print(f'name: {self.name}')
		print(f'grade: {self.grade}')
	def __getAdr(self): #私有方法
		return self.__address
	# construct object through class
s1 = student('john',90,'taiwan')
s1.printStudent()
	#by reference 
def change_name(object):
	object.name = 'name_change'
	object.new = 'new attribute' #add new attribute
	
change_name(s1)
s1.printStudent()
print(s1.new)
