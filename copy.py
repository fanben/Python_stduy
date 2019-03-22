old_file_name = input()

old_file = open(old_file_name,'r')

content = old_file.read()

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

# new_file_name = "[复件]" + old_file_name

new_file = open(new_file_name,'w')

new_file.write(content)

old_file.close()

new_file.close()