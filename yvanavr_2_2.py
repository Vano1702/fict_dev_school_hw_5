# A function to find the index where the sum of the integers is on the left is equal to the sum of the integers to the right
def equal_sums(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1

a = [20, 10, -80, 10, 10, 15, 35]
print(equal_sums(a))
