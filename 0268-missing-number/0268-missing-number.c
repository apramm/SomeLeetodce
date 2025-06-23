int missingNumber(int* nums, int numsSize) {
    // we know that the size is the range expected
    // can use a simple arithmetic technique to find the missing number
    // sum of actual range - sum of all the exisitng range = missing number
    int missingNumber = numsSize;
    for (int i = 0; i < numsSize; i++){
        missingNumber += i - nums[i];
    } 
    return missingNumber;
}