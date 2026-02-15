# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if linked list empty we got no duplicates to remove
        if (head == None):
            return head
        
        # else to find duplicate we'd have to iterate once through list
        # we can have a next and dup head to check against
        check_head = head
        next = head.next
        #iterate over sorted linked list
        while next:
            #we found duplicate, skip the next node and move next to the next node
            if check_head.val == next.val: 
                check_head.next = next.next #skip the head->next
                next = next.next #move next to the next node
            
            else: #we found a new value i.e., continue iterating and move both heads forward
                check_head = check_head.next 
                next = next.next


        return head 