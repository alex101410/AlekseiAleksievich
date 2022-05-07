d = int(input("Enter the deposit amount, BYN\n"))
n = int(input("Enter bank interest rate, %\n"))
t = int(input("Enter term of deposit, years\n"))
print(" 1 daily capitalization\n 2 monthly capitalization\n 3 quarterly capitalization")
print(" 4 semi-annual capitalization\n 5 annual capitalization")
periods = int(input("Choose one of the capitalization periods: 1, 2, 3, 4 or 5\n"))
if periods == 1:
    p = 365
elif periods == 2:
    p = 12
elif periods == 3:
    p = 4
elif periods == 4:
    p = 2
elif periods == 5:
    p = 1
else:
    print("You have a one-time capitalization.")
    p = 1/t
s = round(d * (1 + n/100/p) ** (t * p))
print("The amount in the account at the end of the period will be", s, "BYN")