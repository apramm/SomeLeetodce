class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size()+1; // the ideal range
        for (int num = 0; num <= n; num++){
            auto found = std::find(nums.begin(), nums.end(), num);
            if(found != nums.end()){
                continue;
            }else{
                return num;
            }
        }
        return NULL; 
    }
};