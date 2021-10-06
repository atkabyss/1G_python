password = input("入力＞")

if len(password) < 8:
    print("短すぎます")
elif len(password) >= 13:
    print("長すぎます")
else:
    print("O.K.")