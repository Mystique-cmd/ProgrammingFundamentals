def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]#swaps the elemants
    return arr  

print("Enter the elements of the array separated by space:")
arr = list(map(int, input().split()))
sorted_arr = Bubble_Sort(arr)
print("Sorted array is:", sorted_arr)
