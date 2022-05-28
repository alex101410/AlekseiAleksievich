#x = 0

#while x < 10:
#    print(x)
#    x += 1
#else:
#    print("hello from else")

#print(123)

#l = [1,2,3,4,5,6,7,8,9,10]
#for elem in l:
#    print(elem)

l = [1,-45,3,5,0,4,8,7,9,6,4,3,2]
#M = l[0]
#for i in l:
#    if i < M:
#        M = i
#print(M)
#print(sorted(l))
counter = 0
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            counter += 1
            print(l)

print(l)
print(counter)
