class Solution {
public:

    int rev(int n ){
        int r =0;
        while(n>0){
            r*=10;
            r+=(n%10);
            n/=10;
        }
        return r;
    }
    int countNicePairs(vector<int>& arr) {
        int n = arr.size();
        int count =0;
        unordered_map<int,int> m;
        for(int i =0; i<n; i++){
            arr[i] -= rev(arr[i]);
        }
        for(int i =0; i<n; i++){
            if(m.find(arr[i])!= m.end()){
            count = count%1000000007;
            count += m[arr[i]];
            m[arr[i]]++;
            }
            else{
                m[arr[i]]++;
            }
        }
        return count%1000000007;
    }
};