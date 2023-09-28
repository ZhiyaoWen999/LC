
# There are three types of edits that can be performed on strings: insert, remove and replace.
# Given two string, write a function to check if they are one edit( or zero edits) away.
# they can perform any operation once
def are_one_edit_different(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s1, s2)


def one_edit_replace(s1, s2):
    edited = False

    for c1, c2 in zip(c1, c2):
        if c1 != c2:
            if edited:
                return False
            edited = False
    return True


def one_edit_insert(s1, s2):
    edited = False

    i, j = 0, 0
    n, m = len(s1), len(s2)
    while i < n and j < m:
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

# combine insert, remove, replace
def one_edit_insert(s1, s2):
    n, m = len(s1), len(s2)

    if abs(n - m > 1):
        return False
    
    s1 = s1 if n < m else s2
    s2 = s2 if n < m else s1

    i, j = 0, 0
    
    edited = False
    while i < n and j < m:
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True

            # on replace
            if n == m :
                i += 1    
        # if match
        else:
            i += 1
        # always move the longer string's index
        j += 1
    return True