def sorting_into_two_arrays(arr1,arr2):
    arr1.sort()
    arr2.sort()
    while(arr1[-1]>arr2[0]):
        arr1[-1],arr2[0] = arr2[0],arr1[-1]
        arr1.sort()
        arr2.sort()
    return arr1,arr2
print("Enter 1st array")
arr1 = list(map(int, input().split(",")))
print("Enter 2nd array")
arr2 = list(map(int, input().split(",")))
sorting_into_two_arrays(arr1,arr2)
print(arr1)
print(arr2)