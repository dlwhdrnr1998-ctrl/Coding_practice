#문자열의 길이 N과 길이 N만큼의 문자열 data_1이 주어진다. 
#N번만큼 반복하며 data_1에 담긴 문자열을 인덱스 번호 순대로 arr_1 리스트에 추가한다. 
#append 메서드를 활용한다. 
#arr_1 리스트를 출력한다. 

#문자열의 길이 M과 M개의 정수가 작성된 문자열 data_2가 주어진다. 
#data_2에 담긴 문자열을 공백을 기준으로 나누어 새로운 리스트 arr_2에 할당한다. 
#문자열 메서드 split을 활용한다. 
#arr_2가 가진 요소들을 순회하여 홀수만 차례대로 출력한다.  

N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for i in data_1 :
    arr_1.append(i)
   
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = data_2.split()
for i in arr_2 :
    if int(i) % 2 == 0 :
        continue
    else :
        print(i)











