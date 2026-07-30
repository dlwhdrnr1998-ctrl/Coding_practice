class Animal:
    # 1. num_of_animal 클래스 속성 정의
    num_of_animal = 0


class Dog(Animal):
    # 2. 인스턴스가 생성될 때마다 Animal의 num_of_animal 1 증가
    def __init__(self):
        Animal.num_of_animal += 1


class Cat(Animal):
    # 2. 인스턴스가 생성될 때마다 Animal의 num_of_animal 1 증가
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    # 3. Animal 클래스의 num_of_animal 속성에 접근하는 클래스 메서드 구현
    @classmethod
    def access_num_of_animal(cls):
        return f"동물의 수는 {cls.num_of_animal}마리 입니다."


# --- 실행 및 출력 ---
dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
#  num_of_animal 클래스 속성을 정의하시오.
# Animal 클래스를 상속받는 Dog와 Cat 클래스를 수정하여 각각의 인스턴스가 생성될 때 
# Animal 클래스의 num_of_animal의 값이 증가하도록 생성자를 수정하시오.
# Dog와 Cat을 다중 상속받는 Pet 클래스를 수정하여 
# Animal 클래스의 num_of_animal 속성에 접근할 수 있는 
# 클래스 메서드 access_num_of_animal 를 구현하시오.
