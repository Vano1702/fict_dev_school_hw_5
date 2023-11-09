# A function to pick up undamaged packages of sausages and carefully lay them out on the counter
def unpack(truck):
    counter = ''
    fee = 0
    for box in truck:
        for pack in box:
            if len(pack) == 6 and pack[0] == '[' and pack[-1] == ']':
                flag = 1
                for i in range(2, 5):
                    if pack[i] != pack[i-1]:
                        flag = 0
                if flag:
                    if fee != 4:
                        counter += (pack[1] + ' ') * 4
                        fee += 1
                    else:
                        fee = 0
    return counter.rstrip()

a = [ [ "(-)", "[IIII]", "[))))]" ], [ "IuI", "[llll]" ], [ "[@@@@]", "UwU", "[IlII]" ], [ "IuI", "[))))]", "x" ], [] ]
print(unpack(a))
