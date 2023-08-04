# n=3
# for i in range(n):
#     print("*"*(i+1))
# n=3
# print("\n")
# for k in range(3):
#     print("  "*(n-k-1),end="")
#     print("* "*(2*k+1),end="")
#     print("  "*(n-k-1))

# print("\n")

# m=20
# for a in range(m):
#     for b in range(m):
#         if (a==0 or b==0 or a==m-1 or b==m-1):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#         b+=1
#     print("\n",end="")
#     a+=1

n=3
for i in range(3,0,-1):
    print("* "*i)