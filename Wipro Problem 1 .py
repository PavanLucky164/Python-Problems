"""
Finding the sum of numbers in thousands place,hundreads place,tens place and ones place in given numbers.
input is 4 digit numbers in that separate the thousands place number and hundreads place number and tens place number and ones place number.

formula = [smallest of thousands place numbers]+[largest of hundreads place numbers]+[smallest of tens place numbers]+[largest of ones place numbers]


suppose input is 
 3521 2452 1352 
 
output
 1522
 
"""

nums_list=input().split()
thousands=list()
hundreads=list()
tens=list()
ones=list()
for num in nums_list:
    for i in range(4):
        if i==0:
            int_num=int(num[i])
            thousands.append(int_num)
        if i==1:
            int_num=int(num[i])
            hundreads.append(int_num)
        if i==2:
            int_num=int(num[i])
            tens.append(int_num)
        if i==3:
            int_num=int(num[i])
            ones.append(int_num)
thousands.sort()
hundreads.sort()
tens.sort()
ones.sort()
E1=thousands[0]
E2=hundreads[-1]
E3=tens[0]
E4=ones[-1]
result=str(E1)+str(E2)+str(E3)+str(E4)
print(result)
