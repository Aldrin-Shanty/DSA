'''
swaps adjacent elements in array based on if its ascending or descending sorting. 
every adjacent pairs are compared and swapped n-1 times.
after that,last position is in order.
repeat swapping adjacent pairs but only till 2nd last element(as last element is sorted)
keep repeating until all positions are sorted.
Time Complexity : O(n^2)    Space Complexity : O(1)
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/bubble-sort
'''


sort = [4, 1, 5, 3, 6]


for i in range(len(sort)-1):
    for j in range(len(sort)-i-1):
        if (sort[j] > sort[j+1]):
            sort[j], sort[j+1] = sort[j+1], sort[j]


print(sort)
