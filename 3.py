#!/usr/bin/python3
# Find the Runner-Up Score!

n = 5
# arr = [-100, -99, -92, -3, 4]
arr = map(int, input().split())

x = list(arr)
print(x)

max = -101
max2 = -101

for i in range(0, n):
    if x[i] > max:
        max = x[i]
for i in range(0, n):
    if x[i] > max2 and x[i] < max:
        max2 = x[i]
print(max2)
