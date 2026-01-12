# 재귀 함수 (Recursive Functions)
# 재귀 함수는 자기 자신을 호출하는 함수이다.

# ============================================================================
# 기본 재귀 함수: 팩토리얼
# ============================================================================

def factorial(n):
    """팩토리얼을 계산하는 재귀 함수"""
    # 기본 케이스 (Base Case)
    if n == 0 or n == 1:
        return 1
    # 재귀 케이스 (Recursive Case)
    return n * factorial(n - 1)

result = factorial(5)
#print(result) # 120 (5! = 5 * 4 * 3 * 2 * 1)

# ============================================================================
# 피보나치 수열
# ============================================================================

def fibonacci(n):
    """피보나치 수열의 n번째 항을 계산하는 재귀 함수"""
    # 기본 케이스
    if n <= 1:
        return n
    # 재귀 케이스
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
#print(result) # 8 (0, 1, 1, 2, 3, 5, 8, ...)

# ============================================================================
# 재귀 함수의 구성 요소
# ============================================================================
# 1. 기본 케이스 (Base Case): 재귀를 종료하는 조건
# 2. 재귀 케이스 (Recursive Case): 함수가 자기 자신을 호출하는 부분

# ============================================================================
# 재귀 vs 반복문
# ============================================================================

# 재귀 버전
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# 반복문 버전
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# ============================================================================
# 재귀 깊이 제한
# ============================================================================
# Python은 기본적으로 재귀 깊이를 1000으로 제한한다.

import sys
#print(sys.getrecursionlimit()) # 기본값: 1000

# 재귀 깊이 변경 (주의: 메모리 오버플로우 가능)
# sys.setrecursionlimit(2000)

# ============================================================================
# 꼬리 재귀 (Tail Recursion)
# ============================================================================
# Python은 꼬리 재귀 최적화를 지원하지 않지만, 개념을 이해하는 것이 중요하다.

def factorial_tail(n, accumulator=1):
    """꼬리 재귀 버전 (Python에서는 최적화되지 않음)"""
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# ============================================================================
# 메모이제이션 (Memoization)
# ============================================================================
# 재귀 함수의 성능을 향상시키기 위해 결과를 캐싱한다.

# 메모이제이션 없이 (느림)
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# 메모이제이션 사용 (빠름)
memo = {}

def fibonacci_fast(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_fast(n - 1) + fibonacci_fast(n - 2)
    return memo[n]

# functools.lru_cache 사용
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# ============================================================================
# 재귀 함수 예제
# ============================================================================

# 예제 1: 리스트 합계
def sum_list(numbers):
    """리스트의 합을 재귀적으로 계산"""
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

result = sum_list([1, 2, 3, 4, 5])
#print(result) # 15

# 예제 2: 리스트 최대값
def max_list(numbers):
    """리스트의 최대값을 재귀적으로 찾기"""
    if len(numbers) == 1:
        return numbers[0]
    max_rest = max_list(numbers[1:])
    return numbers[0] if numbers[0] > max_rest else max_rest

result = max_list([3, 7, 2, 9, 1])
#print(result) # 9

# 예제 3: 거듭제곱
def power(base, exponent):
    """거듭제곱을 재귀적으로 계산"""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

result = power(2, 3)
#print(result) # 8

# 예제 4: 문자열 뒤집기
def reverse_string(s):
    """문자열을 재귀적으로 뒤집기"""
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

result = reverse_string("hello")
#print(result) # "olleh"

# ============================================================================
# 주의사항
# ============================================================================
# 1. 재귀 함수는 기본 케이스를 반드시 포함해야 한다.
# 2. 재귀 깊이가 너무 깊으면 스택 오버플로우가 발생할 수 있다.
# 3. 메모이제이션을 사용하여 성능을 향상시킬 수 있다.
# 4. 간단한 반복문으로 해결할 수 있는 경우 반복문을 사용하는 것이 더 효율적일 수 있다.
# 5. 재귀는 문제를 더 작은 하위 문제로 나누는 데 유용하다 (분할 정복).
# ============================================================================
