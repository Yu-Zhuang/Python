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

---

##  input & output

### print
```python
# print 語法
print(value, sep="", end='\n', file=sys.stdout, flush=False)
'''
* value: 欲輸出資料, 多筆輸出 以 逗號',' 隔開
* sep: 多筆輸出時 的分隔字元, 預設是一個空白字元
* end: 設定什麼字元為結尾
* file: 資料輸出位置, 預設為sys.stdout (螢幕), 也可以設為其他檔案或設備
* flush: 是否清除資料流緩衝區, 預設為False (不清除).
'''

# 方式一 (格式話輸出 像C)
a = b = 1
print('%d %d' %(a, b)) # 10進制輸出
print('%.1f %.1f' %(a, b))
'''
還有 %x, %o, %s, %e
'''

# 方式二 f-string (可在 字串中 加入 變數)
a = b = 1
print(f'a={a} , b={b}')
c = 3.1415
print(f'pi = {a:4.2f}') # 設定距離4個字元 並只顯示至 浮點數的第二個小數

```

### input
```python
value = input('prompt: ')
'''
* input會 回傳string型別的值
* 'prompt': 提示字元(自訂)
'''
```


---

## 檔案處理 File processing
```python
file_Obj = open(file, mode="r")
'''
* file: 欲該起檔案
* mode: 開啟模式(同c有: r , w , a , x(開新檔案), rb,wb,ab)
* file_Obj: 檔案物件(名稱自己取)
* 關檔: file_Obj.close()
'''
# 覆蓋寫入
fptr = open('./test.txt', mode='w')
print('hello world ha ha ha', file=fptr)

# 讀取檔案

```



---

## 常用函數
```python
x = 10
id(x) # x的地址
type(x) # x的型別

eval(formula) #直接回傳 算式(字串型別) 的計算結果
abs(x) # 回傳 絕對值
pow(x,y) # 回傳 x 的 y 次方
round(x,y) # 回傳 小數取到第y個 的四捨>4入值(處理位數是偶數則 五捨>5入)

chr(97) # 回傳該 x(97) 的 ascii/unicode 字元(a)
ord('a') # 回傳該 'a' 的 ascii/unicode 碼值(97) 

# 字串 轉成 byte資料
a = b'hello world' 
	#or a = 'hello world'; a = string.encode('utf-8')
print(type(a)) # bytes
# byte資料 轉成 字串
a = b'hello'
a = stringBytes.decode('utf-8')
print(type(a)) # string


```





