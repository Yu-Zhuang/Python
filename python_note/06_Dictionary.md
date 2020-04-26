# Python Note

## Dictionary
* 非序列資料, 是 key and vale
```python
# name = { key1:vale1, key2:vale2 }
dic1 = { 'stu1':'john', 2:7 }
print(dic1['stu1']) # john
print(dic1[2]) # 7
```
* 走訪 字典
```python
# 走訪字典中 key 
dic1 = { 'stu1':'john', 2:7, 'key':'value' }
for i in dic1: # 或是 for i in dic1.keys():
	print(i) 
'''
stu1
2
key
'''
# 走訪字典中 value
dic1 = { 'stu1':'john', 2:7, 'key':'value' }
for i in dic1.values():
	print(i) 
'''
john
7
value
'''

# 走訪字典中 key:value
dic1 = { 'stu1':'john', 2:7, 'key':'value' }
for i,j in dic1.items():
	print(i,j) 
'''
stu1 john
2 7
key value
'''
dic1 = { 'stu1':'john', 2:7, 'key':'value' }
for i in dic1.items():
	print(i) 
'''
('stu1', 'john')
(2, 7)
('key', 'value')
'''
```
* 新增元素
```python
dic1 = { 'key1':'value1' }
print(dic1) # {'key1': 'value1'}
dic1['key2'] = 'vale2'
print(dic1) # {'key1': 'value1', 'key2': 'vale2'}
```
* 更改
```python
dic1 = { 'key1':'value1'}
print(dic1) # {'key1': 'value1'}
dic1['key1']='new'
print(dic1) # {'key1': 'new'}
```
* 刪除
```python
# del
dic1 = { 'key1':'value1', 'key2':'vale2'}
print(dic1) # {'key1': 'value1', 'key2': 'vale2'}
del dic1['key1']
print(dic1) # {'key2': 'vale2'}

# pop()
dic1 = { 'key1':'value1', 'key2':'vale2'}
print(dic1) # {'key1': 'value1', 'key2': 'vale2'}
take = dic1.pop('key1')
print(dic1) # {'key2': 'vale2'}
print(take) # value1

# popitem() :隨機刪除一個字典元素 並回傳該元素(以tuple包)
dic1 = { 'key1':'value1', 'key2':'vale2', 'key3':'value3', 'key4':'value4' }
print(dic1) # {'key1': 'value1', 'key2': 'vale2', 'key3': 'value3', 'key4': 'value4'}
take1 = dic1.popitem()
take2 = dic1.popitem()
print(dic1) # {'key1': 'value1', 'key2': 'vale2'}
print(take1, take2) # ('key4', 'value4') ('key3', 'value3')

# clear :刪除字典所有元素
dic1 = { 'key1':'value1', 'key2':'vale2', 'key3':'value3', 'key4':'value4' }
print(dic1) # {'key1': 'value1', 'key2': 'vale2', 'key3': 'value3', 'key4': 'value4'}
dic1.clear()
print(dic1) # {}
```
* 拷貝 copy
```python
# 淺拷貝
dic1 = { 'key1':'value1', 'key2':'vale2'}
dic2 = dic1.copy()

# 深拷貝
import copy
dic1 = { 'key1':'value1', 'key2':'vale2'}
dic2 = copy.deepcopy(dic1)
```
* 元素是否存在
```python
dic1 = { 'key1':'value1', 'key2':'vale2', 'key3':'value3', 'key4':'value4' }

if 'key1' in dic1:
	print('have key1') # have key1 (其他的都不會是True跟顯示)
if 'value1' in dic1:
	print('have value1')

if 'keyN' in dic1:
	print('have keyN')
if 'valueN' in dic1:
	print('have valueN')
```
* 合併字典 update()
```python
dic1 = { 'key1':'value1', 'key2':'vale2' }
dic2 = { 'key3':'value3', 'key4':'value4' }
dic1.update(dic2)
print(dic1) # {'key1': 'value1', 'key2': 'vale2', 'key3': 'value3', 'key4': 'value4'}
```
* 串列 轉 字典
```python
list1 = [ ['key1', 'key2'], ['key3', 'key4'] ]
dic1 = dict(list1)
print(dic1) # {'key1': 'key2', 'key3': 'key4'}
''' 字典 轉 串列 只會存到 key
list1 = list(dic1)
print(list1) # ['key1', 'key3']
'''
# fromkeys() ((tuple 也可使用此方法))
list1 = ['name', 'name2']
dic1 = dict.fromkeys(list1, 'value')
print(dic1) # {'name': 'value', 'name2': 'value'}
```

* 排序 字典
```python
# 依照 key 排
dic1 = { 'key1':'value1', 'key2':'vale2', 'key3':'value3', 'key4':'value4' }
for i in sorted(dic1.keys()):
	print(i)
'''
key1
key2
key3
key4
'''
for i in sorted(dic1.keys(), reverse=True):
	print(i)
'''
key4
key3
key2
key1
'''
# 依照 value 排 就用 .values()
```

* 搜尋 鍵的值 get()
```python
dic1 = { 'key1':'value1', 'key2':'vale2', 'key3':'value3', 'key4':'value4' }
take = dic1.get('key2', None) # 有找到傳回該鍵對應的值, 沒則傳回 default值
print(take) # value2
```

* 搜尋, 有則回傳值, 無則新增該 鍵:值
```python
dic1 = { 'key1':'value1', 'key2':'vale2' }
take = dic1.setdefault('keyN', 100) # 有找到傳回該鍵對應的值, 沒則傳回 default值並新增該 鍵:值
print(dic1) #{'key1': 'value1', 'key2': 'vale2', 'keyN': 100}
print(take) #100
take = dic1.setdefault('key2', None)
print(take) #vale2
```






