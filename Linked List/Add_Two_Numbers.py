import unittest
# Definition for singly-linked list.
class ListNode(object):
    '''
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    '''

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        result = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry +=l2.val
                l2 = l2.next
            dummy.next = ListNode(carry%10)
            carry = carry//10
            dummy = dummy.next
            
        return result.next

class Test(unittest.TestCase):
    def test_addtwonumbers(self):
        head1 = ListNode(2)
        head2 = ListNode(5)
        headex = ListNode(7)
        cur1 = head1
        cur2 = head2
        curex = headex
        l1 = [4, 3]
        l2 = [6, 4]
        l3 = [0, 8]
        for i,j,k in zip(range(len(l1)),range(len(l2)), range(len(l3))):
            next1 = cur1.next(l1[i])
            next2 = cur2.next(l2[j])
            nextex = curex.next(l3[k])
            cur1 = next1
            cur2 = next2
            curex = nextex
        cur1.next = None
        cur2.next = None
        curex.next = None
        sol = Solution()
        self.assertEqual(sol.addTwoNumbers(head1, head2),headex)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()