#include <iostream>
#include<algorithm>
#include <vector>
using namespace std;

int main(){

    string s = "abc";
    s.insert(0, "d");
    vector<int> nums = {1,2,3,4};
    vector<int>::iterator it = find(nums.begin(), nums.end(), 4);
    cout<< distance(nums.begin(),it)<<endl;
    cout<<s;
    return 0;
}