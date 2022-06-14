def counter(n):
    def bla_bla():
        nonlocal n
        n += 1
        return n
    return bla_bla

f = counter(100)
h = counter(1)
print(f())
print(h())
print(f())
print(h())