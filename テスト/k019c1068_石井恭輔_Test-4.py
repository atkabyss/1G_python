a = int(input("西暦＞"))

if 1930 > a:
    print("サッカーW杯開催年ではない")
elif a == 1942 or a == 1946:
    print("サッカーW杯開催年ではない")
elif (a-1930) % 4 == 0:
    print("サッカーW杯開催年")
else:
    print("サッカーW杯開催年ではない")