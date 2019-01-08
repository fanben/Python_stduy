def printLine():
	print("-"*30)

def printLine_2(n):
	i = 0
	while i<n:
		printLine()
		i+=1

num = int(input("请输入循环次数："))
printLine_2(num)