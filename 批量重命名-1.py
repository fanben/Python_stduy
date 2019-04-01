import os 

folder_name = input("请输入文件夹名字：")

file_names = os.listdir(folder_name)

os.chdir(folder_name)

for name in file_names:
	print(name)
	os.rename(name, "[Elan]-"+name)