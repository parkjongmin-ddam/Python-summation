# Tuple 요소 접근하기
# Tuple 요소에 접근하는 방법은 Index를 사용하거나 Slicing을 사용할 수 있다.
# 이 외에도 반복문을 통해 요소에 접근할 수 있으며, Tuple unpacking을 사용할 수도 있다.

# ============================================================================
# Tuple 요소 접근 방법 비교표
# ============================================================================
# | 방법            | 설명                          | 예제                    | 특징                    |
# |----------------|------------------------------|------------------------|------------------------|
# | 인덱싱          | 특정 위치의 요소에 접근         | tuple[0]               | 단일 요소 반환           |
# | 슬라이싱        | 일부분 추출                    | tuple[1:4]              | 새로운 Tuple 반환        |
# | for 루프        | 모든 요소 순회                 | for x in tuple          | 순차적 접근             |
# | enumerate()     | 인덱스와 값 함께 순회           | for i, x in enumerate() | 인덱스와 값 동시 접근    |
# | 언패킹          | 여러 변수에 한 번에 할당         | x, y = tuple            | 여러 요소 동시 접근      |
# ============================================================================

# ============================================================================
# 1. 인덱싱(Indexing)을 사용하여 요소에 접근하기
# ============================================================================
# Tuple의 각 요소는 Index를 통해 접근할 수 있다 (첫번째 요소는 0번 Index, 두번째 요소는 1번 Index, ...)

basic_tuple = (1, 2, 3, 4, 5)

# 양수 인덱스: 앞에서부터 접근
first_element = basic_tuple[0] # basic_tuple의 첫번째 요소를 가져온다.
#print(first_element) # 1

second_element = basic_tuple[1] # basic_tuple의 두번째 요소를 가져온다.
#print(second_element) # 2

third_element = basic_tuple[2] # basic_tuple의 세번째 요소를 가져온다.
#print(third_element) # 3

# 음수 인덱스(Negative Indexing): 뒤에서부터 접근할 수 있다.
# -1은 마지막 요소, -2는 뒤에서 두번째 요소를 의미한다.
last_element = basic_tuple[-1] # basic_tuple의 마지막 요소를 가져온다.
#print(last_element) # 5

second_last = basic_tuple[-2] # basic_tuple의 뒤에서 두번째 요소를 가져온다.
#print(second_last) # 4

first_from_end = basic_tuple[-5] # basic_tuple의 뒤에서 다섯번째 요소를 가져온다. (첫번째 요소와 동일)
#print(first_from_end) # 1

# 인덱스 범위를 벗어나면 IndexError가 발생한다.
# element = basic_tuple[10] # IndexError: tuple index out of range

# ============================================================================
# 2. 슬라이싱(Slicing)을 사용하여 요소에 접근하기
# ============================================================================
# Tuple의 일부 요소를 가져오기 위해, Slicing을 사용할 수 있다.
# Slicing은 Tuple[start:stop:step] 형태로 사용할 수 있다.
# start: 시작 인덱스 (포함), stop: 종료 인덱스 (제외), step: 간격 (기본값 1)

basic_tuple = (1, 2, 3, 4, 5)

# ============================================================================
# 슬라이싱 패턴 정리표 (basic_tuple = (1, 2, 3, 4, 5))
# ============================================================================
# | 슬라이싱 문법        | 설명                                    | 결과          |
# |---------------------|----------------------------------------|--------------|
# | basic_tuple[0:3]    | 0번 인덱스부터 2번 인덱스까지 (stop 제외) | (1, 2, 3)    |
# | basic_tuple[:3]     | 처음부터 2번 인덱스까지                  | (1, 2, 3)    |
# | basic_tuple[1:]     | 1번 인덱스부터 끝까지                    | (2, 3, 4, 5) |
# | basic_tuple[:]      | 전체 Tuple 복사                         | (1, 2, 3, 4, 5) |
# | basic_tuple[0:5:2]  | 0번부터 4번까지 2칸씩                    | (1, 3, 5)    |
# | basic_tuple[::2]    | 처음부터 끝까지 2칸씩                    | (1, 3, 5)    |
# | basic_tuple[::-1]   | 전체를 역순으로                          | (5, 4, 3, 2, 1) |
# | basic_tuple[::-2]   | 역순으로 2칸씩                           | (5, 3, 1)    |
# | basic_tuple[-3:]    | 뒤에서 세번째부터 끝까지                 | (3, 4, 5)    |
# | basic_tuple[:-2]    | 처음부터 뒤에서 두번째 전까지             | (1, 2, 3)    |
# ============================================================================

