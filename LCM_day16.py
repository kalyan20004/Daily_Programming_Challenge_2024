def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(n, m):
    return abs(n * m) // gcd(n, m)


print(lcm(4, 6))            # Output: 12
print(lcm(5, 10))           # Output: 10
print(lcm(7, 3))            # Output: 21
print(lcm(1, 987654321))    # Output: 987654321
print(lcm(123456, 789012))  # Output: 8117355456
