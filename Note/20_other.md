# Python Note

## 其他常用函數
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

len(list_1) # 取得 該物 長度大小

# 同行輸入多個元素 (會回傳 串列)
newst = input('請依序輸入 學號 名稱 成績: ').split()
# 也可以 input().split(',') (以,分割
```

