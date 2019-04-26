#!/usr/bin/python3
# String Split and Join
line = "this is a string"

def split_and_join(line):
    a = []
    a = line.split(" ")
    a = "-".join(a)
    return(a)
"""if __name__ == '__main__':
    line = input()"""
result = split_and_join(line)
print(result)
