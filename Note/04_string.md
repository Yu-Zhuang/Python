# Python Note

### 字串
```python
# 像字元組成的串列, 但字串裡的元素不能更改

# list(): 字串 轉 串列
x = list('hello')
print(x) # ['h', 'e', 'l', 'l', 'o']

# .split(): 以''將字串分割 並回傳串列
x = ' hello world ha ha '
print(x.split()) #['hello', 'world', 'ha', 'ha']


```
### 字串相關function
```python
# .join(list) (常用在網路爬蟲使用)
path = ['D', 'ch3', 'test.py']
connect = '/'
print(connect.join(path)) # D/ch3/test.py

# .replace()
a = 'hello'
a = a.replace('l','k')
print(a) # hekko



# 字串 相關function
x = 'ABC'
x = x.lower()
print(x) # 'abc'
x = x.upper()
print(x) # 'ABC'

x = x.title()
print(x) # 'Abc'

x = x.swapcase()
print(x) # 'aBC'

x = ' abc '
x = x.lstrip() #刪除字串 左邊 多餘的空白
x = x.rstrip() #刪除字串 右邊 多餘的空白
x = x.strip()  #刪除字串 左右邊 多餘的空白

x = 'abc'
print( x.islower() ) # true
print( x.isupper() ) # false
print( x.isdigit() ) # false
print( x.idalpha() ) # true

# .endswith() / .startswith()
files = ['test.cpp', 'basic.py', 'tree.c']
py = []
for i in files:
	if i.endswith('.py'):
		py.append(i)
print(py) # ['basic.py']
```