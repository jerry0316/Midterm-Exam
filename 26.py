a=str(input("請輸入檢測的字串(end結束):"))
b=str(input("請輸入檢測的單一字元:"))
if a =="end":
    print("檢測結束")
else:
    print("字元",b,"出現次數為:",a.count(b))