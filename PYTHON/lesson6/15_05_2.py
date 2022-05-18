l = [1, 1, "test", 2, 2, 2, 2, 2, 3, 4, 5] + list("hello")
print(l)
l = list(set(l))
print(l)

x = [1,3,2]
y = [1,2,3]
print(x == y)
print(set(x) == set(y))

x = {1,2,3,4,5}
y = {3,4,5,6,7}
print(x.intersection(y))
print(x.union(y))