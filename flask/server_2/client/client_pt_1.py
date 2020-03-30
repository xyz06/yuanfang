import urllib.request


url = "http://127.0.0.1:5000/"
getup = "?user=xyz&pwd=123"
req = urllib.request.urlopen(url+getup)
data = req.read().decode()
print(data)
