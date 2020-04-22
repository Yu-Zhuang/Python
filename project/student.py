import random
# ******* define *********
	#student object
class student(object):
	def __init__(self, _id, name, grade):
		self.id = _id
		self.name = name
		self.grade = grade
	def printStudent(self):
		print(f'{self.id}\t{self.name}\t{self.grade}')
	#function print
def class_print(class_list, st_num):
	print('[學號]\t\t[姓名]\t[成績]')
	for i in range(st_num):
		class_list[i].printStudent()
	#function find
def class_find(class_list, st_num, target):
	for i in range(st_num):
		if class_list[i].id == target:
			class_list[i].printStudent()
			return i
	print("\t[Not Find !]")
	return False
	#function add	
def class_add(class_list, newst):
	newst = student(newst[0],newst[1],newst[2])
	class_list.append(newst)

def class_edit(target, newdt):
	target.id = newdt[0]
	target.name = newdt[1]
	target.grade = newdt[2]

def class_delete(class_list, target):
	class_list.remove(target)

# ********* MAIN **********
st_list = []
st_num = 10
chose = 1
	# initialize class student data
for i in range(st_num):
	newst = student(f'{i+106711101}', f'st_{i+1}', random.randint(0,100))
	st_list.append(newst)

	# 主選單
while chose!=0:
	chose = int( input('\n\t@主選單@\n(1)查詢學生\n(2)新增學生\n(3)編輯學生\n(4)刪除學生\n(5)印出班級\n(0)結束\n請輸入: ') )
	if chose==0: # 結束
		break
		# 查詢
	elif chose==1: 
		target = input('欲找學生學號: ')
		class_find(st_list, st_num, target)
		# 新增
	elif chose==2: 
		newst = input('請依序輸入 學號 名稱 成績: ').split()
		if class_find(st_list, st_num, newst[0])==False:
			class_add(st_list, newst)
			st_num+=1
		else:
			print('\t [此學生已存在]')
		# 編輯
	elif chose==3: 
		_id = input('依序輸入欲編輯學生 學號 新姓名 新成績: ').split(' ')
		ot = class_find(st_list, st_num, _id[0])
		if ot!=False:
			class_edit(st_list[ot], _id)
		else:
			print('\t [無此學生]')
		# 刪除
	elif chose==4:
		_id = input('依序輸入欲刪除學生學號: ')
		ot = class_find(st_list, st_num, _id)
		if ot!=False:
			class_delete(st_list, st_list[ot])
			st_num-=1
		else:
			print('\t [無此學生]')
		# 印出班級
	elif chose==5:
		class_print(st_list, st_num)
	
	# END
print('\t[ 程式結束 ]')

