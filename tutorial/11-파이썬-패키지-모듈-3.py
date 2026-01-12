# 표준 라이브러리
# Python에 내장된 유용한 모듈들

# ============================================================================
# 자주 사용하는 표준 라이브러리
# ============================================================================

# 1. math: 수학 함수
import math
#print(math.sqrt(16)) # 4.0
#print(math.pi) # 3.141592653589793

# 2. datetime: 날짜와 시간
from datetime import datetime, date, timedelta
now = datetime.now()
#print(now) # 현재 날짜와 시간

# 3. random: 랜덤 값 생성
import random
number = random.randint(1, 100)
#print(number) # 1부터 100 사이의 랜덤 정수

# 4. os: 운영체제 인터페이스
import os
current_dir = os.getcwd()
#print(current_dir) # 현재 작업 디렉토리

# 5. sys: 시스템 관련
import sys
#print(sys.version) # Python 버전

# 6. json: JSON 처리
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
#print(json_string) # '{"name": "Alice", "age": 25}'

# 7. csv: CSV 파일 처리
import csv
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# 8. collections: 특수 컬렉션 타입
from collections import Counter, defaultdict, deque
counter = Counter([1, 2, 2, 3, 3, 3])
#print(counter) # Counter({3: 3, 2: 2, 1: 1})

# 9. itertools: 반복자 함수
from itertools import combinations, permutations
comb = list(combinations([1, 2, 3], 2))
#print(comb) # [(1, 2), (1, 3), (2, 3)]

# 10. functools: 함수 도구
from functools import reduce, lru_cache
result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
#print(result) # 15

# ============================================================================
# 주의사항
# ============================================================================
# 1. 표준 라이브러리는 Python에 내장되어 있어 별도 설치가 필요 없다.
# 2. 필요한 모듈만 import하여 사용하는 것이 좋다.
# 3. 공식 문서를 참조하여 각 모듈의 기능을 확인할 수 있다.
# ============================================================================
