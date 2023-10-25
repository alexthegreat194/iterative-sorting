#!python

from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort

sort = bubble_sort

def test_is_sorted_on_sorted_integers():
    # Positive test cases (examples) with lists of sorted integers
    assert is_sorted([]) is True  # Empty lists are vacuously sorted
    assert is_sorted([3]) is True  # Single item is trivially sorted
    assert is_sorted([3, 4]) is True  # Duplicate items are in order
    assert is_sorted([3, 5]) is True
    assert is_sorted([3, 5, 7]) is True
    

def test_is_sorted_on_unsorted_integers():
    # Negative test cases (counterexamples) with lists of unsorted integers
    assert is_sorted([5, 3]) is False
    assert is_sorted([3, 5, 2]) is False
    assert is_sorted([7, 5, 3]) is False
    

def test_is_sorted_on_sorted_strings():
    # Positive test cases (examples) with lists of sorted strings
    assert is_sorted(['A']) is True  # Single item is trivially sorted
    assert is_sorted(['A', 'B']) is True  # Duplicate items are in order
    assert is_sorted(['A', 'C']) is True
    assert is_sorted(['A', 'B', 'C']) is True
    

def test_is_sorted_on_unsorted_strings():
    # Negative test cases (counterexamples) with lists of unsorted strings
    assert is_sorted(['B', 'A']) is False
    assert is_sorted(['D', 'A', 'C']) is False
    assert is_sorted(['C', 'B', 'A']) is False