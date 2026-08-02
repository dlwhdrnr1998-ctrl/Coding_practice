#<문제>
#두 스마트폰의 기종, 색상, 가격을 입력받아 각각 출력 예와 같이 출력하는 프로그램을 작성하시오.

# 입력
# Aphone White 100
# GPhone Black 200

# 출력
# Aphone(White) $100
# GPhone(Black) $200

#<내 답안> : __str__() 매직매서드 활용, .split() 메서드 활용
class Smart_Phone:
    def __init__(self,기종,색상,가격):
        self.기종 = 기종
        self.색상 = 색상
        self.가격 = 가격

    def __str__(self):
        return f"{self.기종}({self.색상}) ${self.가격}"


for _ in range(2):
    what_smartphone = input("스마트폰의 기종 색상 가격을 차례로 입력해주세요. : ").split()

    customer_smartphone = Smart_Phone(what_smartphone[0],what_smartphone[1],what_smartphone[2])
    print(customer_smartphone)


#<모범답안> : 언패킹(*) 활용
class Smart_Phone:
    def __init__(self, 기종, 색상, 가격):
        self.기종 = 기종
        self.색상 = 색상
        self.가격 = 가격

    def __str__(self):
        # 끝에 오타났던 ')' 제거!
        return f"{self.기종}({self.색상}) ${self.가격}"

# 스마트폰 2개 입력받아 출력하기
for _ in range(2):
    what_smartphone = input().split()
    # *what_smartphone 으로 언패킹해서 한 번에 전달!
    customer_smartphone = Smart_Phone(*what_smartphone)
    print(customer_smartphone)

#<모범답안2> : 실무형 스타일 / 리스트 컴프리헨션 활용 / 데이터 버리지 않는 방식
class Smart_Phone:
    def __init__(self, 기종, 색상, 가격):
        self.기종 = 기종
        self.색상 = 색상
        self.가격 = 가격

    def __str__(self):
        return f"{self.기종}({self.색상}) ${self.가격}"

# 1. 2개의 스마트폰 객체를 만들어 리스트에 저장 (리스트 컴프리헨션)
phones = [Smart_Phone(*input().split()) for _ in range(2)]

# 2. 리스트에 저장된 스마트폰들을 순회하며 출력
for phone in phones:
    print(phone)


