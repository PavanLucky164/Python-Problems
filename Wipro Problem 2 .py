"""
Description:

A company has a sales record of N products for M days. The company wishes to know the 
maximum revenue received from a given product of the N products each day. Write an algorithm 
to find the highest revenue received each day.

Input:

The first line of the input consists of two space-separatedIntegers-days (M) and products(N), 
representing the days and the products in the sales record.
The next M lines consist of N space-separated integers representing the sales revenue received 
from each product each day.

Output:

Print M space-separated integers representing the maximum received each day.

Example:

Input:

3 4
100 198 333 323
122 232 221 111
223 565 245 764

Output:

333 232 764


"""

def highest_revenue(sales_record):
    highest_revenue_in_each_day=list()
    for item in sales_record:
        item.sort()
        highest_revenue_in_each_day.append(item[-1])
    return highest_revenue_in_each_day


n=list(map(int,input().split()))
sales_record=list()
for i in range(n[0]):
    row=list(map(int,input().split()))
    sales_record.append(row)
highest_revenue_list=highest_revenue(sales_record)

result=[str(num) for num in highest_revenue_list]
print(" ".join(result))
