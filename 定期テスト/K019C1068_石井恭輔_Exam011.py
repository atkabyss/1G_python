a = int(input("点数を入力して下さい＞"))
b = float(input("出席率を入力して下さい＞"))

if b < 75:
    print("あなたの成績：D")
    exit(0)

if a >= 90:
    print("あなたの成績：S")
elif a >= 80:
    print("あなたの成績：A")
elif a >= 70:
    print("あなたの成績：B")
elif a >= 60:
    print("あなたの成績：C")
else:
    print("あなたの成績：D")