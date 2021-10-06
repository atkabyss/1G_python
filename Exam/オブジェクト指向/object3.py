class Ayanami:
    count = 0
    def __init__(self):
        Ayanami.count += 1
        print("私はたぶん" + str(Ayanami.count) + "人目だと思うから")

ayanami_01 = Ayanami()
ayanami_02 = Ayanami()
ayanami_03 = Ayanami()