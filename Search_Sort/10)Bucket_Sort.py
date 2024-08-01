'''
create a array/list called bucket with size equal to 10 time the greatest value floored down +1 ie floor(max(array/list)*10)+1.
add empty arrays/lists into each slot of the bucket.
traverse the array/list to sort and store the element from the array/list into (floor(element*10))th index of the bucket.
ie append the element to the list/array in the bucket.
now sort every array/list inside the bucket using a stable sorting method.
now assign every value present in all arrays/lists inside the bucket onto the array/list to be sorted.
Time Complexity : Avg = O(n)    Worst = O(n^2)    Best = O(n+k)     More info on time complexity of bucket sort below the code
Space Complexity : O(n+k)   [k = size of bucket list/array]
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/bucket-sort
'''


from math import floor


sort = [2.42, 5.32, 3.33, 2.52, 3.37, 1.47, 2.51]


def bucketSort(array, bsize):
    bucket = []
    for i in range(bsize):
        bucket.append([])
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(bsize):
        # here we use inbuilt sort method(tim sort), we can use any stable sorting method
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(bsize):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1


bucketSort(sort, floor((max(sort)*10))+1)
print(sort)

'''
Time Complexities:-             [k = time complexity of inner sorting used in its best case]
Worst Case Complexity: O(n^2)
When there are elements of close range in the array, they are likely to be placed in the same bucket.
This may result in some buckets having more number of elements than others.
It makes the complexity depend on the sorting algorithm used to sort the elements of the bucket.
The complexity becomes even worse when the elements are in reverse order. If insertion sort is used to sort elements of the bucket,
    then the time complexity becomes O(n^2).
Best Case Complexity: O(n+k)
It occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each bucket.
The complexity becomes even better if the elements inside the buckets are already sorted.
If insertion sort is used to sort elements of a bucket then the overall complexity in the best case will be linear ie. O(n+k).
O(n) is the complexity for making the buckets and O(k) is the complexity for sorting the elements of the bucket using 
    algorithms having linear time complexity at the best case.
Average Case Complexity: O(n)   [technically it is O(n + (n^2/k) + k) but we assume k = n for average case and hence it becomes O(n)]
It occurs when the elements are distributed randomly in the array. 
Even if the elements are not distributed uniformly, bucket sort runs in linear time. 
It holds true until the sum of the squares of the bucket sizes is linear in the total number of elements.
'''
