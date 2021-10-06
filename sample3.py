class Bird:
    def move(self):
        print("とぶよー")
class Pigeon(Bird):
    pass
class Rooster(Bird):
    pass
class Penguin(Bird):
    def move(self):
        print("泳ぐよー")

bird1 = Pigeon()
bird2 = Rooster()
bird3 = Penguin()
bird1.move()
bird2.move()
bird3.move()