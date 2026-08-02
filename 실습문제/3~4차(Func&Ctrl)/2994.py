# built-in function len을 사용하지 않고, matrix의 총 길이를 matrix_len 변수에 담는다. 
# matrix_len 변수에 0을 할당한다. 
# for문을 사용하여 matrix 변수가 가진 요소를 모두 순회한다. 
# 각 요소를 순회할 때 마다 matrix_len 변수에 할당된 값을 1 증가 시킨다. 
# matrix_len 변수를 출력한다. 

# built-in function len을 사용하지 않고, matrix가 가진 각 요소의 길이를 출력한다. 
# for 문을 사용하여 matrix 변수가 가진 각 요소를 순회한다. 임시 변수 명은 number로 작성한다. 
# 이때, 각 요소들의 길이를 계산할 temporary_len 변수에 0을 할당한다. 
# matrix가 가진 각 요소들을 for문을 사용하여 순회한다. 
# 매 순회마다 temporary_len 변수에 할당된 값을 1 증가 시킨다. 
# temporary_len의 길이가 4 이하인 경우에 아래와 같은 형식으로 출력한다. 
# '{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.' 

# range와 len을 사용하여 matrix와 matrix가 가진 각 리스트들의 인덱스를 기준으로 순회할 수 있도록 for문을 작성한다. 
# 아래와 같은 형식으로 출력 될 수 있도록 코드를 작성한다. 
# 'matrix의 {x}, {y} 번째 요소의 값은 {matrix[x][y]} 입니다.'

#<문제>
matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]


#<답안>
matrix_len = 0
for i in matrix:
    matrix_len += 1

print (matrix_len)