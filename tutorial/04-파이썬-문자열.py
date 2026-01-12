# 문자열(String) 자료형
# 문자열은 문자들의 나열로, 텍스트 데이터를 표현하는 데 사용된다.
# 문자열은 불변성(Immutable)을 가지며, 한 번 생성된 문자열은 변경할 수 없다.
# 문자열은 따옴표로 감싸서 표현하며, 큰따옴표("), 작은따옴표('), 삼중 따옴표(""" 또는 ''')를 사용할 수 있다.

# 문자열 생성 방법

# 큰따옴표(")를 사용한 문자열 생성
a = "Hello World"
#print(a) # Hello World

# 작은따옴표(')를 사용한 문자열 생성
b = 'Python is easy'
#print(b) # Python is easy

# 삼중 따옴표(""" """)를 사용한 문자열 생성 (여러 줄 문자열)
c = """Life is too short, 
you need python"""
#print(c) # 여러 줄로 출력된다.

# 문자열 내 따옴표 포함하기
# 작은따옴표를 포함하려면 큰따옴표로 감싼다.
d = "Python's favorite food is perl"
#print(d) # Python's favorite food is perl

# 큰따옴표를 포함하려면 작은따옴표로 감싼다.
e = 'He said "Hello" to me'
#print(e) # He said "Hello" to me

# 이스케이프 문자 사용하기
# ============================================================================
# 이스케이프 문자 정리표
# ============================================================================
# | 이스케이프 문자 | 의미              | 예제                    | 결과              |
# |---------------|------------------|------------------------|------------------|
# | \n            | 줄바꿈 (New Line)  | "Hello\nWorld"         | Hello와 World가 두 줄로 출력 |
# | \t            | 탭 (Tab)          | "Hello\tWorld"         | Hello와 World 사이에 탭 |
# | \\            | 백슬래시 자체      | "C:\\Users\\Python"    | C:\Users\Python  |
# | \'            | 작은따옴표         | 'It\'s a day'          | It's a day       |
# | \"            | 큰따옴표           | "He said \"Hello\""    | He said "Hello"  |
# | \r            | 캐리지 리턴        | "Hello\rWorld"         | World (덮어쓰기)  |
# | \b            | 백스페이스          | "Hello\bWorld"         | HellWorld        |
# | \f            | 폼 피드            | "Hello\fWorld"         | 페이지 나누기    |
# ============================================================================

# \n : 줄바꿈 (New Line)
f = "Hello\nWorld"
#print(f) # Hello와 World가 두 줄로 출력된다.

# \t : 탭 (Tab)
g = "Hello\tWorld"
#print(g) # Hello와 World 사이에 탭이 들어간다.

# \\ : 백슬래시 자체를 표현
h = "C:\\Users\\Python"
#print(h) # C:\Users\Python

# \' : 작은따옴표를 문자열 내에서 표현
i = 'It\'s a beautiful day'
#print(i) # It's a beautiful day

# \" : 큰따옴표를 문자열 내에서 표현
j = "He said \"Hello\""
#print(j) # He said "Hello"

# 문자열 연결하기 (Concatenation) : + 연산자를 사용하여 문자열을 연결할 수 있다.
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2 # 두 문자열을 공백과 함께 연결한다.
#print(result) # Hello World

# 문자열 반복하기 : * 연산자를 사용하여 문자열을 반복할 수 있다.
str3 = "Python "
repeated = str3 * 3 # str3를 3번 반복한다.
#print(repeated) # Python Python Python 

# 문자열 인덱싱(Indexing) : 문자열의 각 문자는 인덱스를 통해 접근할 수 있다.
# 첫 번째 문자는 0번 인덱스, 두 번째 문자는 1번 인덱스, ...
text = "Python"
first_char = text[0] # 첫 번째 문자를 가져온다.
#print(first_char) # P

last_char = text[-1] # 마지막 문자를 가져온다. (음수 인덱스 사용)
#print(last_char) # n

# 문자열 슬라이싱(Slicing) : 문자열의 일부분을 추출할 수 있다.
# ============================================================================
# 문자열 슬라이싱 패턴 정리표 (text = "Python")
# ============================================================================
# | 슬라이싱 문법    | 설명                        | 결과      |
# |----------------|----------------------------|----------|
# | text[0:3]      | 0번 인덱스부터 2번 인덱스까지  | "Pyt"    |
# | text[:3]       | 처음부터 2번 인덱스까지        | "Pyt"    |
# | text[3:]       | 3번 인덱스부터 끝까지          | "hon"    |
# | text[:]        | 전체 문자열 복사               | "Python" |
# | text[0:6:2]    | 0번부터 5번까지 2칸씩          | "Pto"    |
# | text[::-1]     | 전체를 역순으로                | "nohtyP" |
# | text[-3:]      | 뒤에서 세번째부터 끝까지        | "hon"    |
# | text[:-2]      | 처음부터 뒤에서 두번째 전까지   | "Pyth"   |
# ============================================================================

