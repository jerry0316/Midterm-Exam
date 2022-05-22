data = {}
for i in range(int(input("輸入n值:"))):
    name = input("請輸入姓名:")
    email = input("請輸入電子郵件:")
    data[name] = email
search = input("請輸入要查詢電子郵件的姓名:")
print(search,"電子郵件帳號為",data[search])