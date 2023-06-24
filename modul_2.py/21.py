def get_string(string):
    # Check if the length of the string is less than 2
    if len(string) < 2:
        return ''
    else:
        # Get the first two and last two characters of the string and concatenate them
        new_string = string[:2] + string[-2:]
        return new_string

