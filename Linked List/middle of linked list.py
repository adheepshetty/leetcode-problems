import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        i,curr = 0, head
        while curr:
            i,curr = i+1, curr.next
        
        mid,i,curr = i // 2, 0, head
        
        while curr:
            if i == mid: return curr.val
            i, curr = i+1, curr.next
        
        return curr.val
    
class Test(unittest.TestCase):
    def test_middleNode(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        res = 3

        sol = Solution()
        self.assertEqual(sol.middleNode(head),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()