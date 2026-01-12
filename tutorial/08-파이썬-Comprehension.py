# 파이썬에서 List의 요소에 접근하는 방법에는 매우 다양함
# 1. 인덱싱(Indexing) : List의 각 요소는 Index를 통해 접근할 수 있다 (첫번째 요소는 0번 Index, 두번째 요소는 1번 Index, ...)

# 기본적인 인덱싱 방법
# List의 요소는 0부터 시작하는 Index를 사용하여 접근할 수 있다.
basic_list = [1, 2, 3, 4, 5]
first_element = basic_list[0] # basic_list의 첫번째 요소를 가져온다.
#print(first_element) # 1

second_element = basic_list[1] # basic_list의 두번째 요소를 가져온다.
#print(second_element) # 2

third_element = basic_list[2] # basic_list의 세번째 요소를 가져온다.
#print(third_element) # 3

# 음수 인덱스(Negative Indexing) : 뒤에서부터 접근할 수 있다.
# -1은 마지막 요소, -2는 뒤에서 두번째 요소를 의미한다.
last_element = basic_list[-1] # basic_list의 마지막 요소를 가져온다.
#print(last_element) # 5

second_last = basic_list[-2] # basic_list의 뒤에서 두번째 요소를 가져온다.
#print(second_last) # 4

first_from_end = basic_list[-5] # basic_list의 뒤에서 다섯번째 요소를 가져온다. (첫번째 요소와 동일)
#print(first_from_end) # 1

# 인덱스 범위를 벗어나면 IndexError가 발생한다.
# element = basic_list[10] # IndexError: list index out of range

# 2. 슬라이싱(Slicing)
# List의 일부 요소를 가져오기 위해, Slicing을 사용할 수 있다.
# Slicing은 List[start:stop:step] 형태로 사용할 수 있다.
# start: 시작 인덱스 (포함), stop: 종료 인덱스 (제외), step: 간격 (기본값 1)

basic_list = [1, 2, 3, 4, 5]

# ============================================================================
# 슬라이싱 패턴 정리표
# ============================================================================
# | 슬라이싱 문법      | 설명                                    | 결과          |
# |-------------------|----------------------------------------|--------------|
# | basic_list[0:3]   | 0번 인덱스부터 2번 인덱스까지 (stop 제외) | [1, 2, 3]    |
# | basic_list[:3]    | 처음부터 2번 인덱스까지                  | [1, 2, 3]    |
# | basic_list[1:]     | 1번 인덱스부터 끝까지                    | [2, 3, 4, 5] |
# | basic_list[:]      | 전체 리스트 복사                         | [1, 2, 3, 4, 5] |
# | basic_list[0:5:2] | 0번부터 4번까지 2칸씩                    | [1, 3, 5]    |
# | basic_list[::2]   | 처음부터 끝까지 2칸씩                    | [1, 3, 5]    |
# | basic_list[::-1]   | 전체를 역순으로                          | [5, 4, 3, 2, 1] |
# | basic_list[::-2]   | 역순으로 2칸씩                           | [5, 3, 1]    |
# | basic_list[-3:]   | 뒤에서 세번째부터 끝까지                 | [3, 4, 5]    |
# | basic_list[:-2]   | 처음부터 뒤에서 두번째 전까지             | [1, 2, 3]    |
# ============================================================================

# 기본 슬라이싱 : [start:stop]
sub_list = basic_list[0:3] # basic_list의 0번 인덱스부터 2번 인덱스까지 추출한다. (stop은 제외)
#print(sub_list) # [1, 2, 3]

# 시작 인덱스 생략 : 처음부터 추출
start_list = basic_list[:3] # basic_list의 처음부터 2번 인덱스까지 추출한다.
#print(start_list) # [1, 2, 3]

# 종료 인덱스 생략 : 끝까지 추출
end_list = basic_list[1:] # basic_list의 1번 인덱스부터 끝까지 추출한다.
#print(end_list) # [2, 3, 4, 5]

# 시작과 종료 모두 생략 : 전체 리스트 복사
full_list = basic_list[:] # basic_list의 전체를 복사한다.
#print(full_list) # [1, 2, 3, 4, 5]

# Step 사용 : [start:stop:step] - step만큼 건너뛰며 추출
step_list = basic_list[0:5:2] # basic_list의 0번 인덱스부터 4번 인덱스까지 2칸씩 추출한다.
#print(step_list) # [1, 3, 5]

step_list2 = basic_list[::2] # basic_list의 처음부터 끝까지 2칸씩 추출한다.
#print(step_list2) # [1, 3, 5]

# 음수 step 사용 : 역순으로 추출
reversed_list = basic_list[::-1] # basic_list의 순서를 역순으로 추출한다.
#print(reversed_list) # [5, 4, 3, 2, 1]

reversed_step = basic_list[::-2] # basic_list를 역순으로 2칸씩 추출한다.
#print(reversed_step) # [5, 3, 1]

# 음수 인덱스 슬라이싱
negative_slice = basic_list[-3:] # basic_list의 뒤에서 세번째 요소부터 끝까지 추출한다.
#print(negative_slice) # [3, 4, 5]

