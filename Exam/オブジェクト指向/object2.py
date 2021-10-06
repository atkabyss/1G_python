class Person:
    def __init__(self, name, age): # __init__メソッドの定義
        self.name = name # 引数をインスタンス変数に代入
        self.age = age # 引数をインスタンス変数に代入
    def print_profile(self): # インスタンスメソッドの定義
        print(self.name + 'は' + str(self.age) + '歳です')

taro = Person('かまトゥ', 20) # __init__メソッドの引数として値を渡す
hanako = Person('ぱっちぃ', 19) # __init__メソッドの引数として値を渡す

taro.print_profile()
hanako.print_profile()