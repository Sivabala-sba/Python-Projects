# python3 program to find maximum in arr[] of size n

def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i]> max:
            max = arr[i]
    return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Larget in given array is ", Ans)
