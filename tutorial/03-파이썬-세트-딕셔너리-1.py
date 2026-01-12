# Set(집합) 자료형
# Set은 Python에서 사용하는 중복되지 않는 고유한 요소들의 모음을 저장하는 자료형이다.
# Set은 중괄호 {} 를 사용하여 표현한다 (Dictionary와 구분하기 위해 빈 Set은 set() 함수 사용).
# Set은 아래와 같은 특징을 가지고 있다:
# 중복 불가: Set 내에서 각 요소는 고유해야 하며, 동일한 요소가 중복될 수 없다.
# 순서 없음: Set은 요소의 순서를 보장하지 않는다 (Python 3.7+ 에서는 삽입 순서가 유지되지만, 공식적으로는 순서가 없다고 간주).
# 가변성(Mutable): Set은 요소의 추가, 삭제가 가능하다.
# 요소의 불변성: Set의 요소는 불변(immutable) 객체만 가능하다 (문자열, 숫자, 튜플 등).
# 수학적 집합 연산: 교집합, 합집합, 차집합 등의 연산을 지원한다.

# ============================================================================
# Set vs List vs Tuple vs Dictionary 비교표
# ============================================================================
# | 특징          | Set                      | List                        | Tuple                      | Dictionary                |
# |--------------|--------------------------|----------------------------|---------------------------|--------------------------|
# | 문법          | 중괄호 {} 사용 (set()로 생성) | 대괄호 [] 사용              | 소괄호 () 사용              | 중괄호 {} 사용             |
# | 구조          | 고유한 요소 모음            | 순서 있는 요소 나열          | 순서 있는 요소 나열        | 키-값 쌍                  |
# | 중복 허용      | 불가능                     | 가능                        | 가능                        | 키는 불가능, 값은 가능     |
# | 순서 보장      | 없음 (Python 3.7+ 삽입 순서) | 있음                        | 있음                        | 있음 (Python 3.7+)        |
# | 가변성        | 가변 (Mutable)            | 가변 (Mutable)              | 불변 (Immutable)           | 가변 (Mutable)            |
# | 요소 수정     | 불가능 (추가/삭제만 가능)    | 가능                        | 불가능                     | 가능                      |
# | 요소 추가     | 가능                      | 가능                        | 불가능                     | 가능                      |
# | 요소 삭제     | 가능                      | 가능                        | 불가능                     | 가능                      |
# | 요소 타입      | 불변 객체만 가능            | 모든 타입 가능               | 모든 타입 가능              | 키는 불변, 값은 모든 타입  |
# | 검색 속도     | 매우 빠름 (O(1))          | 느림 (O(n))                | 느림 (O(n))                | 매우 빠름 (O(1))          |
# | 집합 연산     | 지원 (교집합, 합집합 등)    | 미지원                      | 미지원                      | 미지원                    |
# | 사용 시나리오  | 중복 제거, 멤버십 테스트     | 변경 가능한 데이터 모음      | 고정된 데이터, 딕셔너리 키   | 키-값 매핑, JSON 데이터    |
# ============================================================================

# ============================================================================
# Set 생성 방법
# ============================================================================

# 빈 Set 생성
# 주의: {} 는 빈 Dictionary를 생성한다. 빈 Set을 생성하려면 set() 함수를 사용해야 한다.
empty_set = set() # set() 함수를 사용하여 빈 Set을 생성한다.
#print(empty_set) # set()
#print(type(empty_set)) # <class 'set'>

# 빈 Dictionary와 구분
empty_dict = {} # {} 는 빈 Dictionary를 생성한다.
#print(type(empty_dict)) # <class 'dict'>

# 기본적인 Set 생성
# Set은 중괄호 안에 요소를 콤마로 구분하여 생성한다.
my_set = {1, 2, 3, 4, 5}
#print(my_set) # {1, 2, 3, 4, 5} (순서는 보장되지 않을 수 있음)

# 문자열 Set 생성
string_set = {"apple", "banana", "cherry"}
#print(string_set) # {'apple', 'banana', 'cherry'}

