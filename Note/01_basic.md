# Python note

## basic concenpt
### python 是 動態語言 
```python
a = 10
b = 10
print(id(a)) # reference of a and b will be the same
print(id(b))
``` 
### coding style
```python
# have to have a space near by operator
x = y + z 
x = (y + z) 
# variable name: 
student, student_num = 34 
# class name
Model, MyClass
# function
func1, func1_print
# constant
CONSTANT, MY_CONSTANT #python無法定義變數為 const 只能寫時不要去變它
# 因程式碼當行太長以 \ 換行
a = x = \
y = z = 10
print(a, x, y, z)
# 換行方式二 以括號將太長的敘述包起
a = (1+ #註解
	 2+
	 3+
	 4)
print(a)
```
### compution
```python
x = 3 ** 4
print(x) # 3的四次方

x = 9 // 2
print(x) # 9除以2後 取整除 = 4

# && == and
# || == or
# ! == not
a = 2
b = 2
if a and b == 2:  
	print('a==b') 
else:
	print('a!=b')

# is / is not 會比較兩變數的 地址是否相同
if a is b: # 或是用 is not 
	print('a==b')
else:
	print('b!=b')
```
###  等號的多重指定使用
```python
x = y = z = 10
print(x) # 10

x, y, z = 10, 20, 30
print(x, y, z) # 10 20 30

x, y = y, x
print(x, y) # 20 10

a = divmod(9, 5) #一次獲得 商 跟 餘數 (divmod會回傳tuple)
print(a) # (1, 4)
b, c = a
print(b, c) # 1 4
```
### 刪除變數 (節省記憶體空間)
```python
x = 10
print(x)
del x
print(id(x)) #會跳出錯誤警訊, 因為該變數已被刪除
```
### 型別
```python
"""
1. int 沒有被限制在 32 位元
2. int 在 運算時 會轉成 浮點數 再進行運算 
3. 布林值: True, False (轉為int為1, 0)
4. 被視為False的值: 0, 0.0, ''(空字串), [] (空陣列), (), {}, set(), None (其他都會被視為 True)
5. python只有字串 沒有字元
"""

# 型別轉換
int(variable) # 都是不改變原變數, 回傳要的型別
float(variable)
str(variable) 

# 近位制
a = 0b1001 # 二進位制
b = 0o1 # 8 進位制
c = 0x1 # 16 進位制
print(a, b)
print(bin(a), oct(b), hex(c)) #印出 2進位, 8進位 16進制結果

# 複數 (實數 + 虛數)
a = 3 + 5j
b = complex(3,5)
print(a)
print(b)

# 字串
a = 'hi'
b = 'llo'
c = a + b
print(c) # hillo

a = 'a'
a = a*5
print(a) # aaaaa

c = 'hello\tworld'
print(c) # hello    world (會編譯\t字元)
print(r'hello\tworld') # hello\tworld (不會編譯逸出字元) 

# 字串 轉成 byte資料
a = b'hello world' 
	#or a = 'hello world'; a = string.encode('utf-8')
print(type(a)) # bytes
# byte資料 轉成 字串
a = b'hello'
a = stringBytes.decode('utf-8')
print(type(a)) # string
```