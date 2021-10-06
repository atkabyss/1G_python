"""class Person:
    def __init__(self, name, age): # __init__メソッドの定義
        self.__name = name # 引数をインスタンス変数に代入。名称のPrefixに__あり
        self.__age = age # 引数をインスタンス変数に代入。名称のPrefixに__あり
    def print_profile(self): # クラスメソッドの定義
        print(self.__name + 'さんは' + str(self.__age) + '歳です。')

taro = Person('蒲田太郎', 21) # オブジェクトとしてインスタントを生成
taro.print_profile() # インスタンスメソッドの呼び出し。

# => クラス内部からは__name, __ageを利用できる

"""


value = (yield(x+1) for in range(100))
