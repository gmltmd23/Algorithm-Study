"""

백준 문제 5622번 다이얼

아주 쉬운 구현 문제이다.
if문을 저렇게 많이쓰지않고 구현하는 방법은 있는데,
그것을 한다고해서 속도가 개선되는것도 아니고 코드가독성이 개선되는것도 아니라서
저 방식으로 푸는게 최적인것 같다.

"""

word = input().rstrip()
answer = 0
for w in word:
    if w in {'A', 'B', 'C'}:
        answer += 3
    elif w in {'D', 'E', 'F'}:
        answer += 4
    elif w in {'G', 'H', 'I'}:
        answer += 5
    elif w in {'J', 'K', 'L'}:
        answer += 6
    elif w in {'M', 'N', 'O'}:
        answer += 7
    elif w in {'P', 'Q', 'R', 'S'}:
        answer += 8
    elif w in {'T', 'U', 'V'}:
        answer += 9
    else:
        answer += 10
print(answer)