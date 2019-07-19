import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        else:
            slow = fast = head
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next

            lhead, rhead = head, self.reverse(slow.next)
            slow.next = None

            lcur, rcur = lhead, rhead
            while lcur and rcur:
                tmp, rcur = rcur, rcur.next
                tmp.next = lcur.next
                lcur.next, lcur = tmp, lcur.next

            res = []
            while lhead:
                res.append(lhead.val)
                lhead = lhead.next

            return res
        
    def reverse(self, head):
        if not head: return None
        else:
            cur = head
            prev = None
            while cur:
                cur.next, cur, prev = prev, cur.next, cur
            return prev

class Test(unittest.TestCase):
    def test_reorderList(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
       
        res = [1, 4, 2, 3]


        sol = Solution()
        self.assertEqual(sol.reorderList(head),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()