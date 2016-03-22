# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node = head
        alpha = None
        beta = None
        firstAlpha = None
        firstBeta = None

        while node is not None:
            if node.val < x:
                if alpha is not None:
                    alpha.next = node 
                else:
                    firstAlpha = node
                alpha = node
            else:
                if beta is not None:
                    beta.next = node
                else:
                    firstBeta = node
                beta = node 
            node = node.next
        
        if beta is not None:
            beta.next = None
        if alpha is not None:
            alpha.next= firstBeta
            return firstAlpha
        else:
            return firstBeta

if __name__ == '__main__':
    
    node = ListNode(1)
    head = node
    node.next = ListNode(4)
    node = node.next
    node.next = ListNode(3)
    node = node.next
    node.next = ListNode(2)
    node = node.next
    node.next = ListNode(5)
    node = node.next
    node.next = ListNode(2)

    
    s = Solution() 
    node = s.partition(head, 3)
    while node is not None:
        print node.val
        node = node.next
