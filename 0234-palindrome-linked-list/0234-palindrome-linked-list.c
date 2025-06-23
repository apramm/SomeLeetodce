/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    // Approach using Lists
    int* vals = (int*)malloc(sizeof(int) * 100000); 
    int size = 0;

    // Step 1: Copy values from the list into the array
    struct ListNode* temp = head;
    while (temp != NULL) {
        vals[size++] = temp->val;
        temp = temp->next;
    }

    // Step 2: Two-pointer check
    int left = 0, right = size - 1;
    while (left < right) {
        // condition to return false
        if (vals[left] != vals[right]) {
            free(vals);
            return false;
        }
        left++;
        right--;
    }

    free(vals);
    return true;


    // to check palindrome we can iterate over the linkedlist and mark the node where the current node value is same the next node value
    // after we get the middle node we can iterate from both side an compare the values
    // worst case O(n) time and O(1) space as no storing
    // struct ListNode* dummy = (ListNode*)malloc(sizeof(struct ListNode));
    // dummy->next = head;
    // dummy->va; = 0;

    // struct ListNode* curr = head;
    // struct ListNode* nextNode = curr->next;
    // while(curr->val != nextNode->val){
    //     curr = curr->next;
    //     nextNode = nextNode->next;
    //     if(curr == NULL){
    //         return FALSE;
    //     }
    // } // iterate to find the node where the palindrome could possibly begin

    // while(nextNode != NULL){
    //     if()
    // }

}