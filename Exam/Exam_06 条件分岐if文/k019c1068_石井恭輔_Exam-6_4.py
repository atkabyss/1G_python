point = int(input("入力＞"))

if point >= 80:
    print("評価：優")
elif point <= 79 and point >= 70:
    print("評価：良")
elif point <= 69 and point >= 60:
    print("評価：可")
else:
    print("不可")

