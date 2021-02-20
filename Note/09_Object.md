# Python Note

## Object()
* 基本寫法
```python
# 寫法 一
class NameOfClass(object):
	'''comment'''
	def __init__(self, argu1, argu2): # 資料屬性
		self.valueI = argu1 
		self.valueII = argu2
	def show(self): # 方法屬性
		print(self.valueI)
		print(self.valueII)
# 寫法二
class NameOfClass:
	'''comment'''
	def __init__(self, argu1, argu2):
		self.valueI = argu1
		self.valueII = argu2
	def show(self):
		print(self.valueI)
		print(self.valueII)

# 寫法三
class NameOfClass:
	'''comment'''
	valueI = 'v1'
	valueII = 'v2'
	def show(self):
		print(self.valueI)
		print(self.valueII)
```
* 私有屬性 ( 加兩個 底線)
```python
class NameOfClass:
	'''comment'''
	def __init__(self, argu1, argu2):
		self.valueI = argu1
		self.__valueII = argu2 # 私有資料屬性
	def show(self):
		print(self.valueI)
		print(self.valueII)
	def __p(self): # 私有方法屬性
		return self
# 破解 私有屬性(在 該屬性前用 一個底線加類別名):
Name._NameOfClass__valueII #破解 私有資料
Name._NameOfClass__p() #破解 私有方法

# python style (設私有屬性, 取, 更改):
class NameO:
    def __init__(self, argu1, argu2):
        self.val1 = argu1
        self.__val2 = argu2 # 私有屬性
    def get(self): # 讀取 私有屬性
        return self.__val2 
    def set(self, argu): # 更改 私有屬性
        self.__val2 = argu 

x = NameO(3,6) # 讀取 私有屬性
print(x.get()) # 6

x.set(7) # 更改 私有屬性
print(x.get()) # 7
```
* 裝飾器
```python
# @property
class NameOfClass:
	def __init__(self, argu):
		self.__argu = argu
	
	@property
	def get(self):
		return self.__argu

	@get.setter #setter
	def get(self, argu):
		self.__argu = argu

x = NameOfClass(3)
print(x.get) #透過 設@property後 該func()可直接以 屬性方式呼叫 

x.get = 9
print(x.get) # 9

```
* 類別方法
```python
class NameOfClass:
	counter = 0
	def __init__(self):
		NameOfClass.counter += 1
	@classmethod
	def show(cls):
		print(f'classmothod\nclass={cls}\nclass.counter={NameOfClass.counter}')

x = NameOfClass()
y = NameOfClass()
a = NameOfClass()
b = NameOfClass()
NameOfClass.show()
'''
classmothod
class=<class '__main__.NameOfClass'>
class.counter=4
'''
```
* 靜態方法 (可以不需參數)
```python
class NameOfClass:
	@staticmethod # 沒有這行也會顯示
	def show():
		print('hello python')
		
NameOfClass.show() # 不需參數
```
* 繼承 (inheritance)
```python
class Parent:
	@staticmethod
	def show():
		print('hi im origin')

class Child(Parent): # 繼承 Parent 
	@staticmethod
	def showII(): # 新增加的 屬性 
		print('im second')
x = Parent()
y = Child()

x.show() # hi im origin

y.show() # hi im origin
y.showII() # im second
```

* 繼承 - 取得 基底類別屬性 與取得 兄弟類別
```python
# 觀念: 一般繼承 會繼承 方法屬性, 但不會繼承 資料屬性
# super().__init__() :取得 基底 類別資料屬性
class GrandParent:
	def __init__(self):
		self.val1 = 1000
	def hi(self):
		print('hi')

class Parent(GrandParent):
	def __init__(self):
		self.val2 = 500
		super().__init__() # 繼承 基底 類別的資料屬性
	def show(self):
		print(f'grand:{self.val1}\nme:{self.val2}')

class Child(Parent):
	def __init__(self):
		self.val3 = 200
		super().__init__() # 繼承 基底 類別的資料屬性
	def show(self):
		print(f'grand:{self.val1}\nparent:{self.val2}\nchild:{self.val3}')

x = GrandParent()
y = Parent()
z = Child()
z.show() 
z.hi() # 不需super()也可以執行
```

* polymorphism





