class Solution {
public:
    int fib(int n) {
        
       if(n==0|| n==1) return n;
       int a = 0;
       int b =1;
       int c= a+b;

       for(int i = 2; i<n; i++){
        a= b;
        b=c;
        c = a+b;
       }
        return c;
    }
};