a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []
c = []
for y in a:
    if y not in b:
        b.append(y)
        c.append(y)
    else:
        if y in c:
            i = c.index(y)
            del c[i]
print(*c)