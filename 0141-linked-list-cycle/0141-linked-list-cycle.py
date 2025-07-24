# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #       SET O(n) time and space
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
    
        #       MY TRY WITH SOME KIND OF LINKED LIST MANIPULATION (WORKS)
        # i.e., would need to use some pointer way to know all visited nodes 
        # i can update head.val = None? if it's visited so, i know if it's visited one or not as 


        while head:
            if head.val == None:
                return True
            else:
                head.val = None
            head = head.next
            

        return False

        # i am goat solved in O(1) space don't know if it's valid but works!

        #       FAST AND SLOW
        # there's fast and slow approach which idk how intuitive but works fine
        #IF A POINTER MOVES TWO STEPS AND OTHER ONE STEP THEY'RE BOUND TO MEET

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False