'''잘못된 문장이 작성된 문자열 original_word, 제거할 대상이 작성된 word 문자열과 빈 리스트 arr이 주어진다. 
original_word 변수에 담긴 각 문자열을 모두 나누어 arr 리스트에 담는다. 
extend 메서드를 활용한다. 
arr 리스트를 출력한다. 

문장에서 잘못된 내용을 제거하는 함수 restructure_word 함수를 작성한. 
인자로 넘겨받은 word 문자열을 순회하며 아래 조건에 맞춰 arr에서 불필요한 문자열을 제거한다. 
만약 순회중인 문자열이 숫자라면, 해당 숫자 만큼 반복하여 arr의 마지막 요소를 제거한다. 
isdecimal 메서드와 pop 메서드를 활용한다. 
그 외의 경우, arr에서 해당 문자열을 제거한다. 
remove 메서드를 활용한다. 
불필요한 문자를 제거한 arr를 반환한다. 
함수 호출 결과를 result 변수에 담고 result를 출력한다. 

result에 할당된 리스트를 하나의 문자열로 변환하여 출력한다. 
join 메서드를 활용한다.
'''

def restructure_word(word, arr):
    pass

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
bridge = original_word.split()
arr.append(bridge)

print(arr)
result = restructure_word(word, arr)
