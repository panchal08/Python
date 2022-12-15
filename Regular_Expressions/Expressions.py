import re
count = 0
# # pattern = re.compile("a")
# # matcher = pattern.finditer("Python is a programming Language")
# matcher = re.finditer('[a-z]', 'Python is a programming Language')
# for match in matcher:
#     count += 1
#     print(match.start(), "...", match.end(), "...", match.group())
# print("The number of occurrences: ", count)

s = 'shubahm.panchal1234 @digivalet.com'
print(re.findall('\s', s))
print(re.findall('\S', s))
print(re.findall('\d', s))
print(re.findall('\D', s))
print(re.findall('\w', s))
print(re.findall('\W', s))
print(re.findall('.', s))
print(re.findall('a', s))
print(re.findall('a+', s))
print(re.findall('a*', s))
print(re.findall('a?', s))

import re,urllib
import urllib.request
sites="google rediff hello".split()
print(sites)
for s in sites:
    print("Searching...",s)
    u=urllib.request.urlopen("http://"+s+".com")
    text=u.read()
    title=re.findall("<title>.*</title>", str(text), re.I)
    print(title[0])


import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
print(text)
numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
for n in numbers:
    print(n)