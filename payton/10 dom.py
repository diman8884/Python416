from random import randint

def ran(a, b):
    return tuple(randint(a, b) for i in range(10))

tpl1 = ran(0, 5)
print(tpl1)
tpl2 = ran(-5, 0)
print(tpl2)

tp3 =tpl1 + tpl2
print(tp3)
print("0 =", tp3.count(0))