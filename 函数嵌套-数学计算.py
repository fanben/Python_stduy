def addNum(a,b,c):
	sum = a+b+c
	return sum

def average3Num(a,b,c):
	average = addNum(a,b,c) / 3
	return average

result = average3Num(1,2,3)
print(result)