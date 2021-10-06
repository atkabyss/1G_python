def goukei(risuto):
    goukei = 0
    for x in risuto:
        goukei=goukei+int(x)
    return goukei

def heikin(risuto):
    kosu=int(len(risuto))
    heikin=goukei(risuto)/kosu
    return heikin

def saidai(risuto):
    saidai=0
    for x in risuto:
        if int(x)>saidai:
            saidai=int(x)
    return saidai

kazu = input("数値＞")
kazu = kazu.split(" ")

x = str(heikin(kazu))
y = str(saidai(kazu))

print("平均："+ x)
print("最大値："+ y)