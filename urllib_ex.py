import urllib.request, urllib.parse

url = "http://python.org/"
url1 = 'http://docs.python.org/fahim/tutorial/interpreter.html'
url2 = 'http://docs.python.org/tutorial/'
response =urllib.request.urlopen(url2)

print(response.headers['Date'])
print('----')
print(response.geturl())
print('----')

# Write a program wget.py to download a given URL. 
# The program should accept a URL as argument, 
# download it and save it with the basename of the URL. 
# If the URL ends with a /, consider the basename as index.html.
def wget(url):
    filepath = urllib.parse.urlsplit(url).path.split('/')[-1]
    if filepath == '':
        filepath = 'index.html'
    urllib.request.urlretrieve(url,filepath)
#wget(url2)

