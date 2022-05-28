# сортировка выбором
l = [1,45,3,5,0,4,8,7,9,6,2]
counter = 0
print(l)
for i in range(len(l)):
    m = i
    for k in range(i, len(l)):
        if l[k] < l[m]:
            m = k
#    if m == i:
    l[i], l[m] = l[m], l[i]
    counter += 1
#            print(l)

print(l)
print(counter)