class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // OPTIMAL
        int res = nums.size(); //initialize result with n
        for (int i = 0; i < nums.size(); i++){
            res += i - nums[i];
        }
        return res;


        // NOT GOOD AS O(N2 COMPLEXITY DUE TO FIND)
        // int n = nums.size()+1; // the ideal range
        // for (int num = 0; num <= n; num++){
        //     auto found = std::find(nums.begin(), nums.end(), num);
        //     if(found != nums.end()){
        //         continue;
        //     }else{
        //         return num;
        //     }
        // }
        // return NULL; 
    }
};