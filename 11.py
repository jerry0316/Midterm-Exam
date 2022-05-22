#                  摩羯座       射手座       水瓶座      雙魚座    牡羊座   金牛座    雙子座    巨蟹座    獅子座  處女座    天秤座   天蠍座
constellation=["Capricornus","Sagittarius","Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio" ]
month=int(input("請輸入出生月份:"))
day=int(input("請輸入出生日期:"))
if month==1:
    if day<20:
        print("星座為:",constellation[0])
    else:
        print("星座為:",constellation[2])
elif month==2: 
    if day<19:
        print("星座為:",constellation[2])
    else:
        print("星座為:",constellation[3])
elif month==3:
    if day<20:
        print("星座為:",constellation[3])
    else:
        print("星座為:",constellation[4])
elif month==4:
    if day<20:
        print("星座為:",constellation[4])
    else:
        print("星座為:",constellation[5])
elif month==5:
    if day<21:
        print("星座為:",constellation[5])
    else:
        print("星座為:",constellation[6])
elif month==6:
    if day<21:
        print("星座為:",constellation[6])
    else:
        print("星座為:",constellation[7])
elif month==7:
    if day<22:
        print("星座為:",constellation[7])
    else:
        print("星座為:",constellation[8])
elif month==8:
    if day<23:
        print("星座為:",constellation[8])
    else:
        print("星座為:",constellation[9])
elif month==9:
    if day<23:
        print("星座為:",constellation[9])
    else:
        print("星座為:",constellation[10])
elif month==10:
    if day<23:
        print("星座為:",constellation[10])
    else:
        print("星座為:",constellation[11])
elif month==11:
    if day<22:
        print("星座為:",constellation[11])
    else:
        print("星座為:",constellation[1])
elif month==12:
    if day<22:
        print("星座為:",constellation[1])
    else:
        print("星座為:",constellation[0])