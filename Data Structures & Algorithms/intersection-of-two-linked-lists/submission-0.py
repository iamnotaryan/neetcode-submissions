# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        cnt = 0 
        cnr = 0
        while pa:
            cnt += 1
            pa = pa.next
        while pb:
            cnr += 1
            pb = pb.next
        if cnt > cnr:
            diff = cnt - cnr
        else:
            diff = cnr - cnt
        pa = headA
        pb = headB
        while diff > 0:
            if cnt > cnr:
                pa = pa.next
            else:
                pb = pb.next
            diff -= 1
        while pa != pb:
            pa = pa.next
            pb = pb.next
        return pa 