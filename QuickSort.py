def quick_sort(arr):
	if len(arr) <=1:
		return arr
	pivot = arr[0]
	less = [ x for x in arr[1:] if x <= pivot]
	more = [ x for x in arr[1:] if x > pivot]
	return quick_sort(less) + [pivot] + quick_sort(more)

print("Enter the values of the array:")
arr = list(map(int, input().split()))
sorted_array = quick_sort(arr)
print("The sorted array is:", sorted_array)