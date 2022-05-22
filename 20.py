group=int(input("請輸入組數為:"))
for i in range(group):
    group2=input("請輸入第"+str(i+1)+"組:").split(" ")
    price=int(group2[0])*250+int(group2[1])*175
    print("第"+str(i+1)+"組費用為:"+str(price))