#-*- coding:utf-8 -*-

def quicksort(A, p=0, r=-1):
    if r is -1:
        r = len(A)
    if p < r-1:
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)

    return A

def partition(A,i,j):
    x = A[i]
    h = i
    for k in range(i+1, j):
        if A[k] < x:
            h = h+1
            A[h], A[k] = A[k], A[h]
    A[h], A[i] = A[i], A[h]

    return h

A = [3, 5, 2, 3, 7, 6, 4, 3]

print(quicksort(A,0,-1))