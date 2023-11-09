# A function to rearrange the numbers to get the largest possible number
def exaggerated(number):
    list_of_numbers = list(str(number))
    list_of_numbers.sort(reverse = True)
    res = ''
    for el in list_of_numbers:
        res += el
    return res
    
a = int(input('Enter your number: '))

print(f'Transformed number is {exaggerated(a)}')
