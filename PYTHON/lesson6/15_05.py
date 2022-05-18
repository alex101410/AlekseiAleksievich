from re import S


s = {1,2,3,4,5,6}
print(s)
s1 = {1, "tese", (1,2,3)}
print(s1)
#s2 = {} error  
#print(type(s2), s2)
s.add(8)
s.update("test")
s.discard(4)
s.remove(2)
#s.remove(9) error
print(s)
#if 3 in S:
print(s.pop())
print(s)
