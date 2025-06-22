// we don't need first here as we assume first should be 1
int computeMissingElementsTillIndex(int* arr, int index){
    return (arr[index]- 1) - index;
    // we subtract the expected index from actual index to get the number of missing elements till that index
}
int findKthPositive(int* arr, int arrSize, int k) {
    // As it's a sorted array,
    // BRUTE FORCE
    // for my brute force solution: I'll just iterate over the array once and keep track of the missing elements by checking for j=0 to k: nums[i+1] == nums[i] + i, if not then i'll add that in an array and return the kth one but that's O(nk) in worst case

    // OPTIMIZED
    // I've a better approach in mind that will use some index arithmetic to calculate the number of missing elements and then we can get the minimum index till which we miss k elements by using binary search
    // this will be efficient as calculating missing elements is O(1) and the binary search can be done in O(log n) as the array is already sorted

    // to ease the calculations that will done i'll create a helper function to computeMissingElementsTillIndex

    // EDGE : we'd need to check an edge case where if the number of missing elements are less than k (i.e., the missing element that needs to be returned)
    if (computeMissingElementsTillIndex(arr, arrSize-1) < k){
        return arr[arrSize-1] + (k-computeMissingElementsTillIndex(arr, arrSize-1));
        // RETURN THE element that comes after remaining missing elements 
    } 

    // After covering the edge case we need to do binary search to effectively find the missing element within the array itself
 // Binary search
    int left = 0, right = arrSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (computeMissingElementsTillIndex(arr, mid) >= k) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

  
    // ANOTHER EDGE CASE ONE ELEMENT WHICH IS MISSNG BEFORE THE BEGINING THEN, WE STRAIGHT UP RETURN K as starting from 1 that should be kth missed positive num
    if (left == 0) return k;

      // once we've found the minimum index i.e., left before which the k elements are missing we can simply use the out of bound technique to return the kth positive in missing in the array
    return arr[left - 1] + (k - computeMissingElementsTillIndex(arr, left - 1));

}