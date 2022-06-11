
# string s
# permutation p 
# the length == n

# [1,2,3] and [1,2,3,4,5] is permutation
# because every element from 1 to n occurs only once.

# multiply s by p  s --> new
# s = wmbe p=[3,1,4,2] --> s=s_3,s_1,s_4,s_2=bwem

# how many operations the string would become equal to its initial value for the first time

# t -- testcase
# n -- the length of string and permutation
# s -- string s of length n, containing lowercase
# p -- permutation

test_case = int(input())

for i in range(test_case):
    n = int(input())
    origin_str=input()
    perm=input().split(' ')
    perm_cnt=0
    temp_str=origin_str
    new_str=''
    while origin_str != new_str:
        perm_cnt+=1
        new_str=''
        for num in perm:
            num=int(num)
            new_str+=(temp_str[num-1])
        temp_str=new_str
    print(perm_cnt)


# codeforces
# 8 6 1 7 5 2 9 3 10 4

# ababa  
# 3 4 5 2 1

# 8 6 1 7 5 2 9 3 10 4

# 5->5
# 6->2
# 7->9->10->4 -- 7  (4)
# 8 -> 3 -> 1 -- 8  (3)


#  3->5->1
#  4->2


# check if new str == origin_str
# yes --> return cnt
# no --> origin_str=new_str