# 다양한 데이터 타입을 포함하는 Set 생성
# 주의: Set의 요소는 불변 객체만 가능하다.
datatypes_set = {1, "apple", 3.14, True, (1, 2, 3)} # 튜플은 불변 객체이므로 가능
#print(datatypes_set)

# List는 Set의 요소로 사용할 수 없다 (가변 객체)
# invalid_set = {1, [2, 3]} # TypeError: unhashable type: 'list'

# set() 함수를 사용한 생성
set_from_list = set([1, 2, 3, 4, 5]) # 리스트로부터 Set 생성
#print(set_from_list) # {1, 2, 3, 4, 5}

set_from_string = set("hello") # 문자열로부터 Set 생성 (중복 제거됨)
#print(set_from_string) # {'h', 'e', 'l', 'o'} (중복된 'l'이 제거됨)

set_from_tuple = set((1, 2, 3, 4, 5)) # 튜플로부터 Set 생성
#print(set_from_tuple) # {1, 2, 3, 4, 5}

# Set Comprehension을 사용한 생성
set_comprehension = {x for x in range(1, 6)} # 1부터 5까지의 Set
#print(set_comprehension) # {1, 2, 3, 4, 5}

# 조건부 Set Comprehension
even_set = {x for x in range(1, 11) if x % 2 == 0} # 짝수만 포함
#print(even_set) # {2, 4, 6, 8, 10}

# ============================================================================
# Set의 주요 특징: 중복 제거
# ============================================================================
# Set은 자동으로 중복된 요소를 제거한다.

duplicate_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_set = set(duplicate_list) # 중복이 자동으로 제거된다.
#print(unique_set) # {1, 2, 3, 4}

# 리스트에서 중복 제거하기
original_list = [1, 2, 2, 3, 3, 3]
unique_list = list(set(original_list)) # Set으로 변환 후 다시 리스트로 변환
#print(unique_list) # [1, 2, 3] (순서는 보장되지 않을 수 있음)

# ============================================================================
# Set 요소 접근하기
# ============================================================================
# Set은 인덱싱이나 슬라이싱을 지원하지 않는다 (순서가 없기 때문).

my_set = {1, 2, 3, 4, 5}

# 인덱싱 불가능
# element = my_set[0] # TypeError: 'set' object is not subscriptable

# 슬라이싱 불가능
# subset = my_set[1:3] # TypeError: 'set' object is not subscriptable

# in 연산자로 요소 존재 여부 확인
is_present = 3 in my_set # 3이 my_set에 있는지 확인한다.
#print(is_present) # True

is_not_present = 10 in my_set # 10이 my_set에 없는지 확인한다.
#print(is_not_present) # False

# not in 연산자 사용
is_absent = 10 not in my_set # 10이 my_set에 없는지 확인한다.
#print(is_absent) # True

# ============================================================================
# Set 요소 추가하기
# ============================================================================

my_set = {1, 2, 3}

# add() 메서드: 단일 요소 추가
my_set.add(4) # 4를 my_set에 추가한다.
#print(my_set) # {1, 2, 3, 4}

my_set.add(2) # 이미 존재하는 요소를 추가하려고 하면 무시된다.
#print(my_set) # {1, 2, 3, 4} (변화 없음)

# update() 메서드: 여러 요소 추가
my_set.update([5, 6, 7]) # 리스트의 요소들을 추가한다.
#print(my_set) # {1, 2, 3, 4, 5, 6, 7}

my_set.update({8, 9}) # 다른 Set의 요소들을 추가한다.
#print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.update((10, 11)) # 튜플의 요소들을 추가한다.
#print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# ============================================================================
# Set 요소 삭제하기
# ============================================================================

my_set = {1, 2, 3, 4, 5}

# remove() 메서드: 요소 삭제 (요소가 없으면 KeyError 발생)
my_set.remove(3) # 3을 my_set에서 삭제한다.
#print(my_set) # {1, 2, 4, 5}

# 요소가 없으면 KeyError 발생
# my_set.remove(10) # KeyError: 10

