"""
2つの指数を3乗して求められる数字を1つ、組み合わせを2つ
Input: 1, 2 => [(1729, [(1,12), (9,10)])]
Input: 2, 2 => [(1729, [(1,12), (9,10)]), (4140, [(2,16), (9,15)])]
Input: 1, 3 => [(87539319, [(167, 436), (228, 423), (255, 414)])]
"""
from collections import defaultdict
from typing import List, Tuple

"""
max_answer_num: 2つの指数を3乗して求められる数字
match_answer_num: 2つの指数を3乗して求められる組み合わせ 解
"""
def taxi_cab_number(max_answer_num: int, match_answer_num: int = 2, start_answer: int = 1) -> List[Tuple[int, List[Tuple[int,int]]]]:
    result = []
    got_answer_count = 0
    answer = start_answer

    while got_answer_count < max_answer_num:
        match_answer_count = 0
        memo = defaultdict(list)

        max_param = int(pow(answer, 1.0 / 3)) + 1
        for x in range(1, max_param):
            for y in range(x+1, max_param):
                if x ** 3 + y ** 3 == answer:
                    match_answer_count += 1
                    memo[answer].append((x,y))

        if match_answer_count == match_answer_num:
            result.append((answer, memo[answer]))
            got_answer_count += 1

        answer += 1
    return result

if __name__ == '__main__':
    print(taxi_cab_number(1, 2))