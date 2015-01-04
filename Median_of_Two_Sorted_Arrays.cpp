class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        return (((m+n)%2==0)?((findK(A, m, B, n, (m+n)/2)+findK(A, m, B, n, (m+n)/2+1))/2.0):(findK(A, m, B, n, ((m+n)/2+1))));
    }
    
    double findK(int A[], int m, int B[], int n, int k) {
        if(m<n) return findK(B, n, A, m, k);
        if(n==0) return A[k-1];
        if(k==1) return min(A[0],B[0]);
        else {
            int j = min(n, k/2);
            int i = k - j;
            if(A[i-1]==B[j-1]) return A[i-1];
            else if(A[i-1]>B[j-1]) return findK(A, m, B+j, n-j, k-j);
            else return findK(A+i, m-i, B, n, k-i);
        }
    };

};