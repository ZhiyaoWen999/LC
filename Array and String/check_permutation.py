import Counter
# Check two string is permutation or not.

def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


def check_permutation_pythonic(str1, str2):
    # short-circuit to avoid instantiating a Counter which for big strings
    # may be an expensive operation
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)