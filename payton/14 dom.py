t = 0

def outer(a, b, c):
    def inner(i, j):
        return i * j
    global t
    t = 2 * (inner(a, b) + inner(a, c) + inner(b, c))

outer(2, 4, 6)
print(t)
outer(5, 8, 2)
print(t)
outer(1, 6, 8)
print(t)

def outer(a, b, c):
    w = 0
    def inner(i, j):
       nonlocal w
       w += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)
    return 2 * w

print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))
