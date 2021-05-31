print()

# 절차 (구조적) 지향 프로그래밍

showInfo = ''

def person(name, age) :
    global showInfo
    showInfo += '이름 : ' + name + ' , ' + '나이 : ' + age +'\n'
    return showInfo

person('홍길동', '20')
person('유관순', '17')
print(showInfo)

print('----------------------------------------------------')

# 객체 지향 프로그래밍
class Person :
    def __init__(self):
        self.info = ''

    def showInfo(self, name, age):
        self.info += '이름 : ' + name + ' , 나이 : ' + age
        print(self.info)

# 재사용이 편리해짐
man = Person()
man.showInfo('홍길동', '20')

woman = Person()
woman.showInfo('유관순', '17')

print('----------------------------------------------------')

# 객체 정보 : type()
print(type(5))

# 객체 일치 여부 : isinstance()
print(isinstance(5, float))
print(isinstance(5, int))

print('----------------------------------------------------')

num1 = []
print(type(num1))

num2 = list(range(10))

text = list('hello')

print(type(num2))
print(type(text))

print('----------------------------------------------------')

print(isinstance(num1, list))
print(isinstance(num2, list))
print(isinstance(text, list))

print('----------------------------------------------------')

print(isinstance(num1, list))       # True
print(num1 == list)                 # False








