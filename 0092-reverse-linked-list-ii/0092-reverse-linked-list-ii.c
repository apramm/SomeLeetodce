/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    // BASE EDGE
    // if head is empty or left is same as right
    if (!head || left == right) {
        return head; // No reversal needed or list is empty
    }


    // Now as we want to reverse two specific locations i.e., left and right. So, we'd need to set up a dummy node to keep track of the previous node of head which will eventually track the node before left
    // IMPORTANT TO KNOW HOW TO USE MALLOC
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;

    struct ListNode* prev = dummy;
    // struct ListNode* curr = head;
    for (int i = 0; i < left - 1; i++){
        prev = prev->next; //move prev to just one before left
        // curr = curr->next; // move curr to the left node i.e., the one that's supposed to be reversed
    }

    struct ListNode* curr = prev->next; //point to the left node i.e., the one that's to be reversed
    
    // JUST MARKING THE SUBLIST HEADER
    struct ListNode* sublistHeader = curr;

    // sublist reversal
    struct ListNode* preNode = NULL;
    for (int i = 0; i < right-left+1; i++){ // need to reverse right-left times
        struct ListNode* nextNode = curr->next;
        curr->next = preNode;
        preNode = curr;
        curr = nextNode;
        // move curr.next to point to NULL/a previous node, move previous and curr ahead to continue reversing the list
    }
    //JOIN THE PIECES TO COMPLETE THE LINKED LIST
    prev->next = preNode;
    sublistHeader->next = curr;
    return dummy->next;
}