stu = {'name':'Elan','age':13,'sex':'M'}

# 1、增加身高为180

stu['high'] = 180
print (stu)

# 2、修改年龄为25

stu['age'] = 25
print(stu)

# 3、删除身高

del stu['high']
print(stu)

# 4、查询stu的名字
print(stu.get('name'))