"""

LeetCode 문제 2. Add Two Numbers

Linked List 문제인데, 처음에 만들었던 코드는 Runtime이 80ms가 나와서 별로였다.
그래서 개선시킬 방법을 찾기위해 코드들을 참고해서 만들어보니깐
Runtime을 68ms로 줄일수가 있었다.

역시 알고리즘의 세계는 놀랍다.

"""

import sys
input = sys.stdin.readline

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next