# 기본 슬라이싱: [start:stop]
sub_tuple = basic_tuple[0:3] # basic_tuple의 0번 인덱스부터 2번 인덱스까지 추출한다. (stop은 제외)
#print(sub_tuple) # (1, 2, 3)

# 시작 인덱스 생략: 처음부터 추출
start_tuple = basic_tuple[:3] # basic_tuple의 처음부터 2번 인덱스까지 추출한다.
#print(start_tuple) # (1, 2, 3)

# 종료 인덱스 생략: 끝까지 추출
end_tuple = basic_tuple[1:] # basic_tuple의 1번 인덱스부터 끝까지 추출한다.
#print(end_tuple) # (2, 3, 4, 5)

# 시작과 종료 모두 생략: 전체 Tuple 복사
full_tuple = basic_tuple[:] # basic_tuple의 전체를 복사한다.
#print(full_tuple) # (1, 2, 3, 4, 5)

# Step 사용: [start:stop:step] - step만큼 건너뛰며 추출
step_tuple = basic_tuple[0:5:2] # basic_tuple의 0번 인덱스부터 4번 인덱스까지 2칸씩 추출한다.
#print(step_tuple) # (1, 3, 5)

step_tuple2 = basic_tuple[::2] # basic_tuple의 처음부터 끝까지 2칸씩 추출한다.
#print(step_tuple2) # (1, 3, 5)

# 음수 step 사용: 역순으로 추출
reversed_tuple = basic_tuple[::-1] # basic_tuple의 순서를 역순으로 추출한다.
#print(reversed_tuple) # (5, 4, 3, 2, 1)

reversed_step = basic_tuple[::-2] # basic_tuple를 역순으로 2칸씩 추출한다.
#print(reversed_step) # (5, 3, 1)

# 음수 인덱스 슬라이싱
negative_slice = basic_tuple[-3:] # basic_tuple의 뒤에서 세번째 요소부터 끝까지 추출한다.
#print(negative_slice) # (3, 4, 5)

negative_slice2 = basic_tuple[:-2] # basic_tuple의 처음부터 뒤에서 두번째 요소 전까지 추출한다.
#print(negative_slice2) # (1, 2, 3)

# 슬라이싱은 원본 Tuple을 변경하지 않고 새로운 Tuple을 생성한다.
original = (1, 2, 3, 4, 5)
sliced = original[1:4]
# sliced[0] = 99 # 에러 발생! Tuple은 불변 객체이므로 수정할 수 없다.

# ============================================================================
# 3. 중첩 Tuple의 요소에 접근하기
# ============================================================================
# Tuple 안에 Tuple이 있는 경우, 중첩 Tuple의 요소에 접근할 수 있다.

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# 첫번째 방법: 단계별로 접근
first_tuple = nested_tuple[0] # nested_tuple의 첫번째 Tuple을 추출한다.
#print(first_tuple) # (1, 2, 3)

element_1 = first_tuple[0] # first_tuple의 첫번째 요소를 추출한다.
#print(element_1) # 1

# 두번째 방법: 직접 접근 (더 간결함)
# nested_tuple[행][열] 형태로 접근할 수 있다.
element_2 = nested_tuple[0][0] # nested_tuple의 첫번째 Tuple의 첫번째 요소를 추출한다.
#print(element_2) # 1

element_3 = nested_tuple[0][1] # nested_tuple의 첫번째 Tuple의 두번째 요소를 추출한다.
#print(element_3) # 2

element_4 = nested_tuple[1][2] # nested_tuple의 두번째 Tuple의 세번째 요소를 추출한다.
#print(element_4) # 6

# 중첩 Tuple 슬라이싱
row_slice = nested_tuple[0:2] # nested_tuple의 첫번째와 두번째 행을 추출한다.
#print(row_slice) # ((1, 2, 3), (4, 5, 6))

# 특정 행의 일부 요소 추출
column_slice = nested_tuple[0][1:3] # nested_tuple의 첫번째 행에서 1번 인덱스부터 2번 인덱스까지 추출한다.
#print(column_slice) # (2, 3)

# ============================================================================
# 4. 반복문을 사용한 접근
# ============================================================================
# for 루프를 사용하여 Tuple의 모든 요소에 순차적으로 접근할 수 있다.

my_tuple = (1, 2, 3, 4, 5)

# 기본 for 루프
for element in my_tuple:
    #print(element) # 1, 2, 3, 4, 5를 순차적으로 출력
    pass

