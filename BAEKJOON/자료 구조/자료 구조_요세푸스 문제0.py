"""

백준 문제 11866번 자료 구조_요세푸스 문제 0

단순하게 리스트의 구조와 pop을 이용하는 문제이다.
예시 출력에 예쁘게 부등호로 나와있길래 그냥 그런줄 알았는데
부등호 안넣으면 틀리게 나옴 ㅋㅋㅋㅋㅋㅋㅋ

그래서 부등호 넣으니깐 정답이었다.

"""

n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]

idx = k - 1
print("<", end = '')
while nums:
    print(nums.pop(idx), end = '')
    if nums:
        print(", ", end = '')
        idx = (idx + (k - 1)) % len(nums)
print(">")