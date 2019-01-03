#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests



url = 'http://192.168.0.96:8019/eye/rest/library/Test/remote_desktop/getUserInfo'
headers = {'version':'1.0.0'}
body = {    "vm_array": 
      	[
        {
          "uid":"范彭一澜-028:",
          "ip":"192.168.0.51",
          "mac":"11-11-11-11-11-11"
        }
        ]
       }
r = requests.get(url,headers=headers,data = json.dumps(body))

print(r.text)


