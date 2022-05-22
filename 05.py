M = int(input("請輸入階層值M："))
n = 1
total = 1
while total < M:
    n += 1
    total *= n
print("超過 M 為",M,"的最小階層 N 值為：",n)