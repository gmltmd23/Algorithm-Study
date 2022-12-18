def makeEachPartOfTime(number):
    temp = ""
    if number <= 9:
        temp += "0"
    temp += str(number)
    return temp

def makeTimeToSecond(time):
    hour, minute, second = time.split(':')
    hour, minute, second = int(hour), int(minute), int(second)
    return (3600 * hour) + (60 * minute) + second

def makeSecondToTime(totalSecond):
    hour, totalSecond = divmod(totalSecond, 3600)
    minute, totalSecond = divmod(totalSecond, 60)
    second = totalSecond

    time = makeEachPartOfTime(hour) + ":" + makeEachPartOfTime(minute) + ":" + makeEachPartOfTime(second)
    return time

def solution(play_time, adv_time, logs):
    dp = [0] * (makeTimeToSecond(play_time) + 1)
    for log in logs:
        startTime, endTime = log.split('-')
        startSecond, endSecond = makeTimeToSecond(startTime), makeTimeToSecond(endTime)
        dp[startSecond] += 1
        dp[endSecond] -= 1

    for i in range(len(dp) - 1):
        dp[i + 1] += dp[i]
    for i in range(len(dp) - 1):
        dp[i + 1] += dp[i]

    advSecond = makeTimeToSecond(adv_time)
    mostView, maxSecond = 0, 0
    for i in range(advSecond - 1, len(dp)):
        if i >= advSecond:
            if mostView < (dp[i] - dp[i - advSecond]):
                mostView = dp[i] - dp[i - advSecond]
                maxSecond = i - advSecond + 1
        else:
            if mostView < dp[i]:
                mostView = dp[i]
                maxSecond =  i - advSecond + 1

    return makeSecondToTime(maxSecond)

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))