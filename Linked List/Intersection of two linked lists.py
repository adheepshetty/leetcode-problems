import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Write a program to find the node at which the intersection of two singly linked lists begins.
    '''
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB: 
            # return None

            print('here')
            return 0
        curA = headA
        curB = headB
        count = 0
        flagA = flagB = False
        while curA or curB:
            if curA == curB: 
                print('here') 
                return curA.val
            curA = curA.next
            curB = curB.next
            if not curB:
                while curA:
                    count +=1 
                    flagA = True
                    curA = curA.next
            if not curA:
                while curB:
                    count +=1
                    flagB = True
                    curB = curB.next
        # print(curA.val, curB.val)
        curA , curB = headA, headB
        if flagA:
            while count != 0:
                curA = curA.next
                count -=1
        if flagB:
            while count != 0:
                curB = curB.next
                count -=1
        print(curA.val, curB.val)
        while curA is not curB:
            curA = curA.next
            curB = curB.next
        return curA.val


class Test(unittest.TestCase):
    def test_getIntersectionNode(self):
        head = ListNode(4)
        head.next = ListNode(1)
        head.next.next = ListNode(8)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
       

        head1 = ListNode(5)
        head1.next = ListNode(0)
        head1.next.next = ListNode(1)
        head1.next.next.next = ListNode(8)
        head1.next.next.next.next = ListNode(4)
        head1.next.next.next.next.next = ListNode(5)

        res = 8


        sol = Solution()
        self.assertEqual(sol.getIntersectionNode(head, head1),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()