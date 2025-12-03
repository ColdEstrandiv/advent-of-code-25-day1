with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

position = 50
clicks = 0

for l in lines:
    direction = l[0]
    num = int(l[1:])
    digits = num//100

    
    if digits > 0:
        clicks += digits
        num -= digits * 100
    
    if direction == 'R':
        
        if position + num >= 101 : clicks += 1
        
        position += num
        
        if position > 99: 
            position -= 100

    else:
        
        if position < num and position!=0: clicks += 1
        position -= num
        
        if position < -99: 
            position += 100

    if position < 0: position += 100
    if position == 0: clicks += 1
    # print(position,clicks)
print(clicks)
