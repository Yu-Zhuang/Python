# Python Note

## Plot Chart
* 折線圖 plot
```python
import matplotlib.pyplot as plt
y1 = [1,4,9,16,25] # y axis
y2 = [1,9,81,72,83] 
x = [1,2,3,4,5] # x axis
plt.plot(x, y1, '-*', label='y1') # line 1, form, label
plt.plot(x, y2, '-o', label='y2')
plt.title('test chart') # title of chart
plt.xlabel('group') # title of axis
plt.ylabel('value')
plt.legend(loc='best') # 圖例
plt.xticks(x) # x軸設定成自訂刻度
plt.savefig('fin1.pdf', bbox_inches='tight') # 儲存檔案 as pdf
plt.show() #顯示圖片
```

* 點圖 scatter
```python
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,4,5,6]
plt.scatter(x,y)
plt.show()

x = list(range(1,100))
y = [x**2 for x in x]
plt.scatter(x,y,color='y') #設定顏色
plt.show()
```
* 長條圖 bar chart
```python
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,4,5,6]

plt.bar(x,y)
plt.show()
````

* Numpy 模組
