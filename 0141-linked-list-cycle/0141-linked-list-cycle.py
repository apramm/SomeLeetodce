# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea to have a set which keeps on updating as we iterate thru linkedlist
        # if the element alr in the set then we've cycle else we dont
        if head == None : return False
        print(head.next)

        setNodes = set()
        
        while head:
            if head in setNodes:
                return True
            else:
                setNodes.add(head)

            head = head.next
            
        return False
        