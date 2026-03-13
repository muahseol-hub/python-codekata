# 괄호
# 백준 레벨8 (백준)
# 문제 링크: https://www.acmicpc.net/problem/9012
# 알고리즘: 스택
# 작성자: ㅇㅇ
# 작성일: 2026. 03. 13. 21:56:31

T = int(input())
for _ in range(T):
    s = input()
    count = 0
    valid = True
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            valid = False
            break
    print("YES" if valid and count == 0 else "NO")