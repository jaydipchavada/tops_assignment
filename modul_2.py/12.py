string = input("Enter a string: ")
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequency:")
for char, count in freq.items():
    print(f"{char}: {count}")
