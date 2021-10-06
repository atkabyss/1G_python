from time import sleep

target_time = int(input("時間を設定してください＞"))

def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)
    print("時間です！")

up_timer(target_time)