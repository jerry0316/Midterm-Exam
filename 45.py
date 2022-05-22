month=int(input("請輸入出生月份"))
date=int(input("請輸入出生日期"))
s=(month*2+date)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
else:
    print("大吉")