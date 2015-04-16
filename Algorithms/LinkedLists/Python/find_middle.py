#!/usr/bin/env python

def find_middle(l):
    """ Finds the middle element of a linked list.

    Args:
        l (LinkedList): the linked list to search

    Returns:
        The value of the middle node in the linked list.
        If the linked list is empty returns None.
        If the linked list is even, returns the left middle element.
    """
    if len(l) == 0:
        return None

    fast_ptr = l.top.next_
    slow_ptr = l.top.next_
    print "fast:", fast_ptr, "next_", fast_ptr.next_
    print "slow:", slow_ptr
    while fast_ptr.next_ is not None:
        fast_ptr = fast_ptr.next_
        if fast_ptr.next_ == None:
            break
        fast_ptr = fast_ptr.next_
        slow_ptr = slow_ptr.next_

    return slow_ptr.value
