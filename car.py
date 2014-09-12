class Car():

	def __init__(self,x,y,length, direction, name):
		self.x = x
		self.y = y
		self.length  = length
		self.direction = direction
		self.name = name

	def update_pos(self,x,y):
		self.x = x
		self.y = y