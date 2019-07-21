import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        temp = temp_cur = ListNode(0)
        prev = None 
        cur = head
        
        while cur: 
            if prev is not None and prev == cur.val:
                temp_cur.next = None
            else:
                if temp_cur.next:
                    temp_cur = temp_cur.next 
                temp_cur.next = cur 
            prev = cur.val
            cur = cur.next
            
        res = []
        cur = temp.next

        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

class Test(unittest.TestCase):
    def test_deleteDuplicates(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
       
        res = [3, 4]


        sol = Solution()
        self.assertEqual(sol.deleteDuplicates(head),res)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()