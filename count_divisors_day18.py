def count_divisors(N):
    divisor_count = 0
    sqrt_N = int(N ** 0.5)

    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            divisor_count += 2  
        if i * i == N: 
            divisor_count -= 1
    
    return divisor_count

# Test cases
print(count_divisors(12))   # Output: 6
print(count_divisors(18))   # Output: 6
print(count_divisors(29))   # Output: 2
print(count_divisors(100))  # Output: 9
print(count_divisors(1))    # Output: 1
print(count_divisors(997))  # Output: 2
