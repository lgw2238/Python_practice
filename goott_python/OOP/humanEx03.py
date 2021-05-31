class Human() :
    pass

    def create_human(name, height):
        person = Human()
        person.name = name
        person.height = height
        return person

    def eat(person) :
        person.height += 0.2
        print('{} 이 건강하게 먹어서 {} 이 되었어요.'.farmat(person.name, person.height))

    def walk(person) :
        person.height += 0.3
        print('{} 이 운동을 해서 {} 이 되었어요.'.format(person.name, person.height))

person = Human.create_human('유관순', 157.3)
person.eat()
person.walk()

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
  
'''





