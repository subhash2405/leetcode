#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        nums.push_back(k);
        priority_queue<int, vector<int>, greater<int>> pq(nums.begin(), nums.end());
        int ans = 0;
        while(pq.size()>1 && pq.top()<k){
            int a = pq.top();
            pq.pop();
            int b = pq.top();
            pq.pop();
            if(2LL*a+b<k){
            pq.push(a*2+b);}
            ans++;
        }
        return ans;
    }
};