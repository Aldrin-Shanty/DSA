'''
let us assume length of array/list = n = 8
first find the middle of the list/array ie n//2th element.
store the middle as temp.
compare it with first element and if first element is greater,place the greater element at temp element's index but keep the temp element in temp.
then place the temp variable value in the position of the greater element(yes,it is a swap but upon next iteration this will be different).
if first element is smaller than or equal to temp element compare the second element and second from the temp element index.
that means set a pointer at start and middle of array/list and swap and iterate both pointers to traverse the array/list.
once the traversal is complete, now take the middle of the first half of the array ie 25th percentile or n//4th element of the array/list as temp.
compare the first element and temp element.
if the element is greater than temp element,then similar to before its a basic swap of the two elements.
same goes for when comparing the 2nd element and temp index+1 element ie 4th element.
IMPORTANT:
    but next iteration onwards,we compare the temp+2th element ie 5th element with 3rd element and 1st element,
    ie we compare all elements from the temp element to start of index with a gap of 2, here it is 5th 3rd 1st
    we compare temp(5th) and 3rd element and if 3rd is greater we set 3rd element as 5th element(temp is still the former 5th element).
    next we compare the temp element and 1st element of the array and if 1st element is greater we do the same as before.
    this goes on until there are no other indexes at the left to compare temp with or temp is greater than the value its compared with.
    if temp is compared with last element in the array/list to be compared with then place temp there after placing the value there at previously compared index. 
next iteration we compare 6th 4th 2nd,we can see this pattern in first iteration if length of list/array is big enough(>8).
once traversal is complete, set temp as n//8th element,ie 2nd element.
do the same traversal.
since n=8 and 8//16 would be 0 we terminate the process and array/list is sorted
Time Complexity : O(nlogn)    Space Complexity : O(1)
Stability : No     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/shell-sort
'''


sort = [4, 1, 5, 3, 6]


def shellsort(array, n):
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j-interval] > temp:
                array[j] = array[j-interval]
                j -= interval
            array[j] = temp
        interval //= 2


shellsort(sort, len(sort))
print(sort)
