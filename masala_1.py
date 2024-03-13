user_input = input(">>>  ")


def longest_substring(s):
    longest = ""
    current = ""

    for char in s:
        if char in current:
            if len(current) > len(longest):
                longest = current
            current = current[current.index(char) + 1:]
        current += char
        
    if len(current) > len(longest):
        longest = current

    return longest

print(longest_substring(user_input))