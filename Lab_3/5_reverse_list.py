def reverse_list():
    arr = input("Enter an array of elements separated by space: ").split()
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list())
