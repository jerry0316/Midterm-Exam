A=1;J=11;Q=12;K=13
poker=input("請輸入一副牌:").split(" ")
total=0
for i in poker:
    if i=="A":
        total+=1
    elif i=="J":
        total+=11
    elif i=="Q":
        total+=12
    elif i=="K":
        total+=13
    else:
        total+=int(i)
print(total)