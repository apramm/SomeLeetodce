#include <stdio.h>
#include <stdlib.h>

// Define the ListNode structure
typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;

ListNode* reverseList(ListNode* head){
  //base if no head we straight up return itself
  if(!head){
    return head;
  }
  // for other cases we'd need to create a prev node to point null so, we can begin reversing the linked list
  ListNode* pre = NULL;
  ListNode* curr = head;
  while (curr!=NULL){
    ListNode* nextNode = curr->next;
    curr->next = pre;
    pre = curr;
    curr = nextNode;
  } // this will continue until curr reaches end i.e., NULL

  return pre;
}

ListNode* reverseSubList(ListNode* head, int left, int right){
  if(!head || left == right){
    return head;
  }

  ListNode* dummy = (ListNode*)malloc(sizeof(ListNode));
  dummy->val = 0;
  dummy->next = head;

  ListNode* prev = dummy; 
  for(int i = 0; i < left-1; i++){
    prev = prev->next;
  } // point prev to just one before the node we need to reverse

  ListNode* curr = prev->next;
  ListNode* sublistHeader = curr; // Keeps track of what the sublist begins

  // REVERSE SUBLIST
  ListNode* pre = NULL;
  for (int i = 0; i < right - left + 1; i++){
    ListNode* next = curr->next;
    curr->next = pre;
    pre = curr;
    curr = next;
  }
  // after we've reversed the sublist we do the joining process
  prev->next = pre; // point the just one previous sublist to pre i.e., new heading
  sublistHeader->next = curr; // update where the old sublistheader should point to

  return dummy->next;
}

// :HELPERS TO PRINT THE VALUES:

// Helper function to print the linked list
void printList(ListNode* head) {
    ListNode* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->val);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Helper function to create a new ListNode
ListNode* createNode(int val) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Helper function to create a linked list from an array
ListNode* createList(int* arr, int size) {
    ListNode* head = createNode(arr[0]);
    ListNode* current = head;
    for (int i = 1; i < size; i++) {
        current->next = createNode(arr[i]);
        current = current->next;
    }
    return head;
}


int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    ListNode* head = createList(arr, size);
    ListNode* betweenhead = createList(arr, size);

    printf("Original list: ");
    printList(head);

    int left = 2, right = 4;
    head = reverseList(head);

    printf("Reversed list: ");
    printList(head);

    betweenhead = reverseSubList(betweenhead, left, right);

    printf("Reversed between list: ");
    printList(betweenhead);
    return 0;
}
