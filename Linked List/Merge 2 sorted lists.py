# author: Adheep
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import unittest
class Solution:
    '''
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

    Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    '''
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        dummy = dummy.next
        result = []
        while dummy:
            result.append(dummy.val)
            dummy  = dummy.next
        return result
        

class Test(unittest.TestCase):
    def test_mergeTwoLists(self):
        head1 = ListNode(1)
        head2 = ListNode(1)
        # headex = ListNode(1)
        cur1 = head1
        cur2 = head2
        # curex = headex
        l1 = [2, 4]
        l2 = [3, 4]
        result = [1, 1, 2, 3, 4, 4]
        for i in range(len(l1)):
            cur1.next = ListNode(l1[i]) 
            cur2.next = ListNode(l2[i])
            cur1 = cur1.next
            cur2 = cur2.next
        # for k in range(len(l3)):
        #     curex.next = ListNode(l3[k])
        #     curex = curex.next
        cur1.next = None
        cur2.next = None
        # curex.next = None
        sol = Solution()
        self.assertEqual(sol.mergeTwoLists(head1, head2),result)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()