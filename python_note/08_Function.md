# Python Note

## Function()
* 基本寫法:
```python
def function_name(argument):  
	"""function comment"""
	'''compution'''
	return

# add type hint	(有需要其他資料型態hint時需: from typing import List,Tuple,Dict,NewType...)
def function_name(argument: int, argument2: str) -> int: 
	"""function comment"""
	'''compution'''
	return 

# 一次傳多筆資料 ( 會回傳以 tuple 包多筆回傳值的資料 )
def function_name(argument):
	return 1,2,3
x = function_name()
print(x) # (1,2,3) 

# ps. 沒有return 則會 return None
```
* 關鍵字參數 (直接指定參數=value, 無論順序)
```python
def hi(name: str, say: str) -> bool:
	print(f'{name} say: {say}')
	return True
hi('john', 'hello')
hi(say='hello', name='john') # outcome will be the same
```
* 參數預設值
```python
def function_name(argument='預設參數值'):  
	"""function comment"""
	'''compution'''
	return
# ps該預設值為 串列 或相似型態時, 重複呼叫使用 預設值 結果是會累加的
```
* 參數是 串列, 字典 等物件時 會是by reference

* 隨意參數數量
```python
def function_name(*argu):
	'''comment'''
	print(argu)
# 加上 * 代表該變數 可以是接受任意數量, 傳進去會包成tuple
```
* 任意數量的 關鍵字參數 (會包成 字典 傳入)
```python
def function_name(**argu):
	'''comment'''
	print(argu)
function_name(key='value', key2='value3') # {'key': 'value', 'key2': 'value3'}
```
* function() 本身也是 物件, 可以當 參數傳遞 與回傳, 也可以 動態建立與刪除
* 閉包 (closure)
```python
def func1():
	b = 'hi '
	def hi(name):
		return b+name
	return hi

fnc = func1()
print(fnc('john')) # hi john
```
* 匿名函數 lamda
```python
add = lambda x, y: x+y
print( add(5,3) ) # 8
```
* 匿名函數 應用在 filter() 與 map(), reduce()
```python
# filter(func, iterable)
x = [1,2,3,4,5,6,7,8,9,10]
print( list( filter(lambda x: x%2 is 0, x) ) ) # [2, 4, 6, 8, 10]

# map(func, iterable)
x = [1,2,3,4,5,6,7,8,9,10]
print( list( map(lambda x: x%2 is 0, x) ) )
	# [False, True, False, True, False, True, False, True, False, True]

# reduce(func, iterable)
from functools import reduce
x = { '1':'2', '3':'4', '5':'6' }
print( list( reduce(lambda x,y: x+y, x) ) ) # ['1', '3', '5']
	
```

