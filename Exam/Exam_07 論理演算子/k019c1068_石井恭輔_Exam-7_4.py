a = int(input("西暦＞"))

if(a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)):
    print("うるう年")
else:
    print("平年")