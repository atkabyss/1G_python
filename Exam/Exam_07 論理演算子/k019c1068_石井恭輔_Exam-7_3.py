a = float(input("身長"))
b = float(input("体重"))

c = b / (a*a)

if(c < 18.5):
    print("痩せすぎ")
elif(c >= 18.5 and c < 25):
    print("標準")
elif(c >= 25):
    print("肥満")