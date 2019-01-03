import json
import requests

url = 'http://192.168.0.206:8019/eye/rest/library/Test/remote_desktop/getUserInfo'
headers = {'version':'1.0.0'}

i = 1
j = []

while i<=50:
	dic = {'mac':str(i),'uid':'范彭一澜-028:','ip':'192.168.0.96'}
	j.append(dic)
	i+=1
body = {'vm_array':j}

r = requests.get(url,headers=headers,data=json.dumps(body))
r1 = r.text
# print(r1)
f = open('/Users/elanfan/Desktop/华夏视频项目/requests.json','w')
f.write(r1)