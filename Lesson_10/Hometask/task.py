# 1 вариант
def dedupe_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

# 2 вариант
# this one uses sets
def dedupe_v2(x):
    return list(set(x))


a = [1, 2, 3, 4, 3, 2, 1]
print(a)
print(dedupe_v1(a))
print(dedupe_v2(a))

# 3 вариант
x = [1, 2, 3, 4, 3, 2, 1]
seen = set()

result = [i for i in x if not (i in seen or seen.add(i))]
print(result)  # [1, 2, 3, 4]
