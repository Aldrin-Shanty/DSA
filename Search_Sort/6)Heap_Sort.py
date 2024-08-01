'''
first we need to heapify the list/array ie convert the list/array into a heap.
to heapify a tree, we arrange the (n//2)-1th value of the heap first and then we arrange the ((n//2)-1)-1th value and so on.
this is done since (n//2)-1th value is the last parent node in a heap,and once we arrange all the parent nodes from last to first,it becomes a heap.
inside heapify function we set parent as largest and compare the parent to its 2 children(here parent = i and 2 childeren are 2*i+1 and 2*i+2).
we check if both children indexes are less than n(length of list/array) to confirm the parent has either or both children.
if the child exists and its value is greater than parent it is set as largest.
after comparing parent to both children, if largest value has been shifted from parent to one of the children we swap the value at parent and greater child positions.
we will also recurse the function now with new parent as the previously largest index ie the current position of the parent after swap
this recursion is to rearrange values down the currently arranged value to be in place according to the new changes made just now.
if the new parent argument given during recursion is a node with no children or its children are not greater than itself then it will terminate.
this is done for all parent nodes from smallest parent node to the root parent node.
now the list/array is heapified.
after heapifying the list/array swap the first element in the list with the last element,this makes it so that the last element is the largest value.
now heapify the root node ie the first index of the list/array but with size of the heap as n-1 as the last element shouldnt be changed.
we dont change the last element since it is already in its sorted position.
now repeat the same by swapping first index and second last index and heapifying with root node as parent and size of heap as n-2.
now the second greatest element of the list/array is at second last index ie it is sorted.
repeat until heap size turns 0 and the entire list/array is sorted.
--------------------------------------------------------------------------------------------------------------------------------
|note: heap is a data structure where we represent an array/list in a tree format. there are 2 types of heaps generally.        |
|min heap :- heap where the root element is the smallest element in the heap and every parent is smaller than their children.   |
|max heap :- heap where the root element is the largest element in the heap and every parent is greater than their children.    |
|in order to sort in :                                                                                                          |
|           ascending order  -> max heap                                                                                        |  
|           descending order -> min heap                                                                                        |
|even though we say it is a heap and it is in form of a tree,it is still in code just an array/list                             |                                                                                                                            
--------------------------------------------------------------------------------------------------------------------------------
Time Complexity : O(nlogn)    Space Complexity : O(1)
Stability : No      (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/heap-sort
'''


sort = [4, 1, 5, 3, 6]


def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


heapsort(sort)
print(sort)
