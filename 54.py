from decimal import ROUND_UP
import math
km = float(input("請輸入路程公里數(km)："))
price = 75
if km > 1.5:
    money= (km-1.5)*1000/250
    money2=math.ceil(money)
    price += int(money2*5)
print("所需車資為"+str(price))
