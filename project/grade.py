import random

class Student(object):
	def __init__(self, id_, cs, pgm):
		self.id = id_
		self.cs = cs
		self.pgm = pgm
		self.avr = float((cs+pgm)/2)
	def show(self):
		print(f'{self.id}\t{self.cs}\t{self.pgm}\t{self.avr:.2f}')

def class_init(list_):
	for i in range(100):
		newst = Student(103000001+i, random.randint(0,100), random.randint(0,100))
		list_.append(newst)
def class_print(list_):
	for i in list_:
		i.show()

def class_find_MinMax(list_):
	cs_max, pgm_max, avr_max = list_[0].cs, list_[0].pgm, list_[0].avr
	cs, pgm, avr = [], [], []
	for i in list_:
		if (cs_max < i.cs):
			cs_max = i.cs
			cs = []
		if (cs_max == i.cs):
			cs.append(i.id)

		if (pgm_max < i.pgm):
			pgm_max = i.pgm
			pgm = []
		if (pgm_max == i.pgm):
			pgm.append(i.id)

		if (avr_max < i.avr):
			avr_max = i.avr
			avr = []
		if (avr_max == i.avr):
			avr.append(i.id)

	return cs, pgm, avr


# ============== MAIN ==============
class_list = []
title = '[學號]\t\t[計概]\t[程規]\t[平均]'

print(title)
class_init(class_list)
class_print(class_list)
seq_cs , seq_pgm, seq_avr = class_find_MinMax(class_list)

print(f'計概最高分同學:\t{seq_cs}')
print(f'程規最高分同學:\t{seq_pgm}')
print(f'平均最高分同學:\t{seq_avr}')


