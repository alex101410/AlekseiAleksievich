#l = [1,2,3,4,5,6]

#def sum(l, i=0):
#    if i == len(l):
#        return
#    print(l[i])
#    sum(l, i+1)

#sum(l)

#def search(l, x, low, high):
#    m = (low+high)//2
#    if l[m] == x:
#        return m
#    elif l[m] > x:
#        return search(l, x, low, high)
#    low = 0
#    high = len(l)-1
#    while low <= high:
#        mid = (low + high)
#        guess = list[mid]
#        if guess == x:
#            return mid
#        if guess > x:
#            high = mid - 1
#        else:
#            low = mid + 1
#    return None

#l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#print(search(l, 3))

#print(list(filter(lambda x : x// 10, l)))

m = ['1', '11', '12', '22', '2', '13', '30', '33']

print(sorted(filter(lambda x: int(x) % 2 == 0, m), key=lambda x: int(x)))


#print(sorted(filter(lambda x: x % 2, [int(x) for x in l]))) но я не могу догнать как список строк вывести