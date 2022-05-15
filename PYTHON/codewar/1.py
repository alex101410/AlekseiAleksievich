m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
positiv = [i for i in m if i > 0]
negativ = [i for i in m if i < 0]
m1 = [len(positiv), sum(negativ)]
print(m1)
#[i] in m > 0
#del m[i]
#print(m)
