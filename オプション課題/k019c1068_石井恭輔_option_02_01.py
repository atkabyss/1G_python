a = int(input("元金＞"))
b = float(input("金利＞"))
c = int(input("預入期間＞"))

b = b*0.01
k=1

for i in range(c):
    risoku = a*b
    zandaka = a+risoku

    print(str(k) + "年目 : 元金" + "{:0.0f}".format(a) + "円" + "利息" + "{:0.0f}".format(risoku) + "円＝残高" + "{:0.0f}".format(zandaka) + "円")

    k = k+1
    a = zandaka
    risoku = zandaka*b