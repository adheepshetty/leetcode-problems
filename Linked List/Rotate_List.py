import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Given a linked list, rotate the list to the right by k places, where k is non-negative.
    '''
    def rotateRight(self, head, k):
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1

        if not n or not k % n:
            return head

        tail = head
        for _ in range(n - k % n - 1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head

        result = []
        while next != None:
            result.append(next.val)
            next = next.next

        return result

class Test(unittest.TestCase):
    def test_rotateRight(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        k = 1
        listex = [3,1,2]

        sol = Solution()
        self.assertEqual(sol.rotateRight(head,k),listex)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()