"""
8) Write a python program to find the longest words ?
=>

"""
def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    
    for i in words:
        if len(i) == max_len:
            maxword = i
    return maxword

print(longest_word('simple.txt'))