a = int(input("年齢＞"))

b = int(input("会員証(1:有 2:無)＞"))

if a >= 18 and b == 1:
    print("料金: 1600円")
elif a >= 18 and b == 2:
    print("料金: 2400円")
elif a < 18 and b == 1:
    print("料金: 800円")
elif a < 18 and b == 2:
    print("料金: 1200円")
