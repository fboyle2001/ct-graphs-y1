f = open("names.txt")
classes = []

for line in f:
    names = line.strip().split(",")
    classes.append(names)

matrix = []

for i, c in enumerate(classes):
    class_row = []
    for j, o in enumerate(classes):
        if i == j:
            class_row.append(0)
            continue
        ap = False
        for name in c:
            if name in o:
                class_row.append(1)
                ap = True
                break
        if ap == False:
            class_row.append(0)
    matrix.append(class_row)

for row in matrix:
    print(row)

f.close()
