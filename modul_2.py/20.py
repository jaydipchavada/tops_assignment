def reverse_string(string):
    # Checking if the length of the string is a multiple of 4
    if len(string) % 4 == 0:
        # Reversing the string
        reversed_string = ''.join(reversed(string))
        return reversed_string
    else:
        return string

