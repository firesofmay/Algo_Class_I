path = "/media/New Volume/Currently Reading/Algorithms Class - Stanford/Algo_Class_I/Programming Question - 1/IntegerArray.txt"

#Taking the input from the file, splitting it on newline, 
#we get last element as empty, hence we take all elements except that last element
input = open(path).read().split("\r\n")[:-1]

#Map the List of string numbers = ['1', '11'] -> [1, 11]
int_input = map(int, input)

def Count (A_list, n):

    if n == 1:
        return A_list, 0

    # Send the left and right half, 
    # doing len on it so that odd numbers do not get a length of 1, 
    #so if A has 3 elements doing a simple 3/2 != 1, 
    #therefore doing a len to check
    #Returns the Sorted Partial List and the number of inversions counted
    (B_list, x) = Count(A_list[:n/2], len(A_list[:n/2]))
    (C_list, y) = Count(A_list[n/2:], len(A_list[n/2:]))

    #Pass the newly sorted list
    #Returns the merged sorted list and the inversions counted
    (D_list, z) = Merge_and_Count_Inversion(B_list, C_list, n)


    #Return the sorted list and the sum of inversions count
    return D_list, x+y+z

def Merge_and_Count_Inversion(B_list, C_list, n):

    #Initialize count of inversions
    count = 0

    #Final Temp sorted list of B + C
    D_list = []

    while B_list and C_list:

        #If the right halfs first element is smaller than 
        #left halfs first element than you have 
        #number of inversions = len(elemnts left in B)
        #pop out the element in C and append it to D
        if C_list[0] < B_list[0]:
            count += len(B_list)
            D_list.append(C_list.pop(0))

        #If the left half is smaller, 
        #it does not add to the count of inversions, 
        #simply pop the first element off from B and append it to D
        else:
            D_list.append(B_list.pop(0))

    #Append all the Elements left in B and C
    D_list = D_list + B_list + C_list

    #Return the new sorted array and the count of inversions
    return (D_list, count)

(sorted_list, count) = Count(int_input, len(int_input))
print count
