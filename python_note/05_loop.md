# Python Note

## 迴圈
```python
# itertable object ( list, tuple, dictionary, string)
x = [3,5,7]
for i in x: print(i) # 3, 5, 7

# for i in range(n)
# for i in range(start:end)
# for i in range(start:end:step)

# 串列 產生
x = list(range(6))
print(x) # [0, 1, 2, 3, 4, 5]

# enumerate() 使用
# enumerate(逸代物件) 會回傳 該逸代物件的 (index,value)
record = [32,43,56,87,90]
for count, score in enumerate(record):
	print('場次: %d; 得分: %d' %(count,score) )
'''
場次: 0; 得分: 32
場次: 1; 得分: 43
場次: 2; 得分: 56
場次: 3; 得分: 87
場次: 4; 得分: 90
'''

```