text = "Python"
substring1 = text[0:3] # 0번 인덱스부터 2번 인덱스까지 추출한다.
#print(substring1) # Pyt

substring2 = text[:3] # 처음부터 2번 인덱스까지 추출한다.
#print(substring2) # Pyt

substring3 = text[3:] # 3번 인덱스부터 끝까지 추출한다.
#print(substring3) # hon

substring4 = text[:] # 전체 문자열을 추출한다.
#print(substring4) # Python

# 문자열 길이 확인하기 : len() 함수를 사용하여 문자열의 길이를 확인할 수 있다.
text = "Python"
length = len(text) # text의 길이를 반환한다.
#print(length) # 6

# 문자열 대소문자 변환하기
# ============================================================================
# 대소문자 변환 메서드 정리표
# ============================================================================
# | 메서드        | 설명                          | 예제              | 결과              |
# |--------------|------------------------------|------------------|------------------|
# | upper()      | 모든 문자를 대문자로 변환        | "python".upper() | "PYTHON"         |
# | lower()      | 모든 문자를 소문자로 변환        | "PYTHON".lower() | "python"         |
# | capitalize() | 첫 글자만 대문자로 변환          | "python".capitalize() | "Python"     |
# | title()      | 각 단어의 첫 글자를 대문자로 변환 | "python is".title() | "Python Is"  |
# | swapcase()   | 대소문자를 서로 바꿈             | "PyThOn".swapcase() | "pYtHoN"    |
# ============================================================================

# upper() 메서드를 사용하여 문자열을 대문자로 변환할 수 있다.
text = "python"
upper_text = text.upper() # text를 대문자로 변환한다.
#print(upper_text) # PYTHON

# lower() 메서드를 사용하여 문자열을 소문자로 변환할 수 있다.
text = "PYTHON"
lower_text = text.lower() # text를 소문자로 변환한다.
#print(lower_text) # python

# capitalize() 메서드를 사용하여 첫 글자만 대문자로 변환할 수 있다.
text = "python"
capitalized_text = text.capitalize() # 첫 글자만 대문자로 변환한다.
#print(capitalized_text) # Python

# title() 메서드를 사용하여 각 단어의 첫 글자를 대문자로 변환할 수 있다.
text = "python is easy"
title_text = text.title() # 각 단어의 첫 글자를 대문자로 변환한다.
#print(title_text) # Python Is Easy

# swapcase() 메서드를 사용하여 대소문자를 서로 바꿀 수 있다.
text = "PyThOn"
swapped_text = text.swapcase() # 대소문자를 서로 바꾼다.
#print(swapped_text) # pYtHoN

# 문자열 공백 제거하기
# ============================================================================
# 공백 제거 메서드 정리표 (text = "  Python  ")
# ============================================================================
# | 메서드    | 설명              | 예제              | 결과            |
# |----------|------------------|------------------|----------------|
# | strip()  | 양쪽 공백 제거     | text.strip()     | "Python"       |
# | lstrip() | 왼쪽 공백 제거     | text.lstrip()    | "Python  "     |
# | rstrip() | 오른쪽 공백 제거   | text.rstrip()    | "  Python"     |
# ============================================================================

# strip() 메서드를 사용하여 문자열 양쪽의 공백을 제거할 수 있다.
text = "  Python  "
stripped_text = text.strip() # 양쪽 공백을 제거한다.
#print(stripped_text) # Python

# lstrip() 메서드를 사용하여 문자열 왼쪽의 공백을 제거할 수 있다.
text = "  Python  "
left_stripped = text.lstrip() # 왼쪽 공백을 제거한다.
#print(left_stripped) # Python  (오른쪽 공백은 남아있음)

# rstrip() 메서드를 사용하여 문자열 오른쪽의 공백을 제거할 수 있다.
text = "  Python  "
right_stripped = text.rstrip() # 오른쪽 공백을 제거한다.
#print(right_stripped) #   Python (왼쪽 공백은 남아있음)

