

def merge(arr, s, e):
    mid= (s+e)//2

    left_arr=arr[s:mid+1]
    right_arr = arr[mid+1:e+1]

    len_left = len(left_arr)
    len_right= len(right_arr)

    index_left, index_right, main_arr_index = 0, 0, s

    while((index_left<len_left) and (index_right<len_right)):
        if left_arr[index_left]<right_arr[index_right]:
            arr[main_arr_index]=left_arr[index_left]
            index_left+=1
        else:
            arr[main_arr_index] = right_arr[index_right]
            index_right+=1
        main_arr_index+=1

    while(index_left<len_left):
        arr[main_arr_index] = left_arr[index_left]
        index_left += 1
        main_arr_index += 1

    while(index_right<len_right):
        arr[main_arr_index] = right_arr[index_right]
        index_right += 1
        main_arr_index += 1

def merge_sort(arr, s, e):
    if s>=e:
        return
    mid= (s+e)//2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid+1, e)
    merge(arr, s, e)

if __name__ == "__main__":
    arr = [2, 1, 6, 9, 4, 5]
    size = len(arr)
    s = 0
    e = size - 1

    print("Before merge sort:")
    print(" ".join(map(str, arr)))

    merge_sort(arr, s, e)

    print("After merge sort:")
    print(" ".join(map(str, arr)))