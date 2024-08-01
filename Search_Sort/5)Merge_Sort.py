'''
divide the list/array into 2 lists/arrays.
the 2 lists/arrays are recursed into the same function.
reapeat it until u create a list/array of length 1 of each element in original array.
now merge the originally adjacant values into an array/list of length 2 and sort it.
keep merging the lists until all the lists are merged into a single sorted list/array.
Time Complexity : O(nlogn)    Space Complexity : O(n)
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/merge-sort
'''
sort = [4, 1, 5, 3, 6]


def mergesort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergesort(L)
        mergesort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


mergesort(sort)
print(sort)
