# Python note

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