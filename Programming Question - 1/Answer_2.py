path = "/media/New Volume/Currently Reading/Algorithms Class - Stanford/Algo_Class_I/Programming Question - 1/IntegerArray.txt"

#Taking the input from the file, splitting it on newline, we get last element as empty, hence we take all elements except that
input = open(path).read().split("\r\n")[:-1]

#Map the List of string numbers = ['1', '11'] -> [1, 11]
input1 = map(int, input)

def Count (A_arr, n):

    if n == 1:
        return A_arr, 0

    # Send the left and right half, 
    # doing len on it so that odd numbers do not get a length of 1, so if A has 3 elements doing a simple 3/2 != 1, therefore doing a len to check
    #Returns the Sorted Partial List and the number of inversions counted
    (B_arr, x) = Count(A_arr[:n/2], len(A_arr[:n/2]))
    (C_arr, y) = Count(A_arr[n/2:], len(A_arr[n/2:]))

    #Pass the newly sorted list
    #Returns the merged sorted list and the inversions counted
    (D_arr, z) = Merge_and_Count_Inversion(B_arr, C_arr, n)


    #Return the sorted list and the sum of inversions count
    return D_arr, x+y+z

def Merge_and_Count_Inversion(B_arr, C_arr, n):

    #Initialize count of inversions
    count = 0

    #Final Temp sorted list of B + C
    D_arr = []

    while B_arr and C_arr:

        #If the right halfs first element is smaller than left halfs first element than you have number of inversions = len(elemnts left in B)
        #pop out the element in C and append it to D
        if C_arr[0] < B_arr[0]:
            count += len(B_arr)
            D_arr.append(C_arr.pop(0))

        #If the left half is smaller, it does not add to the count of inversions, 
        #simply pop the first element off from B and append it to D
        else:
            D_arr.append(B_arr.pop(0))

    #Append all the Elements left in B and C
    D_arr = D_arr + B_arr + C_arr

    #Return the new sorted array and the count of inversions
    return (D_arr, count)

(sort_deq, count) = Count(input1, len(input))
print count
