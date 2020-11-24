def Quicksort(seq):
    if len(seq) < 2:
        return seq
    
    pivot = seq.pop()
    left_side, right_side = [], []

    for item in seq:
        # Append the rest of the list's values into either side based on their value
        if item < pivot:
            left_side.append(item)
        else:
            right_side.append(item)

    # Call the function recursively
    return Quicksort(left_side) + [pivot] + Quicksort(right_side)

unordered_list = [4,8,3,1,6,9,36,17,84,14,74]
print(Quicksort(unordered_list))