# discard() 메서드: 요소 삭제 (요소가 없어도 에러 발생하지 않음)
my_set.discard(4) # 4를 my_set에서 삭제한다.
#print(my_set) # {1, 2, 5}

my_set.discard(10) # 존재하지 않는 요소를 삭제하려고 해도 에러가 발생하지 않는다.
#print(my_set) # {1, 2, 5} (변화 없음)

# pop() 메서드: 임의의 요소를 반환하고 삭제
# 주의: Set은 순서가 없으므로 어떤 요소가 삭제될지 예측할 수 없다.
popped_element = my_set.pop() # 임의의 요소를 반환하고 삭제한다.
#print(popped_element) # 1, 2, 또는 5 중 하나
#print(my_set) # 나머지 요소들

# clear() 메서드: 모든 요소 삭제
my_set.clear() # my_set의 모든 요소를 삭제한다.
#print(my_set) # set()

# ============================================================================
# Set 주요 메서드 및 함수
# ============================================================================
# ============================================================================
# Set 메서드 정리표
# ============================================================================
# | 메서드/함수     | 설명                          | 예제                        | 반환값              |
# |---------------|------------------------------|---------------------------|-------------------|
# | add()         | 단일 요소 추가                 | set.add(element)           | None               |
# | update()      | 여러 요소 추가                 | set.update(iterable)       | None               |
# | remove()      | 요소 삭제 (없으면 KeyError)    | set.remove(element)        | None               |
# | discard()     | 요소 삭제 (없어도 에러 없음)    | set.discard(element)        | None               |
# | pop()         | 임의 요소 반환 후 삭제          | set.pop()                  | 요소 값             |
# | clear()       | 모든 요소 삭제                 | set.clear()                | None               |
# | copy()        | Set 복사                       | set.copy()                 | 새로운 Set         |
# | len()         | 요소 개수                      | len(set)                   | 정수               |
# | in            | 요소 존재 여부 확인              | element in set             | True/False         |
# | union()       | 합집합                         | set1.union(set2)           | 새로운 Set         |
# | intersection()| 교집합                        | set1.intersection(set2)    | 새로운 Set         |
# | difference()  | 차집합                         | set1.difference(set2)       | 새로운 Set         |
# | symmetric_difference() | 대칭 차집합      | set1.symmetric_difference(set2) | 새로운 Set |
# | issubset()    | 부분집합 여부 확인              | set1.issubset(set2)         | True/False         |
# | issuperset()  | 상위집합 여부 확인              | set1.issuperset(set2)       | True/False         |
# | isdisjoint()  | 교집합이 없는지 확인            | set1.isdisjoint(set2)       | True/False         |
# ============================================================================

my_set = {1, 2, 3, 4, 5}

# copy(): Set 복사
copied_set = my_set.copy() # my_set을 복사하여 새로운 Set을 생성한다.
#print(copied_set) # {1, 2, 3, 4, 5}

# len(): Set의 요소 개수
length = len(my_set) # my_set의 요소 개수를 반환한다.
#print(length) # 5

# ============================================================================
# Set 집합 연산
# ============================================================================

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 합집합 (Union)
union1 = set1.union(set2) # set1과 set2의 합집합
#print(union1) # {1, 2, 3, 4, 5, 6, 7, 8}

union2 = set1 | set2 # | 연산자를 사용한 합집합
#print(union2) # {1, 2, 3, 4, 5, 6, 7, 8}

# 교집합 (Intersection)
intersection1 = set1.intersection(set2) # set1과 set2의 교집합
#print(intersection1) # {4, 5}

intersection2 = set1 & set2 # & 연산자를 사용한 교집합
#print(intersection2) # {4, 5}

# 차집합 (Difference)
difference1 = set1.difference(set2) # set1에서 set2를 뺀 차집합
#print(difference1) # {1, 2, 3}

difference2 = set1 - set2 # - 연산자를 사용한 차집합
#print(difference2) # {1, 2, 3}

# 대칭 차집합 (Symmetric Difference)
# 두 집합 중 하나에만 있는 요소들
symmetric_diff1 = set1.symmetric_difference(set2) # set1과 set2의 대칭 차집합
#print(symmetric_diff1) # {1, 2, 3, 6, 7, 8}

