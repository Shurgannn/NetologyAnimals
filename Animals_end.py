from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight  # kg
        self.sound = sound

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def feed(self):
        pass


class Goose(Animal):

    def voice(self):
        print(f'{self.name} сказал(а): {self.sound}')

    def collect(self):
        print(f'Яйца собраны у {self.name}')

    def feed(self):
        print(f'{self.name} покормлен(а)')


class Cow(Animal):

    def voice(self):
        print(f'{self.name} сказал(а): {self.sound}')

    def feed(self):
        print(f'{self.name} покормлен(а)')

    def collect(self):
        print(f'Молоко подоено у {self.name}')


class Sheep(Animal):

    def voice(self):
        print(f'{self.name} сказал(а): {self.sound}')

    def feed(self):
        print(f'{self.name} покормлен(а)')

    def collect(self):
        print(f'Шерсть пострижена у {self.name}')


class Chiken(Goose):
    pass


class Goat(Cow):
    pass


class Duck(Goose):
    pass

animals = [Goose('Серый', 5, 'га-га-га'), Goose('Белый', 3, 'га-га-га'), Cow('Манька', 100, 'му-му'), Sheep('Барашек', 10, 'бе-бе'), Sheep('Кудрявый', 20, 'бе-бе'), Chiken('Ко-Ко', 1.5, 'ку-ка-реку'), Chiken('Кукареку', 1, 'ку-ка-реку'), Goat('Рога', 5, 'ме-ме'), Goat('Копыта', 6, 'ме-ме'), Duck('Кряква', 4, 'кря-кря')]
total_weight = 0
for animal in animals:
    animal.feed()
    animal.collect()
    animal.voice()
    total_weight += animal.weight
print('Общий вес животных:', total_weight, 'кг')

def sort_by_weight():
    animals.sort(key=lambda animal: animal.weight)
    print('Имя самого тяжелого животного:', animals[-1].name)

sort_by_weight()
