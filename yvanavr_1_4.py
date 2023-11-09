#A function to determine whether a number is prime or notimport math
def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if number % i == 0:
                return False
    return True
                
        
a = int(input('Enter your number: '))

print(f'{a} is prime: {is_prime(a)}')
