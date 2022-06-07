def scheck_str(string): 
    lower_case = 0 
    upper_case = 0 
    for letter in string: 
        if letter.isupper(): 
            upper_case += 1 
        elif letter.islower(): 
            lower_case += 1
    print(f"{upper_case} upper case, {lower_case} lower case")
scheck_str("The quick Brown Fox")


def is_prime (number_to_chek):
    for x in range(2, number_to_chek):
        if (number_to_chek % x == 0):
            return False
    return True

print(is_prime(787))
print(is_prime(777))


#3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#отсортированных по возрастанию, и которая этот список “сворачивает”.

#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


#def get_ranges(list):
#    for j[i] in list:
#        if j[i+1] == j+1:
#            list.append(j)
#    print(list)
#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])