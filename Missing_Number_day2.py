def MissingNumber(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

arr = list(map(int, input().split()))
ans = MissingNumber(arr)
print("Missing Number:", ans)