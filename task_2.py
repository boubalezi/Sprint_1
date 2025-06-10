class Tester:

    def __init__(self, name, deadline): 
        self.name = name #объявляем атрибут через self
        self.deadline = deadline #объявляем атрибут через self, присваиваем значение атрибута - deadline 

    def work_hard(self): #создаем метод
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1', deadline=False) #создаем объект 1 
tester_1.work_hard()  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2', deadline=True) #создаем объект 2
tester_2.work_hard()   # 'tester_2 Что ж, ещё часок поработаю!'