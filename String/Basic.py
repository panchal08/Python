str_data = """hello
 hii
 bye
 Noo
"""
print(str_data)

s1 = 'hello python'
print(s1[5:])
print(s1[5::-1])

print(s1)
print(s1.replace('python', 'java'))
print(s1)

print('% s'%s1)
print(dir(s1))


sre1 = 'python is a programming language'
s = sre1.replace('Python', 'Java')
print(s)

s = 'java'
print(sre1.capitalize())
s2 = ''
for item in sorted(s):
    s2 += item
print(s2)

s1 = 'Panchal'
s2 = s1[::-1][::-1]

print(id(s1), s2)
print(id(s2), s2)

print('hello \ world')
print("hello \\n world")
print(' ' == " ")


hey = "hello i am shubham"

print("hello" in hey)