time = int(input("搭了幾次電梯:"))
floor = 1
price = 0
for i in range(time):
    floor2 = int(input("請輸入搭到幾樓:"))
    if floor2 > floor:
        price += (floor2-floor)*20
    elif floor2 < floor:
        price += (floor-floor2)*10
    floor = floor2
print(price,"元")