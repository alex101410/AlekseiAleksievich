#try:
#    l = [1,2,3,4,5]
#    l[5]
#    print("try logic goes on")
#except IndexError as e:
#    print(e)


#for i in range(1, 101):
#    if i % 3 == 0:
#        rez += "FIZZ"
#    if i % 5 == 0:
#        rez += "BUZZ"
#print(rez or i)

from cgitb import text
import random

l = [3,5,6,2,3,4,5,6]

def generate_index(n):
    return random.randint(0, n - 1)
        
def swap_items(l):
    n = len(l)
    i = generate_index(n)
    j = generate_index(n)
    j = i
    while i == j:
        j = generate_index(n)
    l[i], l[j] = l[j], l[i]

def is_sorted(l):
    # return l == sorted(l)
    for i in range(len(l)-1):
        if l[i] > l[i + 1]:
            return False
    return True
def sort_by_random(l):
    counter = 0
    while not is_sorted(l):
        swap_items(l)
        counter += 1

    print(counter)

sort_by_random(l)

def show_massage(text):
    print(text)

def calculate_bill(prices, show_func):
    res = sum(prices)
    text = f"It will be {res}"
    show_func(text)

calculate_bill([1123,4564,23], show_massage)

