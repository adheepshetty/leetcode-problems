import unittest
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# author: Adheep
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        heap = []
        heapq.heapify(heap)
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        while not q.empty():
            val , node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

class Test(unittest.TestCase):
    def test_mergeKLists(self):
        head1 = ListNode(1)
        head2 = ListNode(1)
        head3 = ListNode(2)
        # headex = ListNode(1)
        cur1 = head1
        cur2 = head2
        cur3 = head3
        # curex = headex
        l1 = [4, 5]
        l2 = [3, 4]
        l3 = [6]
        result = [1, 1, 2, 3, 4, 4, 5, 6]
        for i in range(len(l1)):
            cur1.next = ListNode(l1[i]) 
            cur2.next = ListNode(l2[i])
            cur1 = cur1.next
            cur2 = cur2.next
        for k in range(len(l3)):
            cur3.next = ListNode(l3[k])
            cur3 = cur3.next
        cur1.next = None
        cur2.next = None
        cur3.next = None
        lists = []
        lists.append(head1)
        lists.append(head2)
        lists.append(head3)
        # curex.next = None
        sol = Solution()
        self.assertEqual(sol.mergeKLists(lists),result)
   

if __name__ == "__main__":
    print(Solution.__doc__)
    unittest.main()
            