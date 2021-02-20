# Python note

## 串列 (list)
```python
# 為一物件
# 類似 array, 但同一list能儲存 不同元素: int, float, string, list, tuple, dictionary.
list_1 = [1, 2.2, 'hi', [3,4], (5,6), {1:2, 3:4}]
for i in list_1:
	print(i) 
```
### 串列切片
```python
list_1[start:end] 
list_1[start:end:step]

list_1[:n] #取 前 n 個
list_1[n:] #取 後 n 個
list_1[:-n] #取 串列不含 後 n 個
list_1[-n:] #取 串列第 n 個到 最後

list_1[:] #取 整個 串列

list_1[-1] # 取 最後一個 元素
```
## 串列的 新增
```python
x = [1,6,3]
x.append(5) # x = [1,6,3,5]

# insert使用: x.insert(index, element)
x.insert(1, 9) # x = [1,9,6,3,5]

```
### 串列的 刪除
```python
# .pop()
x = [1,6,3]
y = x.pop() # x = [6,3]; y = 1

# del
del name[i] # 刪除第 i 個元素
del name[start:end] # 刪除從 start 至 end-1 的元素
del list_1[start:end:step] # 從 start 至 end-1 間隔step步 刪除元素

del list_1 # 刪除 整個串列

# .remove() ( name.remove(element) )
x = [2,3,6]
x.remove(3)
print(x) # [2,6]
```
### 串列加乘
```python
list_1 = ['a', 1, 'c']
list_2 = [2, 'e']
list_3 = list_1 + list_2
print(list_3) # ['a', 1, 'c', 2, 'e']

list_4 = list_3*3
print(list_4) # ['a', 1, 'c', 2, 'e', 'a', 1, 'c', 2, 'e', 'a', 1, 'c', 2, 'e']
```
### 串列 物件內建相關function使用
```python
# 串列中 取最大小值
list_1 = [2,1,5,4,8]
list_max = max(list_1) # 取得 串列中最大 數值
list_min = min(list_1) # 取得 串列中最小 數值
list_sum = sum(list_1) # 取得 串列中 數值總和

# 反轉串列
x = [1,2,3,4,5]
x.reverse()
print(x) #[5,4,3,2,1]

	# 其他反轉法 (串列與字串皆可使用)
x = x[::-1]

# 串列排序 ( .sort() )
x = [3,6,1,4,8,3,6,2]
x.sort() # 由小到大排序
print(x) # [1, 2, 3, 3, 4, 6, 6, 8]
x.sort(reverse=True) # 由大到小排序
print(x) # [8, 6, 6, 4, 3, 3, 2, 1]

	# 不更改原串列的 排序 ( sorted(x) ) 
x = [3,6,1,4,8,3,6,2]
y = sorted(x)
print(x) #[3, 6, 1, 4, 8, 3, 6, 2]
print(y) #[1, 2, 3, 3, 4, 6, 6, 8]

x = [3,6,1,4,8,3,6,2]
y = sorted(x, reverse=True)
print(x) #[3, 6, 1, 4, 8, 3, 6, 2]
print(y) #[8, 6, 6, 4, 3, 3, 2, 1]

# in 判斷是否含有該元素 在串列(or字典)
x = [1,4,7]
if 5 in x: # 或是用: not in
	print('have 5')
else:
	print('no 5')

# .index() 尋找 特定元素 並回傳第一次出現
x = [3,6,2,7,1,4,9]
idx = x.index(7) # 若不存在 程式會無法順利編譯
print(idx) # 3

# .count() 回傳 特定元素 在串列中有幾個
x = [3,14,75,3,541,6,2]
cnt = x.count(3)
print(cnt) # 2

# extend() 連接兩個串列
x = [2,3,6]
y = [1,4,5]
x.extend(y)
print(x) # [2, 3, 6, 1, 4, 5]
print(y) # [1, 4, 5]
```
### 串列的 copy (使兩相同值的串列可以分別處理而互不影響)
```python
# 切片copy ( 效果與 淺copy一樣)
a = [1,2,3]
b = a[:]
print(id(a), id(b))
# 淺copy (串列 位址會不同 但串列中的 子物件 位址 還是會相同)
a = [1,2,[3,4]]
b = a.copy()

print(id(a), id(b)) # will be different
print(id(a[2]), id(b[2])) # will be the same

# 深copy (皆會不同)
import copy
a = [1,2,[3,4]]
b = copy.deepcopy(a)
print(id(a), id(b)) # will be different
print(id(a[2]), id(b[2])) # will be "different"
```
### 二維串列
```python
x = [['stu1', 80],
	 ['str2', 100],
	 ['stu3', 90]
	]
```
### 多重指定串列
```python
# *name 會將 多餘元素 包成串列 指派給該變數
a, b, *c = 1, 2, 3, 4, 5
print(a, b, c) # 1, 2, (3,4,5)
a, *b, c = 1, 2, 3, 4, 5
print(a, b, c) # 1, (2,3,4), 5
```

## Tuple
* 除宣告時以 () 宣告, 且元素個數與值 不可變 以外 皆與 list 相同
```python
x = tuple(range(0,100,5)) # 以generator生成
print(x)
```
* 較省資源 也更安全
* 如欲修改 直接重新定義
```python
x = (2,3,4)
x = (1,2,3)
```
* 可與 list 互換資料型態
```python
x = (2,3,4)
print(x) # (2, 3, 4)
x = list(x)
print(x) # [2, 3, 4]
x = tuple(x)
print(x) # (2, 3, 4)
```
* 換成enumetate物件後 轉成list:
```python
x = (2,3,4)
y = enumerate(x)
print(y) # <enumerate object at 0x107d52af0>
y = list(y)
print(y) # [(0, 2), (1, 3), (2, 4)]
```

## 其他相關資料型態
* zip
```python
x = (1,2,3)
y = ['q','g','y']
z = zip(x,y) # 以 zip 打包
print(z) # <zip object at 0x10b0cfa50>
z = list(z)
print(z) # [(1, 'q'), (2, 'g'), (3, 'y')]
z = tuple(z)
print(z) # ((1, 'q'), (2, 'g'), (3, 'y'))
 
```
