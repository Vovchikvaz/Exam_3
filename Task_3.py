#дописать классы Company, Programmer.
class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}

    def __init__(self, index):
        if index > 4: index = 4
        self._index = index
        self._levels = self.levels[self._index]

    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
            print('Ваш уровень повысился до:', self._levels)

    def s_lead(self):
        if self._index == 4:
            print('У вас максимальный уровень!')
        else:
            print('Ваш уровень слишком мал! ', self.levels[self._index])
        return self._index == 4


class Programmer(Company):

    def __init__(self, name, uroven):
        super().__init__(uroven)
        self.name = name

    def work(self):
        self.level_up()

    @staticmethod
    def knowledge_base():
        print( Company.levels)


it = Company(1)
jhon = Programmer('Jhon',1)
jhon.knowledge_base()
while jhon.s_lead() == False:
    jhon._level_up()
jhon.s_lead()


