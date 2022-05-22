moeny = int(input("小明身上有幾元:"))
drink = int(input("販賣機有幾種飲料:"))
answer = 0
for i in range(drink):
    price=int(input("請輸入飲料價格:"))
    if moeny >= price:
        answer += 1
print("可以購買飲料數量為",answer,"種")