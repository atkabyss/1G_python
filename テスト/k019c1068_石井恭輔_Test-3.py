a = str(input("４桁の２進数＞"))

c = int(a[0]) * 8

d = int(a[1]) * 4

e = int(a[2]) * 2

f = int(a[3]) * 1

g = c+d+e+f

print("１０進数：" + str(g))