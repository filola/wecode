def even():
    li = []
    i = 1
    for i in range(51):
        if i == 0:
            continue
        if i % 2 == 1:
            continue
        else:
            li.append(i)
    return li

print(even())