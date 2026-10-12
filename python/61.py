# Program 133: Find GCD of Two Numbers

a = 24
b = 36

while b != 0:
    a, b = b, a % b

print("GCD is:", a)