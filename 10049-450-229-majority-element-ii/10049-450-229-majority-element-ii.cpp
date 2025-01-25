#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        int a, b = 0;
        int ele1 = INT_MIN;
        int ele2 = INT_MIN;

        for(auto num : nums){
            if(a==0 && ele2!=num){
                a=1;
                ele1 = num;
            }
            else if(b==0 && ele1!=num){
                b=1;
                ele2 = num;
            }
            else if(num==ele1)a++;
            else if(num==ele2)b++;
            else{
                a--;
                b--;
            }
        }
        vector<int> res;
        int min = n/3;
        int c1, c2 = 0;
        for(auto it : nums){
            if(it==ele1)c1++;
            else if(it==ele2)c2++;
        }
        if(c1>min){
            res.push_back(ele1);
        }
        if(c2>min){
            res.push_back(ele2);
        }
        return res;
    }   
};