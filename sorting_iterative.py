#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(n)
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(1)
    """
    # TODO: Check that all adjacent items are in order, return early if so

    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(1)
    """
    
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(items)-1):
            if items[i+1] < items[i]:
                items[i], items[i+1] = items[i+1], items[i] 
                swapped = True

    return items
    

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(log(n))
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(1)
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    for i in range(len(items)):
        small_index = i
        for j in range(i, len(items)):
            if items[small_index] > items[j]:
                small_index = j
        items[small_index], items[i] = items[i], items[small_index]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    Time: O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?
    Memory: O(1)
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    for i in range(len(items)):
        for j in range(i, 0):
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]
            else:
                break
    return items

sorted_list = [1, 2, 10, 4, 5]
print(is_sorted(sorted_list))

list = [65,	69,	94,	11,	74, 94,	79,	13,	83,	71]

listBubble = bubble_sort(list)
print("Bubble Sort: ", listBubble, is_sorted(listBubble))

listSelection = selection_sort(list)
print("Selection Sort: ", listBubble, is_sorted(listBubble))

listInsertion = insertion_sort(list)
print("Insertion Sort", listInsertion, is_sorted(listInsertion))