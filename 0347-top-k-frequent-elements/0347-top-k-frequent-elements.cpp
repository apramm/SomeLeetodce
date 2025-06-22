#include <iostream>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for (int num : nums){
            count[num] += 1;
        }
    // TO PRINT EA VALUE NEED TO ITERATE OVER
    //     for (const auto& entry : count) {
    //     cout << "Key: " << entry.first << ", Value: " << entry.second << endl;
    // }
        // CREATE BUCKETS with freq:[int1, int2, ..]
        vector<vector<int>> buckets(nums.size()+1);
        for(auto& entry: count){
            buckets[entry.second].push_back(entry.first);
        }
        
        vector<int> res;
        for (int i = buckets.size()-1; i >= 0; --i){
            if(!buckets[i].empty()){
                res.insert(res.end(), buckets[i].begin(), buckets[i].end());
                if(res.size() >= k){
                    res.resize(k);
                    break;
                }
            }
        }
        return res;
    }
};