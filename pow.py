# from math import pow
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return (pow(x,n))

# sol=Solution()
# print(sol.myPow(2,2))
# print(pow(2,-2))

# n=90
# i=0
# while i*i<=n:
#     i+=1
# print(i-1)


class Solution:
    def mySqrt(self, n: int) -> int:
        low=1
        high=n
        temp=-1
        if n==0:
            print(n)
            return 0
        while high>=low:
            mid=(high+low)//2
            # print(mid)
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                temp=mid
                low=mid+1
            else:
                # temp=mid
                high=mid-1
        return (temp)
    
sol=Solution()
print(sol.mySqrt(16))