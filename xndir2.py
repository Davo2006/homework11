def count_letters(x):
    y = {}
    for i in x:
        y.update({i:x.count(i)})
    return y
print(count_letters("abcdefabc"))