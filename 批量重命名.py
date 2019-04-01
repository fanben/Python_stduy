import os 

# 1、获取要重命名文件，文件夹的名字
folder_name = input("请输入文件夹名字：")

# 2、获取该文件夹中所有文件的名字
file_names = os.listdir(folder_name)

# os.chdir(folder_name)

# 3、重命名
for name in file_names:
	print(name)

	old_file_name = folder_name + "/" +name
	new_file_name = folder_name + "/" + "[Fan]-" +name
	os.rename(old_file_name, new_file_name)
