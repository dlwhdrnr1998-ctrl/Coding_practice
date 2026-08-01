# 1단계: 기본 데이터 및 함수 준비
# many_user 변수에 다음 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당합니다:
# 이름: 김시습, 나이: 20, 주소: 서울
# 이름 허균, 나이:16, 주소: 강릉
# 이름: 남혜인, 나이:25, 주소: 조선
# decrease_book 함수를 작성합니다. 이 함수는 전체 책의 수(number_of_book)를 인자로 받은 수만큼 줄입니다.

# 2단계: 핵심 기능 함수(rental_book) 설계
# rental_book이라는 이름의 함수를 정의합니다. 이 함수는 단 하나의 인자 info를 받습니다.
# info 인자로는 {'고객이름': 고객나이} 형태의 딕셔너리가 전달됩니다.
# 함수 내부에서는 info 딕셔너리에서 고객의 이름과 나이를 추출합니다.
# 추출한 나이를 10으로 나눈 몫으로 대여할 책의 수를 계산하고, decrease_book 함수를 호출합니다.
# 대여 완료 메시지를 출력합니다.

# 3단계: 데이터 형태 변환 (for문 사용)
# many_user와 rental_book이 요구하는 데이터 형태가 다르므로, {'name': '김시습', ...} 형태를 {'김시습': 20} 형태로 변환하는 규칙을 정의합니다.
# 변환된 딕셔너리를 저장할 새로운 빈 리스트 user_info를 생성합니다.
# many_user 리스트를 순회하는 for 반복문을 작성합니다.
# 반복문 내부에서, many_user의 각 고객 딕셔너리로부터 {'이름': 나이} 형태의 신규 딕셔너리를 만든 후, user_info 리스트에 추가(append)합니다.

# 4단계: 전체 로직 실행 (for문 사용)
# 3단계에서 생성된 user_info를 순회하는 for 반복문을 작성합니다.
# 목록의 각 고객 정보(info)를 rental_book 함수의 인자로 전달하여 호출합니다.

# [도전] 4단계: for문을 lambda와 map으로 변경하기3단계와 4단계에서 작성한 for 반복문은 lambda와 map 함수를 사용하면 단 한 줄의 코드로 동일한 결과를 얻을 수 있습니다.
# map 함수를 사용하여, many_user 리스트의 모든 요소에 lambda로 구현한 변환 규칙을 일괄 적용하고, 결과를 list()로 감싸 새로운 변수에 저장합니다.
# 변환된 결과 전체에 rental_book 함수를 map을 사용해 적용합니다.
# map 객체는 '지연 평가' 특성으로 인해 즉시 실행되지 않으므로, list() 함수로 전체를 감싸 모든 대여 절차가 실제로 실행되도록 합니다.



# <문제>
number_of_people = 0

def increase_user():
    pass

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user():
    pass

def decrease_book(number_of_rentbook):
    number_of_book -= number_of_rentbook


many_user = {
    "이름": "김시습", "나이": 20, "주소": "서울",
    "이름": "허균", "나이":16, "주소": "강릉",
    "이름":"남혜인", "나이":25, "주소": "조선",
}

def rental_book(info):
    info.items()
    대여할책의수= info.value() // 10
    decrease_book()



#<solvel>
number_of_book = 100  # 테스트를 위한 전체 책 수 초기화

# 신규 고객 정보 딕셔너리를 요소로 갖는 리스트
many_user = [
    {"이름": "김시습", "나이": 20, "주소": "서울"},
    {"이름": "허균", "나이": 16, "주소": "강릉"},
    {"이름": "남혜인", "나이": 25, "주소": "조선"},
]


def decrease_book(number_of_rentbook):
    global number_of_book
    number_of_book -= number_of_rentbook
    print(f"남은 책의 수 : {number_of_book}")


# 2단계: 핵심 기능 함수(rental_book) 설계
def rental_book(info):
    # info는 {'고객이름': 고객나이} 형태의 딕셔너리
    # name, age 추출 (items() 이용)
    name, age = list(info.items())[0]

    # 나이를 10으로 나눈 몫으로 대여할 책의 수 계산
    number_of_rentbook = age // 10

    # decrease_book 함수 호출
    decrease_book(number_of_rentbook)

    # 대여 완료 메시지 출력
    print(f"{name}님이 {number_of_rentbook}권의 책을 대여했습니다.")


print("=== 3~4단계: for문 사용 실행 ===")

# 3단계: 데이터 형태 변환 (for문 사용)
user_info = []
for user in many_user:
    # {'이름': 나이} 형태의 신규 딕셔너리 생성 후 추가
    user_info.append({user["이름"]: user["나이"]})

# 4단계: 전체 로직 실행 (for문 사용)
for info in user_info:
    rental_book(info)


print("\n=== [도전] 4단계: lambda와 map 사용 실행 ===")
# 테스트를 위해 책 수 초기화
number_of_book = 100

# 1) map + lambda를 사용해 데이터 변환
user_info_map = list(map(lambda u: {u["이름"]: u["나이"]}, many_user))

# 2) map을 사용해 rental_book 일괄 적용 (list로 감싸 즉시 실행)
list(map(rental_book, user_info_map))

