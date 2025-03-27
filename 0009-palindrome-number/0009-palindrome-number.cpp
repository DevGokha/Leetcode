class Solution {
public:
    bool isPalindrome(int x) {
       bool ans;
       if(x < 0){
        return false;
       }
       long long reversed = 0;
       long long n = x;
       while(n != 0){
         int ld  =n%10;
         reversed = reversed *10 + ld;
         n = n/10;
       } 
       return (reversed == x);
    }
};