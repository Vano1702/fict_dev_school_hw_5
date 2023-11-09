# A function to find the smallest and largest number in a string
def highAndLow(numbers):
    list_of_numbers = list(map(int, numbers.split()))
    num_max = str(max(list_of_numbers))
    num_min = str(min(list_of_numbers))
    res = num_max + " " + num_min
    return res
    
a = input('Enter your numbers: ')

print(f'The largest and smallest numbers of {a} are {highAndLow(a)}')
