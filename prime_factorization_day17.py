def prime_factorization(N):
    factors = []
    divisor = 2
    while N > 1:
        while N % divisor == 0:
            factors.append(divisor)
            N //= divisor
        divisor += 1
        if divisor ** 2 > N:
            if N > 1:
                factors.append(N)
            break
    return factors

# Test cases
print(prime_factorization(18))    # Output: [2, 3, 3]
print(prime_factorization(30))    # Output: [2, 3, 5]
print(prime_factorization(49))    # Output: [7, 7]
print(prime_factorization(19))    # Output: [19]
print(prime_factorization(64))    # Output: [2, 2, 2, 2, 2, 2]
print(prime_factorization(123456))  # Output: [2, 2, 2, 2, 2, 2, 3, 643]
