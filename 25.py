count=int(input("請輸入考試次數為:"))
students=int(input("請輸入學生人數為:"))
proportion = list(map(float, input("每次考試所佔的比率:").split()))
total = 0
for i in range(students):
    scores = list(map(int, input("請輸入成績為:").split()))
    for n in range(len(scores)):
        total += scores[n]*proportion[n]
print("全班的總平均值為:%.2f"%(total/students))