import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Given a linked list, swap every two adjacent nodes and return its head.

    You may not modify the values in the list's nodes, only nodes itself may be changed.
    '''
    def swapPairs(self, head):
        cur = head
        list = []
        while cur != None:
            prev = cur
            nex = cur.next
            if cur.next == None:
                list.append(cur.val)
                break
            cur = cur.next.next
            prev.val , nex.val = self.swap(prev.val, nex.val)
            list.append(prev.val)
            list.append(nex.val)

        return list
    
    def swap(self, a, b):
            return b , a

        
class Test(unittest.TestCase):
    def test_swapPairs(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        listex = [2,1,3]

        sol = Solution()
        self.assertEqual(sol.swapPairs(head),listex)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()