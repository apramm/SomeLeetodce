/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// BETTER TO DEFINE TYPE USING typedef
// typedef struct ListNode {
//     int val;
//     struct ListNode *next;
// } ListNode;

struct ListNode* reverseList(struct ListNode* head) {
    //base case:
    if(!head){
        return head;
    }
    // set a prev node and then keep updating until traverse the whole thing
    struct ListNode* pre = NULL;
    struct ListNode* curr = head;
    while (curr!= NULL){
        struct ListNode* nextNode = curr->next;
        curr->next = pre;
        pre = curr;
        curr = nextNode;
    }

    return pre;
}