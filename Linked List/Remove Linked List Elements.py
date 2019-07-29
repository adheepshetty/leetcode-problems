import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Remove all elements from a linked list of integers that have value val.
    '''
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        else:
            dummy_cur = dummy = ListNode(None)
            cur = head
            while cur:
                if cur.val == val:
                    cur= cur.next
                    dummy_cur.next= None
                else:
                    dummy_cur.next= cur
                    cur= cur.next
                    dummy_cur= dummy_cur.next
            res = []
            dummy = dummy.next
            while dummy:
                res.append(dummy.val)
                dummy = dummy.next
            return res
            
class Test(unittest.TestCase):
    def test_removeElements(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)  

        val = 2
        res = [1,4,5]

        sol = Solution()
        self.assertEqual(sol.removeElements(head, val),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()