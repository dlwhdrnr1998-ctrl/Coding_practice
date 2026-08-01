#  주어진 리스트에서 중복된 요소를 제거한 새로운 리스트를 반환하는 remove_duplicates 함수를 작성하시오. 
# 리스트를 인자로 받아 중복이 제거된 새로운 리스트를 반환해야 한다.

# 아래 함수를 수정하시오.
def remove_duplicates(some_list):


    return  list(set(some_list))


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
