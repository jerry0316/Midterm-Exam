num=int(input("請輸入一正整數:"))
if num>=11 and num<=1000:
    if num%2==0 and num%11==0 and num%5!=0 and num%7!=0:
        print(num,"為新公倍數?:Yes")
    else:
        print(num,"為新公倍數?:No")
else:
    print("輸入數字範圍需介於11~~1000")