#!python
from sorting_iterative import is_sorted, bubble_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(n)
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(n^2)
    """
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    max = 0
    for num in numbers:
        if num > max:
            max = num

    counting_list = [0] * max
    for i in range(len(numbers)):
        counting_list[numbers[i]-1] += 1
        
    list_index = 0
    for count_index in range(len(counting_list)):
        while counting_list[count_index] > 0:
            numbers[list_index] = count_index
            list_index += 1
            counting_list[count_index] -= 1

    return numbers
        


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(n)
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(n)
    """
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # percent = num/max
    # bucket = percent/bucket_amount

    max = 0
    for num in numbers:
        if num > max:
            max = num

    buckets = []
    for i in range(num_buckets):
        buckets.append([])

    for num in numbers:
        percent = float(num)/float(max)
        bucket = int(percent*float(num_buckets))
        # print(percent, bucket)
        buckets[bucket-1].append(num)

    # print(buckets)

    for i, b in enumerate(buckets):
        # print(b)
        buckets[i] = bubble_sort(b)
        # print(bucket[i])

    list_index = 0
    for b in buckets:
        for v in b:
            numbers[list_index] = v
            list_index += 1
    
    return numbers    


# list = [65,	69,	94,	11,	74, 94,	79,	13,	83,	71]

# count_list = counting_sort(list)
# print("Counting Sort:", count_list, is_sorted(count_list))

# bucket_list = bucket_sort(list)
# print("Bucket Sort:", bucket_list, is_sorted(bucket_list))