"""

LeetCode 문제 1. Two Sum

단순하게 Brute Force로 풀어도 되는 문제지만,
그러면 시간복잡도가 O(n^2)이 나오니깐 비효율적이다.
문제의 조건을 활용하여 아랫방식으로 풀으니깐 속도도 더 빨라지고 좋아졌다.

"""

import sys
input = sys.stdin.readline

class Solution:
    def twoSum(self, nums, target):
        index = 0
        result = list()
        for number in nums:
            target_data = target - number
            index += 1
            if target_data in nums[index:]:
                return [index - 1, nums[index:].index(target_data) + index]