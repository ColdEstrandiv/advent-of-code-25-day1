with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

position = 50
clicks = 0

for l in lines:
    direction = l[0]
    num = int(l[1:])
    digits = num//100
    
    if digits > 0:
        num -= digits * 100
    
    if direction == 'R':
        position += num
        if position > 100: position -= 100
    else:
        position -= num
        if position < -100: position += 100
        if position == 0: clicks += 1

print(clicks)