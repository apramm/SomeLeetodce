struct HashNode {
    int key;
    int value;
    struct HashNode* next;
};

bool containsNearbyDuplicate(int* nums, int numsSize, int k) {

    // TODO: find if there is an duplicate k distance from i (i != j)
    // MY SOLUTION IN FIRST 
    // for (int i = 0; i < numsSize; i++){ // go through arr and check till kth distance variable if it's equal and update the k val
    // int temp = k;
    //     while(temp!=0){
    //         if(i+temp >= numsSize){
    //             temp -=1;
    //         }else if(nums[i] != nums[i+temp]){ 
    //             // if the numbers not match check all the before ones
    //             temp -= 1;
    //         }else if(nums[i] == nums[i+temp]){
    //             return true;
    //         }
    //     }
    // }
    // return false;

    //OPTIMIZED Using HASHMAP IDEATION
    // make a seen map/set {val:index}
    // iterate over list and try to find the value in map O(1) lookup
    // compare if the difference of indices <= k if yes, return true
    // else insert in the map
    // after iteration return false


    struct HashNode** hashMap = (struct HashNode**)calloc(numsSize, sizeof(struct HashNode*)); //allocate hashmap which is a pointer to a pointer to hashnode and initialize to val to 0

    for (int i = 0; i < numsSize; ++i) { //for each index
        int currentNum = nums[i]; // current num
        int hashIndex = abs(currentNum) % numsSize; // create a hashIndex

        struct HashNode* node = hashMap[hashIndex]; // create a pointer to the hashnode positioned at hashIndex

        while (node) { //
            if (node->key == currentNum) { // if the node->key match num
                if (i - node->value <= k) { // if index - node->values <= k
                    free(hashMap);
                    return true;
                } else {
                    node->value = i;
                    break;
                }
            }
            node = node->next;
        }

        if (!node) {
            node = (struct HashNode*)malloc(sizeof(struct HashNode));
            node->key = currentNum;
            node->value = i;
            node->next = hashMap[hashIndex];
            hashMap[hashIndex] = node;
        }
    }

    free(hashMap);
    return false;
}