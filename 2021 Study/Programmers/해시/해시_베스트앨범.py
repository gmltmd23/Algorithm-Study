"""

프로그래머스 해시_베스트앨범 : LEVEL3

레벨3의 문제였지만, 생각보다는 어렵지 않은 문제였다.
sorted 함수의 사용법을 충분히 익혀뒀으면 어렵지 않게 풀 문제
다 푸는데 25분정도 걸린거같다.

solution1은 내가 처음으로 짜서 통과한 코드고
solution2는 코드를 더 짧고 예쁘게 만든 코드이다. [중간에 candidate(장르별 재생순위)를 구하는 과정을 람다로 대체함]

"""

def solution1(genres, plays):
    result = []
    songs, id_numbers = {}, {}

    for genre, play, id in zip(genres, plays, range(len(genres))):
        if genre not in songs:
            songs[genre] = play
            id_numbers[genre] = [(play, id)]
        else:
            songs[genre] += play
            id_numbers[genre].append((play, id))

    candidate = []
    while songs:
        candidate.append(songs.popitem())
    candidate = sorted(candidate, key = lambda x: x[1])

    while candidate:
        now = candidate.pop()[0]
        rank = sorted(id_numbers[now], key = lambda x: (x[0], -x[1]))
        result.append(rank.pop()[1])
        if rank:
            result.append(rank.pop()[1])

    return result


def solution2(genres, plays):
    result = []
    songs, id_numbers = {}, {}

    for genre, play, id in zip(genres, plays, range(len(genres))):
        if genre not in songs:
            songs[genre] = play
            id_numbers[genre] = [(play, id)]
        else:
            songs[genre] += play
            id_numbers[genre].append((play, id))
    songs = sorted(songs.items(), key=lambda x: x[1])

    while songs:
        now = songs.pop()[0]
        rank = sorted(id_numbers[now], key=lambda x: (x[0], -x[1]))
        result.append(rank.pop()[1])
        if rank:
            result.append(rank.pop()[1])

    return result

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution1(g, p))
print(solution2(g, p))