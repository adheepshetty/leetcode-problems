import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Given a linked list, remove the n-th node from the end of list and return its head.
    '''
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = -1
        prev, cur= head, head
        flag = False
        while cur:
            if count >= n:
                prev = prev.next
                flag = True
            # print('here',prev.val)
            cur = cur.next
            count +=1
            # print(count)
        if flag: prev.next = prev.next.next
        if n > count:
            head = head.next
        if n == count:
            prev.next = prev.next.next
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

class Test(unittest.TestCase):
    def test_removeNthFromEnd(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)  

        val = 3
        res = [1,2,4,5]

        sol = Solution()
        self.assertEqual(sol.removeNthFromEnd(head, val),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()