print()
'''
# 메소드에 대한 특별한 규칙 : 메소드를 호출할 때 첫번째 인자를 생각하면 인스턴스 자신으로 채워준다.
# keyword : self - 자기 자신을 자동으로 호출하는 매개변수
'''

class Human() : 
    # def create_human(): -> self 생략해도 무관하다
    def create_human(name, height) :
        person = Human()
        person.name = name
        person.height = height
        return person

    # 먹기
    # 이때 self는 참고변수임
    def eat(self) :
        self.height += 0.2
        print('{} 이 건강하게 먹어서 {} 이 되었어요.'.format(self.name, self.height))

    def walk(self) :
        self.height += 0.3
        print('{}이 운동을 해서 {} 이 되었어요.'.format(self.name, self.height))

    def speak(self, message) :
        print(message)

person = Human.create_human('유관순', 162.7)
person.eat()
person.walk()

print('-------------------------------------------------------------------------------')

'''
# 인스턴스에서 call by value 수행 시 첫번째 매개변수인 self는 생략하고 호출해 줌
# 파이썬이 첫번째 매개변수인 self는 자동으로 호출해줌 
'''
person = Human.create_human('이순신', 178.3)
person.speak('필사즉생')

print('-------------------------------------------------------------------------------')

# 이때 self는 매개변수임
def no_eat(self) :
    self.height -= 0.5
    print('{} 가 다이어트를 열심히 해서 {} 가 되었어요.'.format(self.name, self.height))

person = Human.create_human('신사임당', 43.8)
no_eat(person)

# person.no_eat()









