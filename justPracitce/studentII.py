# ********* IMPORT *********
import random
from typing import List

# ********* CLASS and FUNCTION **********
class Student:
    def __init__(self, id_, cs, pgm):
        self.id = id_
        self.cs = cs
        self.pgm = pgm
        self.avr = float( (cs+pgm)/2 )
    def show(self):
        print(f'{self.id}\t{self.cs}\t{self.pgm}\t{self.avr}')

def class_init(clas: List[int], num: int) -> None:
    for i in range(num):
        newst = Student(id_=i+106711101, cs=random.randint(0,100), pgm=random.randint(0,100))
        clas.append(newst)

def class_show(clas: List[int]) -> None:
    print('[學號]\t\t[計概]\t[程規]\t[平均]')
    for i in clas:
        i.show()

def class_sort(clas: List[int], chose: int) -> None:
    for i in range(len(clas)-1):
        for j in range(i,len(clas)):
            if(clas[i].cs < clas[j].cs and chose is 1):
                clas[i], clas[j] = clas[j], clas[i]
            if(clas[i].pgm < clas[j].pgm and chose is 2):
                clas[i], clas[j] = clas[j], clas[i]
            if(clas[i].avr < clas[j].avr and chose is 3):
                clas[i], clas[j] = clas[j], clas[i]


# ********* MAIN **********
clas = []
chose = 1

class_init( clas, int( input('請輸入幾個學生: ') ) )
class_show(clas)

while(chose is not 0):
    chose = int( input('\t@主選單@\n(1)依計概成績排名\n(2)依程規成績排名\n(3)依平均排名\n(0)結束\n請輸入選擇: ') )
    if chose > 0 and chose < 4:
        class_sort(clas, chose)
        class_show(clas)
    elif chose is not 0:
        print('\t error: 輸入錯誤!')

# ********* END **********
print('\t[ 程式結束 ]')

