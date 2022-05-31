a = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
dic = a.split()
#print(dic[0])


dic_translet = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, 
                "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, 
                "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, 
                "nineteen":19, "twenty":20}
data = []
i = 0
data
for dic[i] in dic_translet:
    data.append(dic_translet[dic[i]])
    i += 1


print(data)



#data = list(set(data))

#data = ["five thirteen two eleven seventeen two one thirteen ten four eight five nineteen", {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,
#                'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
#                'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
#                'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}, '']


#print('1. transform text to number\n')

#data = [data[1][data[2]] for data[2] in data[0].split()]
#print(data)

#print('\n2. 3. delete dublicate and sort list\n')

#    if data[1] % 2 != 0:
#        print(f'{data[0][data[1]]} + {data[0][data[1] + 1]} = {data[0][data[1]] + data[0][data[1] + 1]}')
#    if data[1] % 2 == 0:
#        print(f'{data[0][data[1]]} * {data[0][data[1] + 1]} = {data[0][data[1]] + data[0][data[1] + 1]}')

#print('\n5. sum odd elements\n')

#print(sum(data for data in data if data % 2 != 0))