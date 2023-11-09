# A function to find the number of cubes needed to build a tower of a given volume
def findNb(m):
    vol = 0 #current volume
    n = 1 #number of cubes
    while vol < m:
        vol += n ** 3
        if vol == m:
            return n
        n += 1
    return -1
    
a = int(input('Enter the total volume: '))

print(findNb(a))
