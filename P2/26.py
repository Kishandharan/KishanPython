from requests import get
api = "https://api.ipify.org"
#way 1
ip = get(api).content.decode("utf8")
print(ip)

#way 2
ip = get(api).text
print(ip)