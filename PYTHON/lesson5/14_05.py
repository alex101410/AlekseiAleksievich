eq = input("Please enter the eq:\n")
x = int(input("Please enter the x:\n"))
parts = eq.split('x')
k = int(parts[0].replace('y=',''))
b = int(parts[1])
y = k * x + b
print(eq, x)
print(y)