def InsertionSort(seq):
    for i in range(1, len(seq)):
        selected_value = seq[i]

        # Comparing the element with the sorted items
        while seq[i-1] > seq[i] and i != 0:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1

    return seq

unordered_list = [4,8,3,1,6,9,36,17,84,14,74]
print(InsertionSort(unordered_list))
