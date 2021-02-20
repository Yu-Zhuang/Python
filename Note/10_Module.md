# Python Note

## Module (模組)
* 分類:
	1. 自訂模組
	2. 內建模組
	3. 外部模組
* 自訂模組
```python
# 檔案: SayHi.py
def Hi():
	print('Hi im Hi()')
def Hello():
	print('Hello im Hello()')

# 檔案: main.py
import SayHi #引入自訂模組
SayHi.Hi() #使用模組中函數
SayHi.Hello()

# 檔案: main.py, 導入模組內的函數
from SayHi import Hi, Hello #引入模組內的函數
Hi() #使用模組中函數
Hello()

# 檔案: main.py, 導入模組內所有函數
from SayHi import * #引入模組內所有函數
Hi() #使用模組中函數
Hello()

# as使用
import SayHi as SH #引入模組 並名為SH
SH.Hi() #使用模組中函數
SH.Hello()

from SayHi import Hello as HL
HL()

# 亦可以應用在 引入 模組中的 類別
```

* 內建模組
```python
# random 模組
import random
	# .randint()
x = random.randint(1,100) # rand範圍會是整數 1~100
print(x) 
	# .choice
data = ['kk', 'gg','jj']
print( random.choice(data) ) # rand串列中 隨機一個元素
	# .shuffle()
poker = [1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(poker)
print(poker) # 將 串列 次序打亂
	# .uniform() 
print( random.uniform(1,10) ) # 回傳 隨機浮點數 範圍是1~10

# time 模組
import time
	# .time()
print('1970年1月1日 至 現在 以來的秒數: %d' %int(time.time()) )
	# .sleep() #延遲 以秒為單位
x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
	print(i)
	time.sleep(1) # 延遲1秒鐘
	# .asctime()
print(time.asctime()) #顯示 目前時間
	# localtime() #顯示 目前時間的結構資料
x = time.localtime()
print(x) #time.struct_time(tm_year=2020, tm_mon=4, tm_mday=30, tm_hour=14, tm_min=52, tm_sec=10, tm_wday=3, tm_yday=121, tm_isdst=0)


# sys模組
import sys
	# .version
print('目前python版本是: ', sys.version)# 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) [Clang 6.0 (clang-600.0.57)]
print('目前python版本是: ', sys.version_info)# sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)

	# .stdin / .stdout
print('enter something: ')
x = sys.stdin.readline() 
sys.stdout.write(x)
	# .platform
print( sys.platform ) #傳回目前python3的使用平台
	# .path
print( sys.path ) # 回傳電腦目前環境變數path的值
	# .executable
print( sys.executable ) # 傳回目前python可執行檔案路徑
	# .argv 
print( sys.argv ) # 會回傳命令列的引數

# calendar 模組
import calendar
	# .isleap() 判斷是否是閏年
print( calendar.isleap(2020) ) #會是 True or False
	# .month()
print( calendar.month(2020,4) ) # 印出月曆
	# .calendar()
print( calendar.calendar(2020) ) #印出 年曆
```








