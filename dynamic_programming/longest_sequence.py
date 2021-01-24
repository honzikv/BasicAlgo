# Given a sequence of numbers
# e.g S = (1, 2, 3, 5, 2, 2, 21, 22, 23, 77)
# find a longest increasing subsequence
# eg. (1, 2, 3, 5) or (21, 22, 23, 77)

def longest_inc_subseq(array):
    # To solve this a "table" is created which will contain length of subsequence up until the specific item in array
    # E.g index 2 will specify length of the subsequence which contains item array[2]
    # Additionally, an array that will store the subsequence itself is required - this can be implemented using links
    # where each item of the array contains index to the previous one

    # length of subsequence for each element in "array"
    subseq_lengths = [1 for _ in array]  # initialize to 1, since each element is a subsequence with a length of 1

    # link to previous elements in subsequence
    previous_elements = [-1 for _ in array]  # this can be initialized to whatever, -1 for a non existent element

    if len(array) == 1 or len(array) == 0:
        return array  # return array itself if its empty or containing only one element

    for i in range(1, len(array)):

        # iterate over previous elements
        for j in range(0, i):
            if array[j] < array[i] and subseq_lengths[j] >= subseq_lengths[i]:
                # create a link and increase subsequence length if the jth element is smaller than current element
                # and its subsequence length is greater or equal to current subsequence_length
                subseq_lengths[i] = subseq_lengths[j] + 1
                previous_elements[i] = j

    # Print "table"
    print(array)
    print(subseq_lengths)
    print(previous_elements)

    result = []  # result array which will contain the entire subsequence
    max_index = subseq_lengths.index(max(subseq_lengths))

    items_remaining = subseq_lengths[max_index]
    current_index = max_index

    while items_remaining > 0:
        result.append(array[current_index])  # append item to the result array
        current_index = previous_elements[current_index]  # get index of previous element
        items_remaining -= 1  # decrease amount of remaining items

    result.reverse()  # finally, the list needs to be reversed
    return result


print(longest_inc_subseq([9, 5, 2, 8, 7, 3, 1, 6, 4]))
