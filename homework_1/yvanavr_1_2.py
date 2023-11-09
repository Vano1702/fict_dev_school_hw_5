# A function to calculate the minimal number of moves to win the game "Towers of Hanoi", with given number of disks.
def min_moves(disks):
    res = 2**disks - 1
    return res
    
a = int(input('Enter the number of disks: '))

print(f'Minimum number of moves for {a} disks is {min_moves(a)}')
