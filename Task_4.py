class Animals:
    zoo = "Hello zoo!"
    pred = "Хищники! Не кормить!"
    herb = "Это животное можно кормить!"

    def __init__(self, predators, herbivores):
        self.predators = predators
        self.herbivores = herbivores

    def proveka(self):
        if self.predators == self.pred:
            print('Опасно!')
        elif self.herbivores == self.herb:
            print('Можно кормить!')

    def info_zoo(self):
    @staticmethod
    def hellozoo():
        print("Приветсвуем вас! ")


class Wolves(Animals):

    def __init__(self, name):
        super.__init__()
        self.name = name

    def info_zoo(self):
        print('Волки, являются хищниками! ')


class Giraffes(Animals):
    def __init__(self):
        super.__init__()

    def info_zoo(self):
        print()