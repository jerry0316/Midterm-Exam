password=input("輸入一組四位數字為:")
password2=list(password)
for i in range(len(password2)):
    password2[i]=(int(password2[i])+7)%10
print ("輸出加密後的數字為:"+str(password2[2])+str(password2[3])+str(password2[0])+str(password2[1]))