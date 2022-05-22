dict = {}
for i in range(int(input("輸入筆數 n:"))):
    english, chinese = input("請輸入單字英文及中文:").split()
    dict[english] = chinese
search = input("輸入欲查詢單字:")
if search in dict:
    print(search,"中文意思為",dict[search])
else:
    print("字典未有此單字")