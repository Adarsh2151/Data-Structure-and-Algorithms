
def selection_sort(arr):

    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]

    return arr


if __name__ == "__main__":
    arr = [8,6,9,3,74,9,3,]
    print(selection_sort(arr))