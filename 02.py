electricity  = int(input("請輸入電費度數"))

if electricity  <= 120:
    print("Summer months:",(electricity *2.10))
    print("Non-Summer months:",(electricity *2.10))
elif electricity <=330:
    print("Summer months:",(electricity -120)*3.02 + 120*2.10)
    print("Non-Summer months:",(electricity -120)*2.68 + 120*2.10)
elif electricity <=500:
    print("Summer months:",(electricity -330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(electricity -330)*3.61 + (330-120)*2.68 + 120*2.10)
elif electricity <=700:
    print("Summer months:",(electricity -500)*4.97 + (500-330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(electricity-500)*4.01 + (500-330)*3.61 + (330-120)*2.68 + 120*2.10)
elif electricity  >700 :
    print("Summer months:",(electricity -700)*5.63 + (700-500)*4.97 + (500-330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(electricity -700)*4.50 + (700-500)*4.01 + (500-330)*3.61 + (330-120)*2.68 + 120*2.10)
