"""
Consecutive sum triangle

Ex:- input 1 2 3
     output [1,2,3]
            [3,5]
            [8]
"""
def sums_list(nums_list):
    list_length=len(nums_list)
    new_list=list()
    sum=0
    for i in range(list_length-1):
        sum=nums_list[i]+nums_list[i+1]
        new_list.append(sum)
    print(new_list)
    nums_list=new_list
    return nums_list

nums_list=list(map(int,input().split()))
print(nums_list)
for i in range(len(nums_list)-1):
    nums_list=sums_list(nums_list)
