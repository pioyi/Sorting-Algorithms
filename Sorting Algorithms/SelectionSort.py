# # # # # # # # # # # #
#    Selection Sort   #
# # # # # # # # # # # #

# Average    O(n²)
# Worst      O(n²)
# Best       O(n²)

def SelectionSort(seq):
    for i in range(len(seq)):
        minimum = i

        # Search for another smaller value
        for j in range(i+1, len(seq)):
            if seq[minimum] > seq[j]:
                minimum = j

        # Swap the two items
        seq[i], seq[minimum] = seq[minimum], seq[i]   

    return seq
    
unordered_list = [4,8,3,1,6,9,36,17,84,14,74]
print(SelectionSort(unordered_list))