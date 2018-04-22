class Animal(object):
    def __init__(self, new_name):
        self.name = new_name
        print('An animal has been born.')

    def eat(self):
        print('Munch munch.')

    def make_noise(self):
        print('Grr says', self.name, '.')


class Cat(Animal):
    def __init__(self, new_name):
        super().__init__(new_name)
        print('A cat has been born.')

    def make_noise(self):
        print('Meow says', self.name, '.')


class Dog(Animal):
    def __init__(self, new_name):
        super().__init__(new_name)
        print('A dog has been born')

    def make_noise(self):
        print('Bark says', self.name, '.')


cat1 = Cat('Filemon')
dog1 = Dog('Bark')
dog2 = Dog('Dark')

cat1.eat()
cat1.make_noise()

dog1.eat()
dog1.make_noise()

dog2.eat()
dog2.make_noise()
