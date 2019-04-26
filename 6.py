#!/usr/bin/python3
# Nested Lists

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


x = students[1]
y = []
max = min = min2 = 0
for i in students:
    if i[1] > max:
        max = i[1]
min2 = min = max
for i in students:
    if i[1] < min:
        min = i[1]
for i in students:
    if i[1] < min2 and i[1] > min:
        min2 = i[1]
for i in students:
    if i[1] == min2:
        y.append(i[0])
y.sort()
for i in y:
    print(i)
print(min)
print(min2)
