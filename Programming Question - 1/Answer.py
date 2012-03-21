path = "/media/New Volume/Currently Reading/Algorithms Class - Stanford/Algo_Class_I/Programming Question - 1/IntegerArray.txt"

#Taking the input from the file, splitting it on newline, we get last element as empty, hence we take all elements except that
input = open(path).read().split("\r\n")[:-1]

#Map the List of string numbers = ['1', '11'] -> [1, 11]
input1 = map(int, input)

def Count (A_arr, n):

    if n == 1:
        return A_arr, 0

    #Send the left half, doing len on it so that odd numbers do not get a length of 1, so if A has 3 elements doing a simple 3/2 == 1, therefore doing a len to check
    (B_arr, x) = Count(A_arr[:n/2], len(A_arr[:n/2]))
    (C_arr, y) = Count(A_arr[n/2:], len(A_arr[n/2:]))

    #Pass the newly sorted list
    (D_arr, z) = Merge_and_Count_Inversion(B_arr, C_arr, n)


    #Return the sorted list and the count
    return D_arr, x+y+z

def Merge_and_Count_Inversion(B_arr, C_arr, n):
    count = 0
    D_arr = []
    while B_arr and C_arr:

        if C_arr[0] < B_arr[0]:
            count += len(B_arr)
            D_arr.append(C_arr.pop(0))
        else:
            D_arr.append(B_arr.pop(0))

    while B_arr:
        D_arr.append(B_arr.pop(0))

    while C_arr:
        D_arr.append(C_arr.pop(0))

    return (D_arr, count)

(sort_deq, count) = Count(input1, len(input))
