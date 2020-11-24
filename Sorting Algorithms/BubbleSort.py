def BubbleSort(seq): 
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):

            # Swap the pair if necessary
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i] 
                
    return seq
    
unordered_list = [4,8,3,1,6,9,36,17,84,14,74]
print(BubbleSort(unordered_list))
