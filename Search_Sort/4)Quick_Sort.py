'''
select pivot element(here last element is set as pivot).
traverse the array/list using two variable/pointers(here i and j)
j will normally traverse the list/array but i will only traverse to the next element if the data j is pointing at is lower than or equal to pivot.
also whenever i traverses ie when we find a smaller or equal value to pivot, we swap elements at pointer i and j.
continue traversing the array/list until the end ,and at the end ,pivot element is swapped with element at ith position.
after this we can see that the original pivot element will be now in its sorted position.
now use recursion to do the same steps as above to other elements by splitting the array/list into 2 halves and performing same function(above steps) on them.
the 2 halves are one before the pivot element and one after the pivot element.
do the same for them as seperate lists/arrays.
once the array/list cannot be split the sorting is done.
--------------------------------------------------------------------------------------------------------------------------------
|note: in the code i is initially -1(doesnt mean the last index of the array(ignore this if u dont understand what it means))  |
|i is set as -1 so that we increment its value when we find a lower element and need to swap.                                  |        
|and that is why when swapping pivot after the for loop, we write it as i+1 since we need to increment i again.                |
--------------------------------------------------------------------------------------------------------------------------------
Time Complexity : O(nlogn)    Space Complexity : O(1)
Stability : No     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/quick-sort
'''


sort = [4, 1, 5, 3, 6]


def partition(array, low, high):
    pivot = array[high]
    i = low-1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p-1)
        quicksort(array, p+1, high)


quicksort(sort, 0, len(sort)-1)
print(sort)
