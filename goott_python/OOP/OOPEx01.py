print()

# 클래스 선언
class Test:     # 클래스 명은 첫글자 대문자(권장)
    str = 'This is Class' # str: Test 클래스의 요소 (attribute - field or member)

# 클래스 호출
test1 = Test()    # test1은 Test클래스에 의해서
print(test1.str)


print('-----------------------------------------')
class Person:
    def say(self):   # say : Person 클래스의 요소(attribute - method)
        print('hi python')

p1 = Person()

p1.say()

'''
# 클래스 구조
class 클래스명 : 
    변수 - 클래스에 내부 변수들을 필드(field)라고 부름

    함수 - 클래스 내부 함수들을 메소드(method)라고 부름

# 클래스는 필드와 메소드로 구성된다. 이를 클래스의 속성(attribute)이라고 정의
# 변수와 함수이지만 구별지어서 부르는 것은 클래스나 객체에 소속되어있다는 대상이라는 것을 나타내기 위함

# 일반함수와 클래스 내부의 메소드의 차이점 - self
  메소드의 경우 매개변수에 항상 self를 맨 앞에 두어야 함.


  메소드 호출 시 이 self 매개변수에는 사용자(개발자)가 직접적으로 값을 넘겨주지 않아도 된다.
  파이썬이 자동으로 값을 할당
'''


print('-------------------------------------------------------')
class Person1:
    pass                # 클래스 내부에 요소가 없다면 반드시 pass 구문을 통해 블록이 닫히도록 해줘야 한다

p2 = Person1()
print(p2)


print('-------------------------------------------------------')
'''
# 파이썬의 클래스에는 여러가지 특별한 메소드들이 존재한다.
그 중 init()은 클래스가 인스턴스화 할때 초기화 기능을 해준다.
'''
class Person2:
    
    
    
    def __init__(self, name):   # init 으로 생성자 초기화 기능
        self.name = name
        # 원래는 class 에 name 이라는 값을 담아서 호출 하는 식으로 해야하지만
    def say(self):

        print('내 이름은', self.name)

p2 = Person2('임건우')

p2.say()

print('---------------------------------------------------------------------')
'''
# 클래스의 필드는 네임스페이스(클래스 내부 혹은 객체 내부)에서만 의미가 있다. 
# 필드를 누가 소유하고 있느냐에 따라서 클래스 변수, 객체 변수로 구분

# 클래스 변수 특성
    - 클래스로 부터 생성된 모든 인스턴스들이 접근 할 수 있다 (공유된다)
    - 어떤 객체가 클래스 변수를 변경한다면 다른 인스턴스 들에게도 변경 내용이 반영
# 객체 (인스턴스) 변수
    - 클래스로부터 생성도니 각각의 객체(인스턴스)에 속해 있는 변수
    - 객체별로 하나씩 따로 가질 수 있는 변수 (서로 공유하지 않는다.)
    
'''
class Character:

    # 클래스 변수
    cnt = 0
    def __init__(self, name):
        self.name = name                # self.name : 객체변수
        print('{}이/가 생성 중 ...'.format(self.name))
        # 클래스 변수 접근 : 클래스명. 클래스변수명
        Character.cnt += 1
    def say(self):
        print(' 안녕하세요 제 이름은 {} 입니다.'.format(self.name))

    def attack(self):
        print('{} 이/가 죽었습니다.'.format(self.name))

        Character.cnt -= 1

        if Character.cnt == 0:
            print('더 이상 캐릭터가 남아있지 않습니다.')
            return
        else:
            print('아직 {}명의 캐릭터가 남아있습니다'.format(Character.cnt))
    @classmethod
    def characterInfo(self):
        print('현재 {}개의 캐릭터가 있습니다.'.format(Character.cnt))
        
gameCharacter1 = Character('마린1')
gameCharacter1.say()

gameCharacter2 = Character('마린2')
gameCharacter2.say()

print('-------------------------------')
Character.characterInfo()

print('-------------------------------')
gameCharacter3 = Character('마린3')
gameCharacter3.attack(gameCharacter2)





print('-------------------------------')
Character.characterInfo()