# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self):
        pass

    def bark(self):
        print("멍멍!")


dog1 = Dog()
dog1.bark()




#  Dog 클래스는 Animal 클래스의 속성과 메서드를 상속받는다.
# Dog 클래스에 추가로 bark 메서드를 작성하여 "멍멍!"이라는 메시지를 출력하시오.