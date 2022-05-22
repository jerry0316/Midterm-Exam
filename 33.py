subject=['國文','英文','微積分','體育','程式設計']
score=[]
sum=0
for i in range(5):
    score2=int(input(subject[i]+":"))
    score.append(score2)
    sum+=score[i]
print("平均分數:",sum/5)
print("最高分科目:",max(score))
print("最低分科目:",min(score))