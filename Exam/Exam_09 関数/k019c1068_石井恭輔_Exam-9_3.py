x = int(input("上底＞"))
y = int(input("下底＞"))
z = int(input("高さ＞"))

def tryangle_area(x,y):
    return (hou*z)/2

def trapezoid_area(x,y):
    hou = x+y
    return hou
    

hou = trapezoid_area(x,y)

print(tryangle_area(hou,z))
