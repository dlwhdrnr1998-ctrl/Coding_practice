# 문제 1. 특정 숫자의 위치와 개수
# 주어진 리스트에서 숫자 20이 처음 등장하는 위치와 총 등장 횟수를 출력하시오.

#<답안> : .index() .count() 메서드 활용 
numbers = [10, 20, 30, 20, 40, 20]
first_show = numbers.index(20)
total_show = numbers.count(20)
print(first_show, total_show)


# 문제 2. 할 일 목록 수정하기
# 다음 할 일 목록에 "운동하기"를 추가하고, "공부하기"와 "청소하기"를 한 번에 추가하시오.
# 그 후 마지막 할 일을 삭제하고, 남은 목록을 출력하시오.

#<답안> : .extend([]) .apppend() .pop() 활용
todo_list = ['아침 먹기', '산책하기']
todo_list.append("운동하기")
todo_list.extend(["공부하기","청소하기"])
todo_list.pop()
todo_list.extend([])
print(todo_list)


# 문제 3. 점수 정리하기
# 주어진 점수 리스트를 작은 수부터 정리한 결과와 큰 수부터 정리한 결과를 각각 출력하시오.

#<답안>
scores = [85, 70, 95, 60, 90]
print(sorted(scores))
print(sorted(scores,reverse=True))
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)


# 문제 4. 마지막 상품과 특정 상품 삭제하기
# 상품 목록에서 마지막 상품을 삭제하고, 삭제한 상품을 출력하시오.
# 그 후 인덱스 1에 있는 상품을 삭제하고, 최종 상품 목록을 출력하시오.

#<답안>
products = ['노트북', '마우스', '키보드', '모니터']
print(products.pop())
print(products.pop(1))
print(products)


# 문제 5. 학생 정보 확인하기
# 다음 학생 정보에서 이름, 나이, 지역을 각각 출력하시오.
# 존재하지 않는 "전화번호"를 확인할 때는 "정보 없음"이 출력되도록 하시오.

#<답안>: .get() 메서드 활용 (안에 키를 넣으면 밸류를 가져옴)
student = {
    'name': '김민수',
    'age': 20,
    'region': '서울'
}
print(student.get('name'))  
print(student.get('age'))    
print(student.get('region'))  
print(student.get('phone', '정보 없음'))

key_value = student.items()
for key,value in key_value:
    print(f"{key}은(는) {value} 입니다.")

# 문제 6. 상품 이름과 가격 출력하기
# 상품 이름과 가격이 저장된 딕셔너리가 주어졌을 때, 다음과 같이 출력하시오.


#<답안>
products = {
    '사과': 1500,
    '바나나': 2000,
    '포도': 3000
}

for fruits,cost in products.items():
    print(f"{fruits}은/는 {cost}원 입니다.")


# 문제 7. 판매 완료 상품 삭제하기
# 상품 재고에서 "마우스"를 삭제하고, 삭제된 재고 수량을 출력하시오.
# 그 후 남은 상품 재고를 출력하시오.

#<답안> : pop 메서드 활용
stock = {
    '노트북': 3,
    '마우스': 5,
    '키보드': 4
}
count = len(stock)

print(stock.pop('마우스'))
count -= count
print(count)


# 문제 8. 동아리 회원 관리하기
# 현재 동아리 회원에 "지수"를 추가하고, "철수"를 삭제하시오.
# 최종 회원 목록을 출력하시오.

#<답안>:set함수의 메서드 (add remove)
members = {'민수', '영희', '철수'}
members.add("지수")
members.remove("철수")
print(members)


# 문제 9. 중복 없는 방문 지역 만들기
# 방문 기록을 확인하여 중복되지 않는 지역만 저장하시오.
# 그 후 "대전"을 추가하고 "부산"을 삭제하시오.

#<문제>
visited_list = ['서울', '부산', '서울', '제주', '부산']
visited_regions = set(visited_list)

visited_regions.add("대전")
visited_regions.remove("부산")
print(list(visited_regions))


# 문제 10. 문장 정리하기
# 문장 양쪽의 불필요한 공백을 제거하고, "Python"을 "파이썬"으로 변경하시오.
# 그 후 문장을 단어별로 나눈 뒤, 각 단어 사이를 "-"로 연결하여 출력하시오.

#<답안> : str 메서드 .strip() .replace() .split "".join()
sentence = '   Python 공부는 재미있다   '
modified_sentence = sentence.strip()
retext = modified_sentence.replace('Python', '파이썬')
print("-".join(retext.split()))



# 문제 11. 아이디 검사하기
# 다음 아이디가 모두 알파벳으로 이루어졌는지 확인하고, 모두 대문자인지와 모두 소문자인지를 각각 출력하시오.

#<답안> : .isalpha() .isupper() .islower() 
user_id = 'PYTHON'
print(user_id.isalpha())
print(user_id.isupper())
print(user_id.islower())


# 문제 12. 숫자 문자열 확인하기
# 다음 문자열들을 각각 검사하여 결과를 출력하시오.

#<답안>: isdecimal() .isdigit() .isnumeric()
data1 = '123'
data2 = '²'
data3 = '三'

# data1 ('123' - 일반 숫자)
print(data1.isdecimal())  # True
print(data1.isdigit())    # True
print(data1.isnumeric())  # True

# data2 ('²' - 위첨자)
print(data2.isdecimal())  # False
print(data2.isdigit())    # True
print(data2.isnumeric())  # True

# data3 ('三' - 한자 숫자)
print(data3.isdecimal())  # False
print(data3.isdigit())    # False
print(data3.isnumeric())  # True