# enumerate()를 사용하여 인덱스와 값 함께 접근
for index, value in enumerate(my_tuple):
    #print(f"인덱스 {index}: 값 {value}") # 인덱스 0: 값 1, 인덱스 1: 값 2, ...
    pass

# range()와 len()을 사용한 인덱스 기반 접근
for i in range(len(my_tuple)):
    element = my_tuple[i]
    #print(f"인덱스 {i}: 값 {element}") # 인덱스 0: 값 1, 인덱스 1: 값 2, ...
    pass

# while 루프 사용
i = 0
while i < len(my_tuple):
    element = my_tuple[i]
    #print(element) # 1, 2, 3, 4, 5를 순차적으로 출력
    i += 1

# ============================================================================
# 5. Tuple Unpacking을 사용한 접근
# ============================================================================
# Tuple Unpacking은 Tuple의 요소를 여러 변수에 한 번에 할당하는 방법이다.

# 기본 언패킹
coordinates = (10, 20)
x, y = coordinates # Tuple의 요소를 각각 x, y에 할당
#print(x) # 10
#print(y) # 20

# 여러 요소 언패킹
person_info = ("Python", 30, "Developer")
name, age, job = person_info
#print(name) # Python
#print(age) # 30
#print(job) # Developer

# 일부만 언패킹 (나머지는 *로 처리)
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers # 첫 번째 요소와 나머지
#print(first) # 1
#print(rest) # [2, 3, 4, 5] (리스트로 반환됨)

first, *middle, last = numbers # 첫 번째, 중간, 마지막 요소
#print(first) # 1
#print(middle) # [2, 3, 4]
#print(last) # 5

# 함수에서 여러 값을 반환받을 때 유용
def get_coordinates():
    return (10, 20)

x, y = get_coordinates() # 함수가 반환한 Tuple을 언패킹
#print(x, y) # 10 20

# 변수 교환 (임시 변수 없이 가능)
a, b = 1, 2
a, b = b, a # a와 b의 값을 교환
#print(a) # 2
#print(b) # 1

# ============================================================================
# 6. 조건부 접근
# ============================================================================
# 조건에 따라 특정 요소에만 접근할 수 있다.

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 조건에 맞는 요소만 추출
even_numbers = tuple(x for x in my_tuple if x % 2 == 0) # 짝수만 추출
#print(even_numbers) # (2, 4, 6, 8, 10)

# 특정 조건을 만족하는 요소 찾기
greater_than_5 = tuple(x for x in my_tuple if x > 5) # 5보다 큰 수만 추출
#print(greater_than_5) # (6, 7, 8, 9, 10)

# ============================================================================
# 7. Tuple 메서드 및 함수
# ============================================================================
# Tuple은 불변 객체이므로 수정 메서드가 없지만, 몇 가지 유용한 메서드와 함수가 있다.

my_tuple = (1, 2, 3, 2, 4, 2, 5)

# count(): 특정 요소의 개수 세기
count_2 = my_tuple.count(2) # my_tuple에서 2의 개수를 반환한다.
#print(count_2) # 3

# index(): 특정 요소의 인덱스 찾기
index_3 = my_tuple.index(3) # my_tuple에서 3의 인덱스를 반환한다.
#print(index_3) # 2

# len(): Tuple의 길이 확인
length = len(my_tuple) # my_tuple의 길이를 반환한다.
#print(length) # 7

# in 연산자: 요소 포함 여부 확인
is_in = 3 in my_tuple # my_tuple에 3이 포함되어 있는지 확인한다.
#print(is_in) # True

# max(), min(), sum(): 최대값, 최소값, 합계
numeric_tuple = (1, 5, 3, 9, 2)
max_value = max(numeric_tuple) # 최대값
min_value = min(numeric_tuple) # 최소값
sum_value = sum(numeric_tuple) # 합계
#print(max_value) # 9
#print(min_value) # 1
#print(sum_value) # 20

# ============================================================================
# 주의사항
# ============================================================================
# 1. Tuple은 불변 객체이므로 슬라이싱으로 추출한 결과는 새로운 Tuple이다.
# 2. 인덱스 범위를 벗어나면 IndexError가 발생한다.
# 3. 중첩 Tuple의 경우 여러 단계의 인덱싱을 사용할 수 있다.
# 4. 언패킹 시 변수의 개수와 Tuple의 요소 개수가 일치해야 한다.
# 5. * 연산자를 사용하면 나머지 요소를 리스트로 받을 수 있다.
# ============================================================================