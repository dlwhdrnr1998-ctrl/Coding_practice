#<문제>
# A = ['J', 'U', 'N', 'G', 'O','L']로 초기화 한 후, 
# 문자를 한 개 입력받아 리스트에서의 위치를 출력하는 프로그램을 작성하시오. 
# 첫 번째 위치는 0번이며 리스트에 없는 문자가 입력되면 "none"라는 메시지를 출력한다.

#<내 답안> : .index() 메서드 활용
A = ['J', 'U', 'N', 'G', 'O','L']
string = str(input("문자를 입력하세요 : "))


if string in A :
    result = A.index(string)
    print(result)


#<다른 방식> : for문 활용
# idea : for문으로 하나하나 비교해서 결과가 같으면 뽑아내는 시스템
#      : 입력값은 string이니, string을 기준으로
#      : 리스트 A의 인덱스 값에 따른 해당 요소와 비교하는 아이디어

for i in range(len(A)):
    if A[i] == string : 
        print (i)