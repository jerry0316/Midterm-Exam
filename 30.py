answer=list(input("請輸入正確答案:"))
A=0;B=0
while True:
    answer2=list(input("請輸入猜測答案:"))
    for i in range(len(answer)):
        if answer2[i] in answer:
            if answer[i]==answer2[i]:
                A+=1
            else:
                B+=1
        else:
            continue
    print(A,"A",B,"B")
    A=0;B=0
    if answer2==answer:
        break