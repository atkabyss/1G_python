a = input("入力＞")

b = a.split(",")

d = 0

for c in b:
    d = int(c) + d

d = d / len(b)

print("平均：" + str(d))