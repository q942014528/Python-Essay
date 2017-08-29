#coding=utf-8
import random
import time
class guess():
	def __init__(self):
		self.num = str(random.randint(1000,9999))
		
		while True:
			self.list1 = []
			self.list2 = []
			self.cs = 0
			self.newnums = 1
			for i in self.num:
				self.list1.append(i)
			for i in self.list1:
				if i not in self.list2:
					self.list2.append(i)

			if len(self.list2) == 4:
				break
			else:
				self.num = str(random.randint(1000,9999))



			# for i in self.num:
			# 	print i
			# 	if i == self.num[0]:
			# 		if i == self.num[4-1] or i== self.num[3-1] or i == self.num[2-1]:
			# 			print'--------'
			# 			self.num = str(random.randint(1000,9999))
			# 			self.cs +=1
			# 			break
 		# 		if i == self.num[0]:
 		# 			kk
 		# 		if i == self.num[0]:








		self.times = 15
		
		self.newTimes = 1

	# def userinput(self):
		
		
	# 	self.marry()
	def marry(self):
		print('-----------猜数字游戏-----------')
		while self.times>=self.newTimes:
			self.list3 = []
			self.list4 = []
			self.B = 0
			self.A = 0
			self.ints=0
			self.temp = input('请输入')
			self.temp = str(self.temp)
			
			 
			for i in self.temp:
				self.list3.append(i)
			for i in self.list3:
				
				if i not in self.list4:
					self.list4.append(i)
				# else:
				# 	self.list4.append('a')

			if len(self.list4)==4:
				self.forsin()
			else:
				print('Invalid input!,')


			print ('A'*self.A+'B'*self.B)
			if self.temp == self.num:
				print('正确')
			if self.A == 4:
				print
				return
			
			if self.times-self.newTimes == 1:
				print('最后一次机会')
			self.newTimes +=1
		answer = raw_input('请输入good获取答案')
		if answer == 'good':
			print(self.num)
	def forsin(self):
		for i in self.list4:
			if i in self.num:
				self.B+=1
				if str(i) == self.num[self.ints]:
					# print self.num[self.ints] 
					self.A +=1
					self.B -=1
					
			self.ints+=1


if __name__ == '__main__':
	gue = guess()
	gue.marry()