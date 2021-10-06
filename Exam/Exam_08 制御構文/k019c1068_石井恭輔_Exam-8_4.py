a = int(input("数値＞"))
c=0
for i in range(2,a):
    if(a % i == 0):
        print("素数ではありません")
        c=1
        break

if(c == 0):
    print("素数です")