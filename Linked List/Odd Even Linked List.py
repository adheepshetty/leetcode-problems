import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
    '''
    def oddEvenList(self, head):
        headOdd = dummyOdd = ListNode(-1)
        headEven = dummyEven = ListNode(-1)
        cur = head
        count = 1
        while cur:
            if count % 2 == 0:
                dummyEven.next = cur
                dummyEven = dummyEven.next
            else:
                dummyOdd.next = cur
                dummyOdd = dummyOdd.next
            cur = cur.next
            count += 1
        dummyEven.next = None
        dummyOdd.next = headEven.next

        res = []
        cur = headOdd.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

class Test(unittest.TestCase):
    def test_oddEvenList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
       
        res = [1,3,5,2,4]


        sol = Solution()
        self.assertEqual(sol.oddEvenList(head),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()