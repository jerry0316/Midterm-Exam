out=""
password = input("請輸入傳送密碼(6位數):")
if len(password)==6:
    password2= list(password)
    for i in range(0,len(password)):
            for j in range(0,10):
                if j*4%7 == int(password2[i]):
                    out+=str(j)
                    break
print("解密後密碼為:"+out)