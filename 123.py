import time

# for i in range(10):
# 	list01 = [ "\\","|","/","-"]
# 	# index = i%4
# 	# print ('\r操作成功！请稍等{}'.format(list01[index]),end='')
# 	print("\r[{}]{}%".format("■"*(i+1),int(i+1)*10),end="")
# 	time.sleep(0.25)

class test():
	def __init__(self):
		self.book = [1,2,3,4,5]
		self.index = -1

	# def __len__(self):
	# 	return len(self.book)

	def __getitem__(self,i):
		return self.book[i]

	# def __iter__(self): #返回的是一个可迭代对象，使得这个类成为一个可迭代对象，但要想让这个可迭代对象能通过for去循环遍历，必须和__next__函数一起实现
	# 	return self

	# def __next__(self): # 如果单独实现__next__，则是能通过next()调用，不能使用for循环遍历
	# 	self.index += 1
	# 	if self.index > len(self.book)-1:
	# 		raise StopIteration('索引越界！！！')
	# 	return self.book[self.index]

from random import choice
t = test()
# print(choice(t))
# print(len(t))
for i in t:
	print(i)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

from collections import Counter

print(Counter('aabbcddddeeeee')) # 统计序列中的频度==> Counter({'e': 5, 'd': 4, 'a': 2, 'b': 2, 'c': 1})
print(dict(Counter('aabbcddddeeeee')))  # ==> {'a': 2, 'b': 2, 'c': 1, 'd': 4, 'e': 5}