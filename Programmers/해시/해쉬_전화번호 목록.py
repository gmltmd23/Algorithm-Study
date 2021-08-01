"""

프로그래머스 해시_전화번호 목록 : LEVEL 2

해시 문제라길래 해시로 풀어볼까 고민했는데,
그것보다는 sort를 사용해서 정렬해놓고 값을 비교하는게 더 빠를거같아서
풀었더니 잘 풀렸다.

그런데 다른사람의 풀이를 보니 sort를 안쓰고도 푸는 방법이있긴하다,
그리고 자바에만 있는줄 알았더니 파이썬에도 startswith 함수가 있어서 편했다.

"""

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

a = ["123","456","789"]
print(solution(a))