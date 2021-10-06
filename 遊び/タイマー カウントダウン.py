from time import sleep

target_time = int(input("時間を設定してください＞"))

def down_timer(secs):
    for i in range(secs, -1, -1):
        print(i)
        sleep(1)
    print("時間です！")

down_timer(target_time)
