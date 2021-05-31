print()
'''
# 특수한 메소드 : 메소드 이름 양쪽에 __ 두개 
# 구글 검색 : python special attributes
'''

class Human() :
    # 초기화 메소드
    # 오버로딩
    def __init__(self):
        pass
        print('__init__ 실행')

    # 오버로딩
    def __init__(self, name, height) :
        print('__init__ 실행')
        print('이름 : {}, 키 : {}'.format(name, height))

    # 오버로딩
    def __init__(self, name, height) :
        self.name = name
        self.height = height

    # 오버라이딩
    # 문자열화 메소드 : 인스턴스를 문자열로 변환할 때 어떻게 표현할지 결정 할 수 있음
    def __str__(self) :
        return "이름 : {}, 키 : {} ".format(self.name, self.height)

'''
person = Human('홍길동', 178.8)
print(person.name)
print(person.height)
'''

person = Human('유관순', 160.3)
# 실행하면 원래는 객체의 인스턴스 값이 나와야하는데
# 문자열화 메소드를 사용하면
print(person)















