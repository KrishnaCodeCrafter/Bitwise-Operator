a = int(input())
b = int(input())
# Method 1
def add_without_plus_M1(a,b):
    while b!=0:
        k = a & b
        a = a ^ b
        b = k << 1
    return a
result = add_without_plus_M1(a,b)
print(result)

# Method 2
def add_without_plus_M2(a,b):
    result = (a*a - b*b)/(a - b)
    return result
result = add_without_plus_M2(a,b)
print(int(result))
