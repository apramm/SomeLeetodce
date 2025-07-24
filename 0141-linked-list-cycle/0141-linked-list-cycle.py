# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #my soln O(n) time and space
        # idea to have a set which keeps on updating as we iterate thru linkedlist
        # if the element alr in the set then we've cycle else we dont
        # spinned around on value wayy to long bro just store the whole thing :/

        if head == None : return False

        setNodes = set()

        while head:
            if head in setNodes:
                return True
            else:
                setNodes.add(head)

            head = head.next
            
        return False

        # follow up, can it be done in O(1) SPACE?
        # i.e., would need to use some pointer way to know all visited nodes 

        # i can update head = head.next and change the visited node's head.next as it doesn't state that i need to keep linkedlist the same way :/

        curr = head
        while head:
                curr = head.next
                head.next.val = -1
                head = head.next
                if head.val == -1:
                    return True

        return False

        