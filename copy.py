old_file_name = input("请输入要复制的文件名:")

old_file = open(old_file_name,'r')

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

# new_file_name = "[复件]" + old_file_name

new_file = open(new_file_name,'w')

while True:
	content = old_file.read(1024)
	if len(content) == 0:
		break
	new_file.write(content)

old_file.close()

new_file.close()