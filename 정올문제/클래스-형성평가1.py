#<문제>
#동물의 종류, 이름, 나이를 자료로 갖는 class를 정의하고 
#자료를 입력받아서 클래스를 이용하여 출력 예와 같이 출력하는 프로그램을 작성하시오.

#입력
# Dog Happy 7
#출력
# Type: Dog
# Name: Happy
# Age: 7

#<내 답안>
class Animal: 
    def __init__(self,type,name,age):
        self.type = type
        self.name = name
        self.age = age
    def arrange_inform(self):
        print(f"Type : {self.type}\n"
            f"Name : {self.name}\n"
            f"Age : {self.age} "
            )
        
animal_info_type, animal_info_name, animal_info_age = input("클래스에 들어갈 성질들을 넣어주세요 : ").split()
animal = Animal(animal_info_type,animal_info_name,animal_info_age)

animal.arrange_inform()


#모범답안
class Animal: 
    def __init__(self, animal_type, name, age):
        self.type = animal_type
        self.name = name
        self.age = int(age)  # 나이는 정수(int)로 변환
        
    # print(객체)를 했을 때 자동으로 실행되는 파이썬 특수 메서드
    def __str__(self):
        return (
            f"Type: {self.type}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}"
        )

# 입력받기
info = input("클래스에 들어갈 성질들을 넣어주세요 : ").split()

# 인스턴스 생성
animal = Animal(info[0], info[1], info[2])

# 객체 바로 출력!
print(animal)


        


