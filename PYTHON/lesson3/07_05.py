#x = input("please enter")
#print(x)

#x = 3 / True 
#print(x)

#x = 3 - 1
#if x == 1:
#    print(x)
#elif x == 2:
#    print(2)
#else:
#    print(0)



a = int(input("please enter a"))
b = int(input("please enter b"))
c = int(input("please enter c"))
d = b ** 2 - 4 * a * c
print("d = ", d)
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
elif d == 0:
    x1 = -b / 2 * a
    print("x1 = ", x1)
else:
    print("no roots")