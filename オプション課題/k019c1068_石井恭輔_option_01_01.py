a = int(input('数値を入力してください'))
if a % 400 == 0:
    print('うるう年です')
elif a % 100 == 0:
    print('うるう年ではありません')
elif a % 4 == 0:
    print('うるう年です')
else:
    print('うるう年ではありません')
    
