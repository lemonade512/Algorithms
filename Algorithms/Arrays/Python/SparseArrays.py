#!/usr/bin/python

DEFAULT = 0

class ArrayRow:

    def __init__(self):
        self.row_number = -1
        self.next_row = None
        self.row_sentinel = None

    def __repr__(self):
        result = "Row #" + str(self.row_number) + ":: "
        top = self.row_sentinel
        if top.next_entry != None:
            top = top.next_entry
        else:
            print "Row Empty"
            return

        while top != None:
            result += str(top) + " "
            top = top.next_entry
        return result

class ArrayEntry:

    def __init__(self, value = None):
        self.column_number = -1
        self.value = value
        self.next_entry = None

    def __repr__(self):
        return "(" + str(self.column_number) + ", " + str(self.value) + ")"

def print_sparse_array(sentinel):
    row_sentinel = sentinel
    if row_sentinel.next_row != None:
        row_sentinel = row_sentinel.next_row
    else:
        print "Array Empty"
        return

    while row_sentinel != None:
        print row_sentinel
        row_sentinel = row_sentinel.next_row

def find_row_before(row, array_row_sentinel):
    array_row = array_row_sentinel
    while (array_row.next_row != None and
           array_row.next_row.row_number < row):
        array_row = array_row.next_row

    return array_row

def find_column_before(column, row_sentinel):
    array_entry = row_sentinel
    while (array_entry.next_entry != None and
           array_entry.next_entry.column_number < column):
        array_entry = array_entry.next_entry

    return array_entry

def get_value(row, col, array_sentinel):
    array_row = find_row_before(row, array_sentinel)
    array_row = array_row.next_row
    if array_row == None:
        return DEFAULT
    if array_row.row_number > row:
        return DEFAULT

    array_entry = find_column_before(col, array_row.row_sentinel)
    array_entry = array_entry.next_entry
    if array_entry == None:
        return DEFAULT
    if array_entry.column_number > col:
        return DEFAULT
    return array_entry.value

def set_value(row, col, value, array_sentinel):
    if value == DEFAULT:
        delete_entry(row, col, array_sentinel)
        return

    array_row = find_row_before(row, array_sentinel)

    if (array_row.next_row == None or
        array_row.next_row.row_number > row):
        new_row = ArrayRow()
        new_entry.row_number = row
        new_row.next_row = array_row.next_row
        array_row.next_row = new_row

        sentinel_entry = ArrayEntry()
        new_row.row_sentinel = sentinel_entry

    array_row = array_row.next_row
    array_entry = find_column_before(col, array_row.row_sentinel)

    if (array_entry.next_entry == None or
        array_entry.next_entry.column_number > col):
        new_entry = ArrayEntry()
        new_entry.column_number = col
        new_entry.next_entry = array_entry.next_entry
        array_entry.next_entry = new_entry

    array_entry = array_entry.next_entry
    array_entry.value = value

def delete_entry(row, col, array_sentinel):
    array_row = find_row_before(row, array_sentinel)

    if (array_row.next_row == None or
        array_row.next_row.row_number > row):
        return

    target_row = array_row.next_row
    array_entry = find_column_before(col, target_row.row_sentinel)

    if (array_entry.next_entry == None or
        array_entry.next_entry.column_number > col):
        return

    array_entry.next_entry = array_entry.next_entry.next_entry

    if target_row.row_sentinel.next_entry != None:
        return

    array_row.next_row = array_row.next_row.next_row

def make_test_array():
    row_sentinel = ArrayRow()
    r0 = ArrayRow()
    r1 = ArrayRow()
    r2 = ArrayRow()
    r0c0 = ArrayEntry()
    r0c1 = ArrayEntry()
    r1c0 = ArrayEntry()
    r1c1 = ArrayEntry()
    r1c2 = ArrayEntry()
    r2c0 = ArrayEntry()

    row_sentinel.next_row = r0

    r0.row_number = 0
    r0.next_row = r1
    r0_sentinel = ArrayEntry()
    r0_sentinel.next_entry = r0c0
    r0.row_sentinel = r0_sentinel
    r0c0.column_number = 4
    r0c0.value = 5
    r0c0.next_entry = r0c1
    r0c1.column_number = 7
    r0c1.value = 3

    r1.row_number = 3
    r1.next_row = r2
    r1_sentinel = ArrayEntry()
    r1_sentinel.next_entry = r1c0
    r1.row_sentinel = r1_sentinel
    r1c0.column_number = 0
    r1c0.value = 1
    r1c0.next_entry = r1c1
    r1c1.column_number = 1
    r1c1.value = 6
    r1c1.next_entry = r1c2
    r1c2.column_number = 4
    r1c2.value = 5

    r2.row_number = 4
    r2_sentinel = ArrayEntry()
    r2_sentinel.next_entry = r2c0
    r2.row_sentinel = r2_sentinel
    r2c0.column_number = 0
    r2c0.value = 15

    return row_sentinel

if __name__ == "__main__":
    test_array_sentinel = make_test_array()
    print "Test Array"
    print "-----------------------------------------"
    print_sparse_array(test_array_sentinel)
    print "-----------------------------------------"
    print "\nFind Before methods"
    print "-----------------------------------------"
    print "Row before 2: " + str(find_row_before(2, test_array_sentinel))
    print "Row before 4: " + str(find_row_before(4, test_array_sentinel))
    row = find_row_before(1, test_array_sentinel)
    print "Column before 7 in Row #0: " + \
           str(find_column_before(7, row.row_sentinel))
    print "-----------------------------------------"
    print "\nGet and Set methods"
    print "-----------------------------------------"
    print "Get (0,4): " + str(get_value(0,4, test_array_sentinel))
    print "Get (0,5): " + str(get_value(0,5, test_array_sentinel))
    print "Get (3,1): " + str(get_value(3,1, test_array_sentinel))
    print "Setting (0,8) to 5"
    set_value(0,8, 5, test_array_sentinel)
    print "Get (0,8): " + str(get_value(0,8, test_array_sentinel))
    print "Setting (0,5) to 3"
    set_value(0,5, 3, test_array_sentinel)
    print "Get (0,5): " + str(get_value(0,5, test_array_sentinel))
    print "Setting (3,1) to 4"
    set_value(3,1, 4, test_array_sentinel)
    print "Get (3,1): " + str(get_value(3,1, test_array_sentinel))
    print "-----------------------------------------"
    print "\nDelete Method"
    print "-----------------------------------------"
    print "Deleting (0,5)"
    delete_entry(0,5, test_array_sentinel)
    print "Deleting (4,0)"
    delete_entry(4,0, test_array_sentinel)
    print "Setting (0,5) to 0"
    set_value(0,5, 0, test_array_sentinel)
    print_sparse_array(test_array_sentinel)
