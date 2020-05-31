
class Tree:
	def __init__(self, element):
		self.val = element
		self.left = None
		self.right = None
		
	def add(self, element):
		tmp = self
		while(True):
			if(element > tmp.val):
				if(tmp.right == None):
					tmp.right = Tree(element)
					break
				tmp = tmp.right
			elif(element < tmp.val):
				if(tmp.left == None):
					tmp.left = Tree(element)
					break
				tmp = tmp.left
			else:
				print('element already exist')
				break

	def show(self, root):
		if(root != None):
			root.show(root.left)
			print(f'[{root.val}]-', end='')
			root.show(root.right)

head = Tree(10)
for i in range(1,20,2):
	head.add(i)
head.show(head)
