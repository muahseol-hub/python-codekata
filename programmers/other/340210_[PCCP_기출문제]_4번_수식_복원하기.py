# [PCCP 기출문제] 4번 / 수식 복원하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340210
# 작성자: 설무아
# 작성일: 2026. 01. 15. 23:59:22

def solution(expressions):
    def to_decimal(s, base):
        """base진법 문자열을 10진수로 변환"""
        result = 0
        for c in s:
            result = result * base + int(c)
        return result
    
    def to_base(n, base):
        """10진수를 base진법 문자열로 변환"""
        if n == 0:
            return "0"
        result = ""
        while n > 0:
            result = str(n % base) + result
            n //= base
        return result
    
    def get_max_digit(s):
        """문자열에서 최대 숫자 반환"""
        max_d = 0
        for c in s:
            if c.isdigit():
                max_d = max(max_d, int(c))
        return max_d
    
    def parse(expr):
        """수식 파싱: A, op, B, C 반환"""
        parts = expr.split()
        A, op, B, _, C = parts
        return A, op, B, C
    
    # 1. 모든 수식에서 최소 진법 찾기 (최대 숫자 + 1)
    min_base = 2
    for expr in expressions:
        min_base = max(min_base, get_max_digit(expr) + 1)
    
    # 2. 가능한 진법 후보 (min_base ~ 9)
    possible_bases = set(range(min_base, 10))
    
    # 3. 결과가 있는 수식으로 유효한 진법 필터링
    for expr in expressions:
        A, op, B, C = parse(expr)
        if C == "X":
            continue
        
        valid_bases = set()
        for base in possible_bases:
            a = to_decimal(A, base)
            b = to_decimal(B, base)
            c = to_decimal(C, base)
            
            if op == "+":
                if a + b == c:
                    valid_bases.add(base)
            else:  # op == "-"
                if a - b == c:
                    valid_bases.add(base)
        
        possible_bases &= valid_bases
    
    # 4. X인 수식들의 결과 계산
    result = []
    for expr in expressions:
        A, op, B, C = parse(expr)
        if C != "X": #
            continue
        
        # 가능한 모든 진법으로 계산
        results_set = set()
        for base in possible_bases:
            a = to_decimal(A, base)
            b = to_decimal(B, base)
            
            if op == "+":
                res = a + b
            else:
                res = a - b
            
            results_set.add(to_base(res, base))
        
        # 결과가 유일하면 그 값, 아니면 ?
        if len(results_set) == 1:
            answer = results_set.pop()
        else:
            answer = "?"
        
        result.append(f"{A} {op} {B} = {answer}")
    
    return result