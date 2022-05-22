word = input("輸入一整數序列為:").split()
wordlen=len(word)
for n in word:
    if word.count(n) > wordlen//2:
        overword=n
    else:
        overword="NO"
print("過半元素為:",overword)