# 문자열 찾기 및 검색하기
# ============================================================================
# 문자열 검색 메서드 정리표 (text = "Python is easy")
# ============================================================================
# | 메서드/연산자 | 설명                          | 예제                | 결과      | 오류 처리        |
# |--------------|------------------------------|---------------------|----------|----------------|
# | find()       | 처음 나타나는 위치 찾기        | text.find("is")     | 7        | 없으면 -1 반환  |
# | index()      | 처음 나타나는 위치 찾기        | text.index("is")    | 7        | 없으면 ValueError |
# | count()      | 나타나는 횟수 세기             | text.count("Python")| 1        | 없으면 0 반환   |
# | in           | 포함 여부 확인 (True/False)    | "Python" in text    | True     | 없으면 False    |
# | startswith() | 시작 문자열 확인               | text.startswith("Py")| True    | 없으면 False    |
# | endswith()   | 끝 문자열 확인                 | text.endswith("easy")| True    | 없으면 False    |
# ============================================================================

# find() 메서드를 사용하여 특정 문자열이 처음 나타나는 위치를 찾을 수 있다.
text = "Python is easy"
position = text.find("is") # "is"가 처음 나타나는 위치를 반환한다.
#print(position) # 7

# find() 메서드는 찾는 문자열이 없으면 -1을 반환한다.
position = text.find("Java")
#print(position) # -1

# index() 메서드를 사용하여 특정 문자열이 처음 나타나는 위치를 찾을 수 있다.
# find()와 달리 찾는 문자열이 없으면 에러가 발생한다.
text = "Python is easy"
position = text.index("is") # "is"가 처음 나타나는 위치를 반환한다.
#print(position) # 7

# count() 메서드를 사용하여 특정 문자열이 나타나는 횟수를 셀 수 있다.
text = "Python is easy, Python is fun"
count = text.count("Python") # "Python"이 나타나는 횟수를 반환한다.
#print(count) # 2

# in 연산자를 사용하여 특정 문자열이 포함되어 있는지 확인할 수 있다.
text = "Python is easy"
is_in = "Python" in text # text에 "Python"이 포함되어 있는지 확인한다.
#print(is_in) # True

# 문자열 치환하기 : replace() 메서드를 사용하여 문자열의 일부분을 다른 문자열로 치환할 수 있다.
text = "Python is easy"
replaced_text = text.replace("easy", "fun") # "easy"를 "fun"으로 치환한다.
#print(replaced_text) # Python is fun

# 문자열 분리하기 : split() 메서드를 사용하여 문자열을 특정 구분자로 분리할 수 있다.
text = "Python,Java,JavaScript"
split_list = text.split(",") # 쉼표를 기준으로 문자열을 분리한다.
#print(split_list) # ['Python', 'Java', 'JavaScript']

# 기본적으로 split()은 공백을 기준으로 분리한다.
text = "Python is easy"
split_list = text.split() # 공백을 기준으로 문자열을 분리한다.
#print(split_list) # ['Python', 'is', 'easy']

# 문자열 결합하기 : join() 메서드를 사용하여 리스트의 요소들을 문자열로 결합할 수 있다.
words = ["Python", "is", "easy"]
joined_text = " ".join(words) # 공백을 구분자로 words 리스트의 요소들을 결합한다.
#print(joined_text) # Python is easy

# 다른 구분자로도 결합할 수 있다.
words = ["Python", "Java", "JavaScript"]
joined_text = ", ".join(words) # ", "를 구분자로 words 리스트의 요소들을 결합한다.
#print(joined_text) # Python, Java, JavaScript

# 문자열 포맷팅 (Formatting) : 문자열에 변수의 값을 삽입하는 방법
# ============================================================================
# 문자열 포맷팅 방법 비교표
# ============================================================================
# | 방법        | Python 버전 | 가독성 | 성능    | 예제                              |
# |------------|------------|--------|--------|----------------------------------|
# | f-string   | 3.6+       | 매우 좋음 | 빠름  | f"My name is {name}"             |
# | format()   | 2.7+       | 좋음    | 보통   | "My name is {}".format(name)     |
# | % 포맷팅   | 모든 버전  | 보통    | 빠름   | "My name is %s" % name           |
# ============================================================================

# f-string (Python 3.6+) : 가장 권장되는 방법
name = "Python"
age = 30
formatted_text = f"My name is {name} and I am {age} years old"
#print(formatted_text) # My name is Python and I am 30 years old

# format() 메서드 사용
formatted_text = "My name is {} and I am {} years old".format(name, age)
#print(formatted_text) # My name is Python and I am 30 years old

# % 포맷팅 (구식 방법이지만 여전히 사용됨)
formatted_text = "My name is %s and I am %d years old" % (name, age)
#print(formatted_text) # My name is Python and I am 30 years old

# 문자열 시작/끝 확인하기
# startswith() 메서드를 사용하여 문자열이 특정 문자열로 시작하는지 확인할 수 있다.
text = "Python is easy"
starts_with = text.startswith("Python") # text가 "Python"으로 시작하는지 확인한다.
#print(starts_with) # True

