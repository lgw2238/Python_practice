# 상속 : extend 확장느낌.
class Animal:
    Animal_name = '앙'
    
    def __init__(self, name, angle):
        print('생성자 호출')
        self.name = name
        self.angle = angle

    def eat(self):
        print('삼시 세끼를 잘 챙깁시다.')

    def sleep(self):
        print('하루 6시간은 자야해요.')

    def walk(self):
        print('두 발로 걸어요')

    def move(self):
        # 각 객체가 걷는다.
        print(' 걷는 것은 {} 이다.'.format(self.name))

# 자식 클래스 : Sub Class
class Human(Animal):  # 객체안에 상속시킬 클래스를 ()언에 담는다.

    def __init__(self, name, angle):
        super(Human, self).__init__(name, angle)
        self.angle = angle

    def coding(self):
        print('godGoogle, StackOverflow')

    def walk(self):
        print('두 발로 서서 전방 {} 도를 주시하며'.format(self.angle))

    def move(self):
        self.walk()
        super().move()


class Dog(Animal):
    def __init__(self, name, angle):
        super(Dog, self).__init__(name, angle)
        self.angle = angle

    def detect(self):
        print('집을 지키자')

    def walking(self):
        print('네 발로 서서 {} 를 돌아보며'.format(self.angle))

    def move(self):
        self.walking()
        super().move()


'''
# 두 발로 서서 전방 15도를 주시하며 걷는 것은 사람이다.
 네 발로 서서 사방을 돌아보며 걷는 것은 강아지 이다.
 - move
 - angle, name
'''

person = Human('사람', 15)
person.move()

print('------------------------------------')
dog = Dog('강아지', '사방')
dog.move()