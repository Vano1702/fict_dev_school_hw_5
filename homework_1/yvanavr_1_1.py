# A function for calculating the sum of numbers that are multiples of 3 or 5, which are smaller than the specified value
def sum_3_5(value):
    if value > 0:
        res = sum([x for x in range(value) if x % 3 == 0 or x % 5 == 0])
        return (res)
    else:
        return 0

a = int(input('Enter the number: '))

print(f'The sum of numbers that are multiples of 3 or 5, which are smaller than {a} is {sum_3_5(a)}')
