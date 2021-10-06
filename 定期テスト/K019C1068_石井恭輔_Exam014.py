def circle_area(r):
    redius = r*r*3.14
    return redius

redius = float(input("半径を入力してください＞"))

area = circle_area(redius)

print("円の面積：" + str(area))