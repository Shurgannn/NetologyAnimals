from abc import ABC, abstractmethod

class Animal(ABC):
    satiety = 0  # сытость
    max_satiety = 100
    max_weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # kg

    def feed(self, satiety):  # кормление
        if self.satiety + satiety > self.max_satiety:
            print('Сытость:', self.name, ':', self.satiety)
            self.satiety = self.max_satiety
            print('Наелся')
            print('Сытость:', self.name, ':', self.satiety)
        else:
            self.satiety += satiety

    def __lt__(self, other):
        return self.weight < other.weight

    @abstractmethod
    def collect(self):
        pass


class Goose(Animal):
    voice = 'га-га-га'
    max_satiety = 50

    def collect(self):
        print('Яйца собраны')

Goose1 = Goose('Серый', 5)
print(Goose1.name, ':', '"', Goose.voice, '"')
Goose1.feed(10)
Goose1.feed(100)
Goose1.collect()
Goose2 = Goose('Белый', 3)
print(Goose2.name, ':', '"', Goose.voice, '"')
Goose2.feed(60)
Goose2.collect()


class Cow(Animal):
    voice = 'му-му'

    def collect(self):
        print('Молоко подоено')

Cow1 = Cow('Манька', 100)
print('\n',Cow1.name, ':', '"', Cow.voice, '"')
print('Сытость коровы:', Cow1.name, ':', Cow1.satiety)
Cow1.feed(110)
Cow1.collect()


class Sheep(Animal):
    voice = 'бе-бе'
    state2 = 'овца не стрижена'

    def collect(self):
        print('Овца пострижена')

Sheep1 = Sheep('Барашек', 10)
print('\n',Sheep1.name, ':', '"', Sheep.voice, '"')
Sheep1.feed(110)
Sheep1.collect()
Sheep2 = Sheep('Кудрявый', 20)
print(Sheep2.name, ':', '"', Sheep.voice, '"')
Sheep2.feed(110)
Sheep2.collect()


class Chiken(Animal):
    voice = 'ку-ка-реку'

    def collect(self):
        print('Яйца собраны')

Chiken1 = Chiken('Ко-Ко', 1.5)
print('\n',Chiken1.name, ':', '"', Chiken.voice, '"')
Chiken1.feed(110)
Chiken1.collect()
Chiken2 = Chiken('Кукареку', 1)
print(Chiken2.name, ':', '"', Chiken.voice, '"')
Chiken2.feed(110)
Chiken2.collect()


class Goat(Cow):
    voice = 'ме-ме'

Goat1 = Goat('Рога', 5)
print('\n',Goat1.name, ':', '"', Goat.voice, '"')
Goat1.feed(110)
Goat1.collect()
Goat2 = Goat('Копыта', 6)
print(Goat2.name, ':', '"', Goat.voice, '"')
Goat2.feed(110)
Goat2.collect()


class Duck(Animal):
    voice = 'кря-кря'

    def collect(self):
        print('Яйца собраны')

Duck1 = Duck('Кряква', 4)
print('\n',Duck1.name, ':', '"', Duck1.voice, '"')
Duck1.feed(110)
Duck1.collect()

print('Общий вес всех животных:', sum([Goose1.weight, Goose2.weight, Cow1.weight, Sheep1.weight, Sheep2.weight, Chiken1.weight, Chiken2.weight, Goat1.weight, Goat2.weight, Duck1.weight]), 'кг')

animals_list = [(Goose1.name, Goose1.weight), (Goose2.name, Goose2.weight), (Cow1.name, Cow1.weight), (Sheep1.name, Sheep1.weight), (Sheep2.name, Sheep2.weight), (Chiken1.name, Chiken1.weight), (Chiken2.name, Chiken2.weight), (Goat1.name, Goat1.weight), (Goat2.name, Goat2.weight), (Duck1.name, Duck1.weight)]

def sort_by_weight():
    animals_list.sort(key=lambda animal: animal[1])

sort_by_weight()
print('Имя самого тяжелого животного методом функции:', animals_list[-1][0])

list1 = sorted(animals_list, key=lambda animal: animal[1])
print('Имя самого тяжелого животного методом сортировки списка:', list1[-1][0])

max_weight = Goose1.weight
max_weight_name = Goose1.name
if max_weight > Goose2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goose2.weight
    max_weight_name = Goose2.name
if max_weight > Cow1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Cow1.weight
    max_weight_name = Cow1.name
if max_weight > Sheep1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Sheep1.weight
    max_weight_name = Sheep1.name
if max_weight > Sheep2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Sheep2.weight
    max_weight_name = Sheep2.name
if max_weight > Chiken1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Chiken1.weight
    max_weight_name = Chiken1.name
if max_weight > Chiken2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Chiken2.weight
    max_weight_name = Chiken2.name
if max_weight > Goat1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goat1.weight
    max_weight_name = Goat1.name
if max_weight > Goat2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goat2.weight
    max_weight_name = Goat2.name
if max_weight > Duck1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Duck1.weight
    max_weight_name = Duck1.name
print('Имя самого тяжелого животного:', max_weight_name)



# print(goose1.__dict__)
# print(goose2.__dict__)
# print(goose.__dict__)
