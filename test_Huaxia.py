#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests

i = 1

while i <= 200:

	url = 'http://localhost:7999/rest/personnels'
	headers = {'timeout':'5'}
	r = requests.get(url,headers=headers)

	r1 =  r.text

	f = open('C:/Users/Tcsy/Desktop/Test/'+str(i)+'.json','w')
	f.write(r1)
	i += 1


