a = str(input("氏名を入力してください＞"))
b = str(input("得点を入力してください＞"))

c = "メッセージ：__NAME__さんの得点は__POINT__点です。"

c = c.replace("__NAME__",a)
c = c.replace("__POINT__",b)

print(c)