i = " I am learning Python. hello, WORLD!"
a = i[:i.find('h')]
b = i[i.find('h'):i.rfind('h') + 1]
c = i[i.rfind('h') + 1:]

print(a + b[::-1] + c)