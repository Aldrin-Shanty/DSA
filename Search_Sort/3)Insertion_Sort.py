'''
take second element of array as key.
if key is smaller than element just behind key position,place the element behind key to key position(key value doesnt change,it still remains the same).
move right and check if key is smaller than it and do the same as above.
repeat above step till end of rightside of elements.
reppeat the entire steps above with 3rd elemenet as key and so on till last element as key.
Time Complexity : O(n^2)    Space Complexity : O(1)
Stability : Yes     (Stability means that two elements with equal value will retain their relative postion even after sorting)
Further Info : https://www.programiz.com/dsa/insertion-sort
'''

sort = [4, 1, 5, 3, 6]

for i in range(1, len(sort)):
    key = sort[i]
    j = i-1
    while j >= 0 and key < sort[j]:
        sort[j+1] = sort[j]
        j = j-1
    sort[j+1] = key


print(sort)
