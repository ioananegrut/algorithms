# 1. Retrieve the longest sequence, the elements of which add up to N

def test_max_sequence_of_sum():
    assert(get_max_sequence_of_sum([100,5,1,1,-5,3,8,0,-203,198], of_sum=5) == [[5,1,1,-5,3]])
    assert(get_max_sequence_of_sum([2,3,8,100,-50,1,4], of_sum=5) == [[2,3], [1,4]])
    assert(get_max_sequence_of_sum([3], of_sum=5)==[[]])
    assert(get_max_sequence_of_sum([5], of_sum=5)==[[5]])
    assert(get_max_sequence_of_sum([], of_sum=5)==[[]])

def get_max_sequence_of_sum(ls: list, of_sum: int)->list:
    """
        Get the maximum length sequence which adds up to a given number.
    """
    condition_sum = of_sum
    max_elem = 0
    sequences = [[]] # store the results

    for i in range(len(ls)):
        # Start with the longest possible sequence (length of the list)
        # and gradually decrease the length by 1 step
        seq_size = len(ls) - i
        nr_subseq = i+1

        # Extract each subsequence of a certain size and calculate the sum
        for j in range(nr_subseq):
            candidate_seq = ls[j:j+seq_size]
            sub_seq_sum = sum(candidate_seq)

            validCondition = sub_seq_sum == condition_sum
            if validCondition == False:
                continue

            # if the condition is met, update
            num_elem = len(candidate_seq)
            if num_elem > max_elem:
                sequences = [[]]
                sequences.append(candidate_seq)
                max_elem = num_elem

            elif num_elem == max_elem:
                sequences.append(candidate_seq)

        # Stop once the longest sequences were found and don't continue beyond
        if len(sequences) > 1:
            return sequences[1:]

    return sequences

## run the TESTS 
test_max_sequence_of_sum()

###
if __name__=="__main__":
    ls = [3,3,3,-4,3,2,4,65,4,66,66,67,68,1,0,0,0,0,0,10,1,69,70,70,70, 230]
    get_max_sequence_of_sum(ls, of_sum=5)
