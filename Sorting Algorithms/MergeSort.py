# # # # # # # # # #
#   Merge  Sort   #
# # # # # # # # # #

# Average    O(n log n)
# Worst      O(n log n)
# Best       O(n log n)

def MergeSort(seq): 
    if len(seq) > 1: 
        center = len(seq) // 2
        left_side = MergeSort(seq[:center]) 
        right_side = MergeSort(seq[center:]) 
  
        seq = [] 
        while left_side and right_side: 
            seq.append(min(left_side, right_side).pop(0)) 

        seq += left_side + right_side

    return seq 
    
unordered_list = [4,8,3,1,6,9,36,17,84,14,74]
print(MergeSort(unordered_list))