# endswith() 메서드를 사용하여 문자열이 특정 문자열로 끝나는지 확인할 수 있다.
text = "Python is easy"
ends_with = text.endswith("easy") # text가 "easy"로 끝나는지 확인한다.
#print(ends_with) # True

# 문자열 정렬하기
# ljust() 메서드를 사용하여 문자열을 왼쪽 정렬하고 오른쪽을 공백으로 채울 수 있다.
text = "Python"
left_aligned = text.ljust(10) # 10자리로 왼쪽 정렬한다.
#print(left_aligned) # Python    (오른쪽에 공백 4개)

# rjust() 메서드를 사용하여 문자열을 오른쪽 정렬하고 왼쪽을 공백으로 채울 수 있다.
text = "Python"
right_aligned = text.rjust(10) # 10자리로 오른쪽 정렬한다.
#print(right_aligned) #     Python (왼쪽에 공백 4개)

# center() 메서드를 사용하여 문자열을 가운데 정렬할 수 있다.
text = "Python"
centered = text.center(10) # 10자리로 가운데 정렬한다.
#print(centered) #   Python  (양쪽에 공백)

# 문자열 확인하기 (True/False 반환)
# ============================================================================
# 문자열 검증 메서드 정리표
# ============================================================================
# | 메서드      | 설명                          | 예제              | 결과  |
# |------------|------------------------------|------------------|------|
# | isdigit()  | 숫자로만 구성되어 있는지        | "123".isdigit()  | True |
# |            |                              | "12a".isdigit()  | False|
# | isalpha()  | 알파벳으로만 구성되어 있는지     | "abc".isalpha()  | True |
# |            |                              | "ab1".isalpha()  | False|
# | isalnum()  | 알파벳과 숫자로만 구성되어 있는지 | "ab1".isalnum()  | True |
# |            |                              | "ab 1".isalnum() | False|
# | isspace()  | 공백으로만 구성되어 있는지       | "   ".isspace() | True |
# |            |                              | "ab ".isspace()  | False|
# | islower()  | 모두 소문자인지                 | "abc".islower()  | True |
# | isupper()  | 모두 대문자인지                 | "ABC".isupper()  | True |
# | istitle()  | 각 단어가 대문자로 시작하는지    | "Ab C".istitle() | True |
# ============================================================================

# isdigit() 메서드를 사용하여 문자열이 숫자로만 구성되어 있는지 확인할 수 있다.
text1 = "12345"
is_digit = text1.isdigit() # text1이 숫자로만 구성되어 있는지 확인한다.
#print(is_digit) # True

text2 = "123abc"
is_digit = text2.isdigit()
#print(is_digit) # False

# isalpha() 메서드를 사용하여 문자열이 알파벳으로만 구성되어 있는지 확인할 수 있다.
text1 = "Python"
is_alpha = text1.isalpha() # text1이 알파벳으로만 구성되어 있는지 확인한다.
#print(is_alpha) # True

text2 = "Python123"
is_alpha = text2.isalpha()
#print(is_alpha) # False

# isalnum() 메서드를 사용하여 문자열이 알파벳과 숫자로만 구성되어 있는지 확인할 수 있다.
text1 = "Python123"
is_alnum = text1.isalnum() # text1이 알파벳과 숫자로만 구성되어 있는지 확인한다.
#print(is_alnum) # True

text2 = "Python 123"
is_alnum = text2.isalnum() # 공백이 포함되어 있으면 False
#print(is_alnum) # False

# isspace() 메서드를 사용하여 문자열이 공백으로만 구성되어 있는지 확인할 수 있다.
text1 = "   "
is_space = text1.isspace() # text1이 공백으로만 구성되어 있는지 확인한다.
#print(is_space) # True

text2 = "Python"
is_space = text2.isspace()
#print(is_space) # False

# islower() 메서드를 사용하여 문자열이 모두 소문자인지 확인할 수 있다.
text1 = "python"
is_lower = text1.islower() # text1이 모두 소문자인지 확인한다.
#print(is_lower) # True

# isupper() 메서드를 사용하여 문자열이 모두 대문자인지 확인할 수 있다.
text2 = "PYTHON"
is_upper = text2.isupper() # text2가 모두 대문자인지 확인한다.
#print(is_upper) # True

# istitle() 메서드를 사용하여 각 단어가 대문자로 시작하는지 확인할 수 있다.
text3 = "Python Is Easy"
is_title = text3.istitle() # text3의 각 단어가 대문자로 시작하는지 확인한다.
#print(is_title) # True
