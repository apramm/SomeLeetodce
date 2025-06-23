/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // BASE CASES
    // * if both empty then return any list
    if(list1 == NULL && list2 == NULL){
        return list1;
    }

    // * if list1 empty then return list2
    if(list1 == NULL && list2 != NULL){
        return list2;
    }
    // * if list2 empty then return list1
    if(list2 == NULL && list1 != NULL){
        return list1;
    }


    // MERGING NON EMPTY
    struct ListNode dummy; //create a new ListNode
    struct ListNode* tail = &dummy;
    dummy.next = NULL;

    while (list1 != NULL && list2 != NULL) {
        // compare the list1 val with list2 val if less then
        if (list1->val <= list2->val) {
            tail->next = list1; // we can assign the next one to point to list1
            list1 = list1->next; // move list1 ahead
        } else {
            tail->next = list2; //same if list2 is smaller value
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Append the remaining list if one is longer
    if (list1 != NULL) tail->next = list1;
    if (list2 != NULL) tail->next = list2;

    return dummy.next;
}   