'''
merge_sort([2, 1, 6], 0, 2)
│
├─ merge_sort([2, 1, 6], 0, 1)   # Left half [2, 1]
│  │
│  ├─ merge_sort([2, 1, 6], 0, 0) # Base case, single element [2]
│  │
│  └─ merge_sort([2, 1, 6], 1, 1) # Base case, single element [1]
│  │
│  └─ merge([2, 1, 6], 0, 1)      # Merge [2] and [1] into [1, 2]
│
└─ merge_sort([2, 1, 6], 2, 2)   # Right half [6]
│                                  # Base case, single element [6]
│
└─ merge([1, 2, 6], 0, 2)         # Merge [1, 2] and [6] into [1, 2, 6]

'''


def merge(arr, s, e):
    # Calculate the middle index of the current segment of the array
    mid = (s + e) // 2

    # Divide the array segment into two halves
    left_arr = arr[s:mid + 1]
    right_arr = arr[mid + 1:e + 1]

    # Determine the length of the left and right segments
    len_left = len(left_arr)
    len_right = len(right_arr)

    # Initialize pointers for left_arr, right_arr, and the main array
    index_left, index_right, main_arr_index = 0, 0, s

    # Merge the two halves into the main array
    while index_left < len_left and index_right < len_right:
        if left_arr[index_left] < right_arr[index_right]:
            arr[main_arr_index] = left_arr[index_left]
            index_left += 1
        else:
            arr[main_arr_index] = right_arr[index_right]
            index_right += 1
        main_arr_index += 1

    # If there are any remaining elements in left_arr, add them to the main array
    while index_left < len_left:
        arr[main_arr_index] = left_arr[index_left]
        index_left += 1
        main_arr_index += 1

    # If there are any remaining elements in right_arr, add them to the main array
    while index_right < len_right:
        arr[main_arr_index] = right_arr[index_right]
        index_right += 1
        main_arr_index += 1

def merge_sort(arr, s, e):
    # Base case: If the segment size is 1 or 0, it's already sorted
    if s >= e:
        return

    # Calculate the middle index
    mid = (s + e) // 2

    # Recursively apply merge_sort to the left half
    merge_sort(arr, s, mid)

    # Recursively apply merge_sort to the right half
    merge_sort(arr, mid + 1, e)

    # Merge the two sorted halves
    merge(arr, s, e)

if __name__ == "__main__":
    arr = [2, 1, 6, 9, 4, 5]
    size = len(arr)
    s = 0
    e = size - 1

    print("Before merge sort:")
    print(" ".join(map(str, arr)))

    # Perform merge sort on the entire array
    merge_sort(arr, s, e)

    print("After merge sort:")
    print(" ".join(map(str, arr)))
