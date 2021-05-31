# 상속 : extend 확장느낌.
class Animal:
    def eat(self):
        print('삼시 세끼를 잘 챙깁시다.')
    def sleep(self):
        print('하루 6시간은 자야해요.')
    def walk(self):
        print('두 발로 걸어요')


# 자식 클래스 : Sub Class
class Human(Animal):   # 객체안에 상속시킬 클래스를 ()언에 담는다.
    def coding(self):
        print('godGoogle, StackOverflow')

class Dog(Animal):
    def detect(self):
        print('집을 지키자')

person = Human()
person.eat()
person.sleep()
person.coding()

print('-----------------------------------------------')
dog = Dog()
dog.eat()
dog.sleep()
dog.detect()

