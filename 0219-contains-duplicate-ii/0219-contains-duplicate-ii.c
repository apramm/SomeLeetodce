// bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
//     // TODO: find if there is an duplicate k distance from i (i != j)
//     for (int i = 0; i < numsSize; i++){ // go through arr and check till kth distance variable if it's equal and update the k val
//     int temp = k;
//         while(temp!=0){
//             if(i+temp >= numsSize){
//                 temp -=1;
//             }else if(nums[i] != nums[i+temp]){ 
//                 // if the numbers not match check all the before ones
//                 temp -= 1;
//             }else if(nums[i] == nums[i+temp]){
//                 return true;
//             }
//         }
//     }
//     return false;

//     //OPTIMIZED Using HASHMAP maybe? in Cpp
//     // make a seen map/set {val:index}
//     // iterate over list and try to find the value in map O(1) lookup
//     // compare if the difference of indices <= k if yes, return true
//     // else insert in the map
//     // after iteration return false

    
// }

struct HashNode {
    int key;
    int value;
    struct HashNode* next;
};

bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    struct HashNode** hashMap = (struct HashNode**)calloc(numsSize, sizeof(struct HashNode*));

    for (int i = 0; i < numsSize; ++i) {
        int currentNum = nums[i];
        int hashIndex = abs(currentNum) % numsSize;

        struct HashNode* node = hashMap[hashIndex];
        while (node) {
            if (node->key == currentNum) {
                if (i - node->value <= k) {
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