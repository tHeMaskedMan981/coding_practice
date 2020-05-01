#include <istream>
#include <vector>
#include <map>
#include <iterator> 
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int,int> map1;
        
        for (int i=0; i<nums.size(); i++){
            map1.insert(pair<int, int>(nums[i], i));
        }
        
        for (int i=0; i<nums.size(); i++){
            int complement = target - nums[i];
            
            auto itr = map1.find(complement);
            if (itr!=map1.end() && i!=itr->second)
                return {i, itr->second};
        }
        
        return {};
    }
};