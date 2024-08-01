'''
set first element as minimum.
compare it with every element on the right of that element and set whichever is smallest as min.
swap min element and first element.
now first element in array is in sorted position.
now repeat above steps for second element and keep doing the same till last element is sorted.
Time Complexity : O(n^2)    Space Complexity : O(1)
Stability : No     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/selection-sort
'''


sort = [4, 1, 5, 3, 6]


for i in range(len(sort)):
    min = i
    for j in range(i+1, len(sort)):
        if sort[j] < sort[min]:
            min = j
    sort[min], sort[i] = sort[i], sort[min]


print(sort)
