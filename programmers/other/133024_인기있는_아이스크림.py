# 인기있는 아이스크림
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133024
# 작성자: ㅇㅇ
# 작성일: 2026. 01. 19. 13:27:38

SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;