import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты в пространстве
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        return f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, i'm peaceful :)"
        else:
            return "Be careful, i'm attacking you 0_0"


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True  # Наличие клюва

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        return f"Here are(is) {eggs_count} eggs for you"


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz_abs = abs(dz)
        new_z = self._cords[2] - (dz_abs / 2) * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"  # Звук утконоса
        # Устанавливаем степень опасности для атаки
        self._DEGREE_OF_DANGER = 8

    def speak(self):
        return self.sound


# Пример использования классов
db = Duckbill(10)

# Проверка атрибутов
print(db.live)          # True
print(db.beak)          # True

# Проверка звука
print(db.speak())       # Click-click-click

# Проверка атаки
print(db.attack())      # Be careful, i'm attacking you 0_0

# Движение и получение координат
db.move(1, 2, 3)
print(db.get_cords())   # X: 10 Y: 20 Z: 30

# Ныряние и получение координат
db.dive_in(6)           # Z изменится на 0 (30 - (6/2)*10)
print(db.get_cords())   # X: 10 Y: 20 Z: 0

# Печать яиц
print(db.lay_eggs())     # Here are(is) X eggs for you (где X - случайное число от 1 до 4)