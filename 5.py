#!/usr/bin/python3
# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

x = 0
for i in range(0, 3):
#    print(student_marks[query_name][i])
    x += student_marks[query_name][i]
print('%3.2f' %(x / 3))
# print(n)
# print(student_marks)
# print(query_name)
# print (student_marks[query_name])
