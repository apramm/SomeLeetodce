/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    // brute is that i traverse through the linked list
    // as soon as i find the value equalling val, i remove that guy
    if(!head){return head;} //base no head
    // let's create a dummy to just always know where the og head 
    // i NEED a dummy to keep track of head as i will have to manipulate the ll

    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* pre = dummy;
    struct ListNode* curr = head;

    while(curr){
        if(curr->val == val){
            struct ListNode* tmp = curr;
            pre->next = curr->next;
            curr = curr->next;
            free(tmp);
        }else{
        pre = curr;
        curr = curr->next;
        }
    } 
    
    return dummy->next;
}