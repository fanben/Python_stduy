#!/usr/bin/python3
# coding=UTF-8

usrname = "elan"
password = "298312"

usrInput = input("请输入账号:")
usr = string(usrInput)

pswInput = input("请输入密码:")
psw = string(pswInput)

if (usr == usrname and psw == password):
	print("登录成功!")
else:
	print("登录失败!")
