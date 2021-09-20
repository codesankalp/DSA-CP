class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        ans = ListNode()
        temp = ans
        r = c = 0
        while(l1):
            s = (l1.val + l2.val)
            r = s % 10
            if (c):
                r += c
                c = 0
            c = s // 10
            ans.val = r
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        return temp


