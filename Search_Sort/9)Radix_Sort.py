'''
find largest element in array/list and x be number of digits in the largest element.
sort the array/list using counting sort but only consider ones place elements,next tens place and goes on for x times.
once the array/list is sorted by ones, then tenths and till the last place,the array/list is sorted.
--------------------------------------------------------------------------------------------------------------------------------
|note: here we used radix sort but we can use any stable sorting technique but counting sort works well here.                   |
|refer counting sort program to understand how it works.                                                                        |
--------------------------------------------------------------------------------------------------------------------------------
Time Complexity : O(n+k)    Space Complexity : O(max)   [k = range of elements in the array/list,ie lowest-greatest][max = greatest value of array/list]
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/radix-sort
'''


sort = [4, 1, 5, 3, 6]


def countingsort(array, Max, place):
    size = len(array)
    output = [0]*size
    count = [0]*(Max+1)
    for i in range(0, size):
        index = array[i]//place
        count[index % 10] += 1
    for i in range(1, Max+1):
        count[i] += count[i-1]
    i = size-1
    while i >= 0:
        index = array[i]//place
        output[count[index % 10]-1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


def radixsort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingsort(array, max_element, place)
        place *= 10


radixsort(sort)
print(sort)
