class SweetPotato:

	def __init__(self):
		self.cookLevel = 0
		self.cookString = '生的'
		self.condiments = []

	def __str__(self):

		msg = '当前状态为:'+self.cookString
		if len(self.condiments)>0:
			msg += '; 添加的佐料为:'
			for x in self.condiments:
				msg = msg + x +','

		msg = msg.strip(',')
		return msg

	def cook(self,time):
		self.cookLevel += time
		if self.cookLevel > 8:
			self.cookString = '烤焦了'
		elif self.cookLevel > 5:
			self.cookString = '熟了'
		elif self.cookLevel > 3:
			self.cookString = '半生不熟'
		else :
			self.cookString = '生的'

	def addCondiments(self,temp):
		self.condiments.append(temp)

digua = SweetPotato()
print(digua)

print('='*40)

print('首先开始烤2分钟，并加入番茄酱')
digua.cook(2)
digua.addCondiments('番茄酱')
print(digua)

print('再烤4分钟，加入胡椒粉')
digua.cook(2)
digua.addCondiments('胡椒粉')
print(digua)

print('最后再烤2分钟')
digua.cook(2)
print(digua)

print('='*40)
print('美味地瓜完成了')