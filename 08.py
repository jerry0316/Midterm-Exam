firstline = input("輸入第一行正整數為:")
secondline = input("第二行中數列中的數字為:").split()
count = 1
for n in secondline:
    if secondline.count(n) > count:
        count = secondline.count(n)
        Max = n
if count == 1:
    print("每個數字剛好只出現 1 次")
else:
    print("最大出現次數的數字為:",Max,"出現次數為:",count)