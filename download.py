import requests

x = input("Enter URL of the file that you want to download? ")
r = requests.get(x)
print("Status Code:", r.status_code)
print("File is downloading [#      ]")
f = open("output.bytes", "wb")
c = r.content
f.write(c)
f.close()
print("File is downloading [#######]")
