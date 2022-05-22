num = int(input("請輸入測試資料數量為(1~20):"))
list = []
for i in range(num):
    for j in range(4):
        list.append(input("請輸入第"+str(j+1)+"項資料:"))
    if int(list[1]) - int(list[0]) == int(list[3]) - int(list[2]):
        ans=int(list[3])+(int(list[3])-int(list[2]))
        list.append(str(ans))
        print(str(list) +"此為等差數列")
    if int(list[1]) / int(list[0]) == int(list[3]) / int(list[2]):
         ans=int(list[3])*2
         list.append(str(ans))
         print(str(list) +"此為等差數列")
       