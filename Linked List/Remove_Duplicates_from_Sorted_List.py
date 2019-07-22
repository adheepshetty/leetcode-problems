import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Given a sorted linked list, delete all duplicates such that each element appear only once.
    '''

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        prev = head
        cur = head.next
        dummy = dumy_cur = ListNode(0)
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
            
        return res


class Test(unittest.TestCase):
    def test_deleteDuplicates(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
       
        res = [1, 2, 3]


        sol = Solution()
        self.assertEqual(sol.deleteDuplicates(head),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()