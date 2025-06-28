/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 //  IDEATION
 
 // BRUTE SOLN
    // go over the array, check if sum of any two equals target and then return the indices O(n2) time

// BETTER SOLN
    // we're computing some redundant sums again and again which can be eliminated

    // even better soln
    // as there's only one target i can subtract it from each one and check if the number is in the array 

    // by making it a set? then return i and the index of the number in array shouldn't be same as i though just check that 
    // NO SET CAUSES MORE PROBLEM AS I WANT TO RETURN INDEX
    // HASHMAP TO RESCUE AS WE CAN HAVE {[NUM:INDEX]} kinda map
#define HASHSIZE 10000

// TYPEDEF for HashNode, HashMap is a pointer to the HashNode*
typedef struct HashNode {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

//HASH FUNCTIONS, please handle when creating keys
int hash(int key){
    return (key % HASHSIZE + HASHSIZE) % HASHSIZE;
    // need to do this so, there's always unique positive address
}

void insert(HashNode** hashMap, int key, int value){
    int idx = hash(key);
    HashNode* node = (HashNode*)malloc(sizeof(HashNode));
    node->key = key;
    node->value = value;
    node->next = hashMap[idx];
    // important to set hashMap[idx] as node
    hashMap[idx] = node;

}

// value is a pointer as we want to return the value where key matches idx on hashMap
bool find(HashNode** hashMap, int key, int* value){
    int idx = hash(key);
    printf("%d\n", idx);
    HashNode* node = hashMap[idx];
    while(node){
        printf("%d\n", key);
        printf("%d\n", node->key);
        if (node->key == key){
            *value = node->value;
            return true;
        }
        node = node->next;
    }
    return false;
}


int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashNode* hashMap[HASHSIZE] = { NULL };
    *returnSize = 2;
    int* result = (int*)malloc(*returnSize * sizeof(int));
    
    
    for (int i = 0; i < numsSize; i++){
        int diff = target - nums[i];
        int index;

        if(find(hashMap, diff, &index)){
            result[0] = i;
            result[1] = index;
            return result;
        }
        insert(hashMap, nums[i], i); //as number is key and index is value
    }

    *returnSize = 0;
    return result;

}