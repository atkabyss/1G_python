a = int(input("数値＞"))

for i in range(1,a+1,1):
    if(a % i == 0):
        print(i,end=",")
