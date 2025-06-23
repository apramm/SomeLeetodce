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

    struct ListNode dummy;
    struct ListNode* head = &dummy;
    dummy.next = NULL;
    // assign and move ahead while checking the values of list1 and list2
    while(list1 != NULL && list2 != NULL ){
        if(list2->val >= list1->val){
            head->next = list1;
            list1 = list1->next;
        }else{
            head->next = list2;
            list2 = list2->next;
        }
        head = head->next; //move ahead
    }

    // if anyone of them is longer then just add it after the tail
    if(list1!=NULL){head->next = list1;}
    if(list2!=NULL){head->next = list2;}

    return dummy.next;
}   