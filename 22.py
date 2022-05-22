data={"123":456,"456":789,"789":888,"336":558,"775":666,"566":221}
money={"123":9000,"456":5000,"789":6000,"336":10000,"775":12000,"566":7000}
number=int(input("請輸入查詢組數N為:"))
for i in range(number):
    password=input("請輸入帳號及密碼:").split(" ")
    if data[password[0]]==int(password[1]):
        print(money[password[0]])
    else:
        print("error")