symmetric_diff2 = set1 ^ set2 # ^ 연산자를 사용한 대칭 차집합
#print(symmetric_diff2) # {1, 2, 3, 6, 7, 8}

# ============================================================================
# Set 집합 관계 확인
# ============================================================================

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

# issubset(): 부분집합 여부 확인
is_subset = set1.issubset(set2) # set1이 set2의 부분집합인지 확인한다.
#print(is_subset) # True

is_subset2 = set1 <= set2 # <= 연산자를 사용한 부분집합 확인
#print(is_subset2) # True

# issuperset(): 상위집합 여부 확인
is_superset = set2.issuperset(set1) # set2가 set1의 상위집합인지 확인한다.
#print(is_superset) # True

is_superset2 = set2 >= set1 # >= 연산자를 사용한 상위집합 확인
#print(is_superset2) # True

# isdisjoint(): 교집합이 없는지 확인
is_disjoint = set1.isdisjoint(set3) # set1과 set3의 교집합이 없는지 확인한다.
#print(is_disjoint) # True

is_disjoint2 = set1.isdisjoint(set2) # set1과 set2는 교집합이 있다.
#print(is_disjoint2) # False

# ============================================================================
# Set 순회하기
# ============================================================================
# Set의 모든 요소를 순회할 수 있다.

my_set = {1, 2, 3, 4, 5}

# 기본 for 루프
for element in my_set:
    #print(element) # 각 요소를 순차적으로 출력 (순서는 보장되지 않을 수 있음)
    pass

# enumerate()와 함께 사용
for index, element in enumerate(my_set):
    #print(f"인덱스 {index}: {element}")
    pass

# Set Comprehension과 함께 사용
doubled_set = {x * 2 for x in my_set} # 각 요소를 2배
#print(doubled_set) # {2, 4, 6, 8, 10}

# ============================================================================
# Set 활용 예제
# ============================================================================

# 예제 1: 리스트에서 중복 제거
original_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(original_list)) # Set으로 변환 후 다시 리스트로 변환
#print(unique_list) # [1, 2, 3, 4]

# 예제 2: 두 리스트의 공통 요소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2)) # 교집합
#print(common) # [4, 5]

# 예제 3: 두 리스트의 차이점 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
only_in_list1 = list(set(list1) - set(list2)) # list1에만 있는 요소
#print(only_in_list1) # [1, 2, 3]

only_in_list2 = list(set(list2) - set(list1)) # list2에만 있는 요소
#print(only_in_list2) # [6, 7, 8]

# 예제 4: 빠른 멤버십 테스트
large_list = list(range(1000000))
large_set = set(large_list)

# Set을 사용한 멤버십 테스트 (매우 빠름)
# is_present = 999999 in large_set # O(1) 시간 복잡도

# List를 사용한 멤버십 테스트 (느림)
# is_present = 999999 in large_list # O(n) 시간 복잡도

# ============================================================================
# 주의사항
# ============================================================================
# 1. Set의 요소는 불변 객체만 가능하다 (문자열, 숫자, 튜플 등).
#    List는 Set의 요소로 사용할 수 없다: invalid_set = {1, [2, 3]} # TypeError
#
# 2. Set은 순서를 보장하지 않는다 (Python 3.7+ 에서는 삽입 순서가 유지되지만 공식적으로는 순서가 없다고 간주).
#
# 3. Set은 인덱싱이나 슬라이싱을 지원하지 않는다.
#
# 4. 빈 Set을 생성할 때는 set() 함수를 사용해야 한다. {} 는 빈 Dictionary를 생성한다.
#
# 5. add() 메서드는 단일 요소만 추가할 수 있다. 여러 요소를 추가하려면 update() 메서드를 사용해야 한다.
#
# 6. remove() 메서드는 요소가 없으면 KeyError를 발생시키지만, discard() 메서드는 에러를 발생시키지 않는다.
#
# 7. pop() 메서드는 임의의 요소를 반환하므로, 어떤 요소가 삭제될지 예측할 수 없다.
# ============================================================================
