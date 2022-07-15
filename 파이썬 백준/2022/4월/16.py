while True:
    a,symbol,b = input().split()
    if a =="0"==b and symbol =="W":
        break
    
    a = int(a)
    b = int(b)
    if symbol == "W":
        wow = a-b
    else:
        wow = a+b
    if wow < -200:
        print("Not allowed")
    else:
        print(wow)









