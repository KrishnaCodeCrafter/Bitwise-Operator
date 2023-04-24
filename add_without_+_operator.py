a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
# Method 1
def add_without_plus_M1(a,b):
    while b!=0:
        k = a & b
        a = a ^ b
        b = k << 1
    return a
result = add_without_plus_M1(a,b)
print(result)

