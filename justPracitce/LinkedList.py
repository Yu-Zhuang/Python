
class link:
	def __init__(self, element):
		self.val = element
		self.next = None
	def add(self, element):
		tmp = self
		while(tmp.next != None):
			tmp = tmp.next
		tmp.next = link(element)

	def show(self):
		tmp = self
		while(tmp.next != None):
			print(f'[{tmp.next.val}]-', end='')
			tmp = tmp.next
		print('|END')

head = link('head')
for i in range(1,20,2):
	head.add(i)
head.show()
