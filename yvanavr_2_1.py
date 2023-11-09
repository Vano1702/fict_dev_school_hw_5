# A function that selects leaders by maximum honor and returns it
def max_honor(honor, leaders):
    n = int(len(honor)/leaders)
    sums = []

    for i in range(n):
        current_sum = 0
        for j in range(i, len(honor), n):
            current_sum += honor[j]
        sums.append(current_sum)

    return max(sums)


a = [1, 5, 6, 3, 4, 2]
b = 3

print(max_honor(a, b))
