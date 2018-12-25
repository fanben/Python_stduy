#!/usr/bin/python3
# coding=UTF-8

import random
playerInput = input("请输入（0剪刀 1石头 2布）：")

player = int(playerInput)

mac = random.randint(0,2)

if (player == 0 and mac == 2) or (player == 1 and mac == 0) or (player == 2 and mac == 2):
	print ("您获胜了！")

elif player == mac:
	print("平局，要不要再来一局？")

else:
	print("您输了！")