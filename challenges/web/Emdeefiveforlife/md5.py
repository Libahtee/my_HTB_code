import requests
import hashlib
import re
req = requests.session()
r = req.get("http://159.65.95.35:31619")
print(r.text)

#pull string from response and get md5 hash
rgxres = re.search("<h3 align=\'center\'>(.*)</h3>", r.text)

print("\n\nRegex output: \n")
plain = rgxres.group(1)
print(plain)

res = hashlib.md5(plain).hexdigest()
print("\n\nmd5 hash:\n")
print(res)

#post hash back to website
payload = {'hash': res}
#dump_var("\n\n"+payload+"\n\n")
r = req.post("http://159.65.95.35:31619", data=payload)
print("\n\nPost response:\n")
print(r.text)
