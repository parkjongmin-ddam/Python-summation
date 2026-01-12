# 파이썬에서 리스트의 다양한 속성과 Method를 알아보는 방법에는 여러가지가 있습니다.
# 1. help() 함수를 사용하여 리스트의 속성과 Method를 알아볼 수 있습니다.
# 2. 공식 문서를 참조하여 리스트의 속성과 Method를 알아볼 수 있습니다.
# 3. dir() 함수를 사용하여 리스트의 속성과 Method를 알아볼 수 있습니다.

# dir() 함수 사용하기
# dir() 함수는 List 객체가 가지고 있는 모든 속성과 Method의 이름을 List 형태로 반환한다.

# List 생성
dir_list = []

#List 속성과 Method 확인
attributes_and_methods = dir(dir_list)
print(attributes_and_methods) # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# help() 함수 사용하기
# help() 함수는 List 객체가 가지고 있는 모든 속성과 Method의 상세한 정보를 출력한다.
# 주의: help() 함수는 대화형 모드(인터프리터)에서 사용하는 것이 권장된다.
# 스크립트에서 실행할 경우 pager 관련 에러가 발생할 수 있다.

# List 생성
help_list = []

# List 속성과 Method 확인
# help(help_list) # 주석 처리: 대화형 모드에서만 사용 권장
# 
# 대화형 모드에서 실행하면 다음과 같은 정보가 출력된다:
# Help on list object:
#
# class list(object)
# |  list(iterable=(), /)
# |
# |  Built-in class for immutable sequences of numbers.
# |
# |  Methods defined here:
# |
# |  __add__(self, value, /)
# |      Return self+value.
# ...
#
# 특정 메서드의 도움말을 보려면:
# help(list.append) # append 메서드의 상세 정보를 출력한다.
# help(list.remove) # remove 메서드의 상세 정보를 출력한다.

# 주의사항:
# help() 함수는 Python 인터프리터(>>>) 안에서 실행해야 합니다.
# PowerShell 프롬프트(PS>)에서 직접 실행하면 오류가 발생합니다.
# 
# 올바른 사용법:
# 1. PowerShell에서: python (또는 py) 입력
# 2. Python 인터프리터(>>>)에서: help(list.remove) 입력
# 3. 종료: exit() 또는 Ctrl+Z 입력   

# 예제 코드 (실제 실행 가능한 예제)
example_list = []

# dir() 함수를 통해 List 속성 및 Method 확인
attributes_and_methods = dir(example_list)
print("dir() 함수 결과:")
print(attributes_and_methods)
print()  # 빈 줄 출력

# help() 함수를 통해 List 속성 및 Method 확인
# 주의: help() 함수는 대화형 모드에서 사용하는 것이 권장됩니다.
# 스크립트에서 실행하면 pager 관련 에러가 발생할 수 있습니다.
# 아래 코드는 주석 처리되어 있습니다. 대화형 모드에서 직접 실행해보세요.

# print("\nHelp documentation using help() function: ")
# help(example_list)   # 대화형 모드에서만 실행 권장

# 특정 Method 상세 정보 확인
# print("\n특정 메서드(append)의 상세 정보:")
# help(example_list.append)    # 대화형 모드에서만 실행 권장

# 대화형 모드에서 실행하는 방법:
# 1. 터미널에서: python 입력
# 2. Python 인터프리터(>>>)에서: help(list.append) 입력
# 3. 종료: exit() 입력

