data = open("data")
d = data.read()

def rearrange_string(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2:] + s[:length//2]
    else:
        return s[(length//2)+1:] + s[0:(length//2)+1]

def is_nonrepeated(a:str):
    l = 0
    s = 0
    for i in a:
        l = a.count(i)
        if l == 1:
            s += 1
    if s == len(a):
        return True
    else: return False
    
ls = d.split()

for i in ls:
    if is_nonrepeated(i):
        print(rearrange_string(i))