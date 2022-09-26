'''
Matthew Sharp - 100748071
Purpose: This code emulates the merge sort algorithm, given a random length of an array
Output: Prints the sorted array with the time taken to sort the array
'''

import math
import time
import random

# merge function used to combine the two sorted subarrays
# Input: array of values, lower bound index, middle index, upper bound index
def merge(arr, p, q, r):
    n1 = q - p + 1              # Gets the length of the first half of the array
    n2 = r - q                  # Gets the length of the second half of the array
    L = [0]*(n1+1)              # Generates first half array length
    R = [0]*(n2+1)              # Generates second half array length
    for i in range(n1):
        L[i] = arr[p+i]         # Puts the first half of array into a subarray
    for j in range(n2):         
        R[j] = arr[q+1+j]       # Puts the second half of the array into a sub aray

    L[n1]=math.inf              # Adds infinty to the end of both subarrays
    R[n2]=math.inf
    
    i = 0                       # Used to increment through the left subarray
    j = 0                       # Used to increment through the right subarray
    for k in range(p,r+1):
        if L[i] <= R[j]:        # If the current indexed element on the right subarray is greater or equal to the 
            arr[k] = L[i]       # indexed element of the left subarray it places the next 
            i = i + 1           # element in the left subarray into the current position of the base array
        else:
            arr[k] = R[j]       # If left subarray index element is greater than the right subarray
            j = j + 1           # place the right subarray element into the base array

# mergeSort function called recursively to perform the merge sort algorithm, breaking the problem into subarrays
# Input: array, lower bound index, upper bound index
def mergeSort(arr, p, r):
    if p < r:
        q = math.floor((p+r)/2)     # Gets the middle index
        mergeSort(arr,p,q)        
        mergeSort(arr,q+1,r)
        merge(arr, p, q, r)

arr = []
for i in range(1000000):
    arr.append(random.randint(0, 10000))        # Randomly generated array of numbers
n = len(arr)
print("Generated array:")
#for i in range(n):         # Used to print initial array
#    print(arr[i])

s = time.time()
mergeSort(arr, 0, n-1)
e = time.time()
print("\n\nSorted array:")
for i in range(n):
    print(arr[i])
print("Time Taken:", e-s)       # Time taken to sort the array printed