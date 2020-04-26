# Python Note

## Set
* 核心概念: 沒有重複的元素
* 不會包含 可變元素: 例如 串列 (串列,字串,元組會被轉變為集合元素, 字典則是key會被轉成集合元素)
* 以{}將資料包起
```python
# 一般初始化
tu1 = { 'value1', 'value2', 'value2' }
print(tu1) # {'value1', 'value2'}
# 建立 空集合
tu1 = set() 
# 串列 轉 set
list1 = [23,'hih',78,'hoo'] #串列中不能有 子串列
tu = set(list1)
print(tu) # {'hih', 'hoo', 78, 23}
# 字串 轉 set
str1 = 'hello world'
tu =set(str1)
print(tu) # {'o', 'l', 'e', 'w', 'h', 'r', ' ', 'd'}

## set資料 用 list(set_name) 即可轉為 串列

# 凍結集合
x = frozenset([1,3,5]) #此集合不能再更改
```

* 集合的操作
```python
# 交集(intersection) &
a = {'b','c','d','q'}
b = {'q','t','c'}
c = a & b
print(c) # {'q', 'c'}

# 聯集(union) |
a = {'b','c','d','q'}
b = {'q','t','c'}
c = a | b
print(c) # {'b', 'c', 'd', 'q', 't'}

# 差集(difference) -
a = {'b','c','d','q'}
b = {'q','t','c'}
c = a - b
d = b - a
print(c) # {'b', 'd'}
print(d) # {'t'}

# 對稱差集(symmertric difference) ^
a = {'b','c','d','q'}
b = {'q','t','c'}
c = a ^ b
print(c) # {'d', 'b', 't'}

# ==, != 判斷兩 集合 是否相等

# in, not in 判斷 集合是否含有該元素
```

* 新增元素
```python
# .add(element)
s1 = set()
print(s1) # set()
s1.add('element')
pirnt(s1) # {'element'}
```
* 其他常用function()
```python
# .copy(), .remove(), .clear(), .pop()隨機刪除, 

# name.discard() 刪除元素(即使沒有該元素 也不會程式發生錯誤)

# .isdisjoint() : 兩集合沒有共同元素 回傳 True, 否則回傳 False
x = { 1, 2, 3 }
y = { 5, 6 ,7 }
ret = x.isdisjoint(y)
print(ret) # True

# name1.issubset(name2) : 判斷 name1 是否是 name2 的子集合
x = { 1,2 }
y = { 1,2,3,4 }
print( x.issubset(y) ) # True
# ( .isuperset() : 判斷是否是 父集合 )

# A.update(B)  : 將 集合B 元素加到 集合A

# A.difference_update(B) : 將 集合A  中與B集合有聯集的元素刪除
```



