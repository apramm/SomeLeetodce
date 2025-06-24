/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    // TIP FOR LL:
    // THINK SLOW MAKE IT IN STEPS AND BASIC OPERATIONS USING PNTRS
   if(head == NULL){
     return;
   }
    // SPLIT THE LIST 
    // use a slow and fast pointer
    struct ListNode* slow = head;
    struct ListNode* fast = head;

    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    
    struct ListNode* first = head; // begin for first list
    struct ListNode* second = slow->next; // marker for second list


    slow->next = NULL; // making first and second seperate

    // REVERSE THE SECOND HALF
    struct ListNode* pre = NULL;
    while(second){
        struct ListNode* next = second->next;
        second->next = pre;
        pre = second;
        second = next;
    }
    

    // Merge the two halves
    second = pre;
    while(second){
        struct ListNode* next1 = first->next;
        struct ListNode* next2 = second->next;
        first->next = second;
        second->next = next1;
        first = next1;
        second = next2;
    }

}