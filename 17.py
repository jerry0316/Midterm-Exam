a1 = input("輸入第一個矩陣為:").split()
a2 = input("輸入第一個矩陣第一列的值為:").split()
a3 = input("輸入第一個矩陣第二列的值為:").split()
b1 = input("輸入第二個矩陣為:").split()
b2 = input("輸入第二個矩陣第一列的值為:").split()
b3 = input("輸入第二個矩陣第二列的值為:").split()
if len(a2)==len(b2) and len(a3)==len(b3):
    ans1=int(a2[0])+int(b2[0])
    ans2=int(a2[1])+int(b2[1])
    ans3=int(a3[0])+int(b3[0])
    ans4=int(a3[1])+int(b3[1])
    print(str(ans1)+","+str(ans2))
    print(str(ans3)+","+str(ans4))
else:
    print("兩個矩陣無法相加")

