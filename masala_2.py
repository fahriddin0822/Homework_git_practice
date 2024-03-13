user_input = input(">>> ")
def rearrange_string(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2:] + s[:length//2]
    else:
        return s[(length//2)+1:] + s[0:(length//2)+1]
print(rearrange_string(user_input))
