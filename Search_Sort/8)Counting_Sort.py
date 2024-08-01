'''
find maximum element in array/list.
create an array/list of length max+1 with initial values 0 to store count of elements in array/list.
assign count of each occurence in the original array/list to the count array/list index, ie if 5 occurs once, set 5th index value in count as 1.
make the count array/list cumulative.
create the output array/list. find first element of array/list to sort as index for count array/list. take value in count-1,
and store the first element of array to sort in index count-1 of the output array/list. also decrease the count of that index.
the output array/list is sorted.
Time Complexity : O(n+k)    Space Complexity : O(k)   [k = range of elements in the array/list,ie lowest-greatest][max = greatest value of array/list]
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/counting-sort
'''


sort = [4, 1, 5, 3, 6]


def countingsort(array, Max):
    size = len(array)
    output = [0]*size
    count = [0]*(Max+1)
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, Max+1):
        count[i] += count[i-1]
    i = size-1
    while i >= 0:
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]


countingsort(sort, max(sort))
print(sort)
