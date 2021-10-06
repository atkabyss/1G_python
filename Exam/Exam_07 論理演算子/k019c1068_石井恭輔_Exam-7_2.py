a = int(input("西暦＞"))

if(a >= 1896 and (a - 1896) % 4 == 0):
    print("開催年です")
else:
    print("開催年ではありません")