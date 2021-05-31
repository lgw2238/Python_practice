class Human:
    def eat(self):
        print('삼시 세기를 잘 챙깁시다')
    def sleep(self):
        print('하루 8시간은 자야해요')
    def walk(self):
        print('두 발로 걸어요')
    def coding(self):
        print('stack overflow')

class Dog:
    def eat(self):
        print('사료를 잘 먹어요')
    def sleep(self):
        print('낮잠을 자야 해요')
    def walk(self):
        print('네 발로 걸어요')
    def detect(self):
        print('집을 지키자')

person = Human()
person.eat()

animal = Dog()
animal.eat()
