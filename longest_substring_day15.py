def find_longest_substring_length(input_string):
    max_length = 0
    start = 0
    end = 0
    char_set = set()

    while end < len(input_string):
        if input_string[end] not in char_set:
            char_set.add(input_string[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            char_set.remove(input_string[start])
            start += 1

    return max_length

# Test cases
print(find_longest_substring_length("abcabcbb"))  # Output: 3
print(find_longest_substring_length("bbbbb"))     # Output: 1
print(find_longest_substring_length("pwwkew"))    # Output: 3
print(find_longest_substring_length("abcdefgh"))  # Output: 8
print(find_longest_substring_length("a"))         # Output: 1
