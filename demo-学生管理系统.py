def starLine():
	print("*"*30)

def selectedKey():
	key = input("输入选择的功能(序号)：")
	return key

def showSelectedInfo():
	print("="*30)
	print("     学生管理系统   V1.0")
	print("1.新增学生信息")
	print("2.修改学生信息")
	print("3.删除学生信息")
	print("4.查询学生信息")
	print("5.查看所有学生信息")
	print("6.退出系统")
	print("="*30)

def addNewStu(StuTemp):
	starLine()
	Stu = {}
	Stu['name'] = input("请输入学生姓名：")
	Stu['id'] = input("请输入学生学号：")
	Stu['age'] = input("请输入学生年龄：")
	StuTemp.append(Stu)
	starLine()

def modStuInfo(delStudent):
	starLine()
	num = int(input("请输入要修改学生信息的编号："))
	num1 = num - 1
	delStudent[num1]['name'] = input("姓名：")
	delStudent[num1]['id'] = input("学号：")
	delStudent[num1]['age'] = input("年龄：")
	print("修改成功！")
	starLine()

def findStuInfo(delStudent):
	starLine()
	num = int(input("请输入要查询学生信息的编号："))
	num1 = num - 1
	print("编号：%d 姓名：%s 学号：%s 年龄：%s"%(num,delStudent[num1].get('name'),delStudent[num1].get('id'),delStudent[num1].get('age')))

def delStuInfo(delStudent):
	starLine()
	num = int(input("请输入要删除学生信息的编号："))
	num1 = num - 1
	del delStudent[num1]

def ShowAllStuInfo():
	starLine()
	for i,temp in enumerate(StuInfo):
		print("序号：%s 姓名：%s"%(i+1,temp['name']))
	starLine()

def quitSys():
	quit = input("是否确定退出系统？(yes or no):")
	return quit


StuInfo = []
while True:
	showSelectedInfo()
	key = selectedKey()

	if key == '1':
		addNewStu(StuInfo)
	elif key == '2':
		modStuInfo(StuInfo)
	elif key == '3':
		delStuInfo(StuInfo)
	elif key == '4':
		findStuInfo(StuInfo)
	elif key == '5':
		ShowAllStuInfo()
	elif key == '6':
		quit = quitSys()
		if quit == 'yes':
			break
	else:
		starLine()
		print("输入有误，请重新输入！")
		starLine()