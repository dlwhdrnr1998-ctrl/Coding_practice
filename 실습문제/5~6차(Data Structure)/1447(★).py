# 아래 함수를 수정하시오.
def union_sets(set1,set2):
    set_u = set1|set2
    return set_u

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print("최소 두개 넣어라")

    else: 
        result = set()
        for i in sets:
            result = result | i
        return result



result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다


# 주어진 세트에서 두 개의 셋을 합친 결과를 반환하는 union_sets 함수와
# 다수의 세트을 인자로 받아 합집합한 결과를 반환하는 union_multiple_sets 함수를 작성하시오.