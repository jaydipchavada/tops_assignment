def not_poor(string):
    # Finding the index of "not" and "poor" in the string
    not_index = string.find('not')
    poor_index = string.find('poor')
    
    # Checking if "not" appears before "poor", and replacing it with "good"
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return string[:not_index] + 'good' + string[poor_index+4:]
    else:
        return string