negative_slice2 = basic_list[:-2] # basic_list의 처음부터 뒤에서 두번째 요소 전까지 추출한다.
#print(negative_slice2) # [1, 2, 3]

# 슬라이싱은 원본 리스트를 변경하지 않고 새로운 리스트를 생성한다.
original = [1, 2, 3, 4, 5]
sliced = original[1:4]
sliced[0] = 99 # sliced 리스트만 변경된다.
#print(original) # [1, 2, 3, 4, 5] (원본은 변경되지 않음)
#print(sliced) # [99, 3, 4]

# 3. 중첩 List (Nested List)
# List 안에 List가 있는 경우, 중첩 List의 요소에 접근할 수 있다.
# 2차원 리스트, 3차원 리스트 등 다차원 리스트를 만들 수 있다.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 첫번째 방법 : 단계별로 접근
first_list = nested_list[0] # nested_list의 첫번째 List를 추출한다.
#print(first_list) # [1, 2, 3]

element_1 = first_list[0] # first_list의 첫번째 요소를 추출한다.
#print(element_1) # 1

element_2 = first_list[1] # first_list의 두번째 요소를 추출한다.
#print(element_2) # 2

element_3 = first_list[2] # first_list의 세번째 요소를 추출한다.
#print(element_3) # 3

# 두번째 방법 : 직접 접근 (더 간결함)
# nested_list[행][열] 형태로 접근할 수 있다.
element_4 = nested_list[0][0] # nested_list의 첫번째 List의 첫번째 요소를 추출한다.
#print(element_4) # 1

element_5 = nested_list[0][1] # nested_list의 첫번째 List의 두번째 요소를 추출한다.
#print(element_5) # 2

element_6 = nested_list[1][2] # nested_list의 두번째 List의 세번째 요소를 추출한다.
#print(element_6) # 6

# 중첩 List 슬라이싱
row_slice = nested_list[0:2] # nested_list의 첫번째와 두번째 행을 추출한다.
#print(row_slice) # [[1, 2, 3], [4, 5, 6]]

# 특정 행의 일부 요소 추출
column_slice = nested_list[0][1:3] # nested_list의 첫번째 행에서 1번 인덱스부터 2번 인덱스까지 추출한다.
#print(column_slice) # [2, 3]

# 3차원 리스트 예제
three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
element_3d = three_d_list[0][1][0] # 첫번째 행의 두번째 열의 첫번째 요소
#print(element_3d) # 3

# 4. List 컴프리헨션(List Comprehension)
# List Comprehension을 사용하면, List의 요소에 대해 조건을 적용하거나 변형할 수 있다.
# 일반적인 for 루프보다 간결하고 읽기 쉬운 코드를 작성할 수 있다.
# 문법: [표현식 for 항목 in 반복가능객체 if 조건]

example_list = [10, 20, 30, 40, 50]

# 기본 List Comprehension : 각 요소를 변형
squared_list = [x**2 for x in example_list] # example_list의 요소를 제곱한다.
#print(squared_list) # [100, 400, 900, 1600, 2500]

# 조건문이 있는 List Comprehension : 조건을 만족하는 요소만 추출
even_list = [x for x in example_list if x % 2 == 0] # example_list의 요소 중 짝수인 요소를 추출한다.
#print(even_list) # [10, 20, 30, 40, 50] (모두 짝수이므로 전체 반환)

# 조건문이 있는 List Comprehension : 특정 조건을 만족하는 요소만 추출
greater_than_30 = [x for x in example_list if x > 30] # 30보다 큰 요소만 추출한다.
#print(greater_than_30) # [40, 50]

# 조건문과 변형을 함께 사용
squared_even = [x**2 for x in example_list if x % 2 == 0] # 짝수를 제곱한다.
#print(squared_even) # [100, 400, 900, 1600, 2500]

# 문자열 리스트 예제
words = ["python", "java", "javascript", "c++"]
upper_words = [word.upper() for word in words] # 모든 단어를 대문자로 변환한다.
#print(upper_words) # ['PYTHON', 'JAVA', 'JAVASCRIPT', 'C++']

long_words = [word for word in words if len(word) > 4] # 길이가 4보다 긴 단어만 추출한다.
#print(long_words) # ['python', 'javascript']

# 중첩 List Comprehension : 중첩된 리스트를 생성할 수 있다.
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
#print(matrix) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 조건문이 여러 개인 경우
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in numbers if x % 2 == 0 if x > 5] # 짝수이면서 5보다 큰 수
#print(filtered) # [6, 8, 10]

# if-else를 사용한 조건부 표현식
result = [x if x % 2 == 0 else x*2 for x in range(1, 6)] # 짝수는 그대로, 홀수는 2배
#print(result) # [2, 2, 6, 4, 10]

# 일반 for 루프와 비교
# List Comprehension 사용 (간결함)
squared = [x**2 for x in range(5)]
#print(squared) # [0, 1, 4, 9, 16]

# 일반 for 루프 사용 (동일한 결과)
squared_loop = []
for x in range(5):
    squared_loop.append(x**2)
#print(squared_loop) # [0, 1, 4, 9, 16]
