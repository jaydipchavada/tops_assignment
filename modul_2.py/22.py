def insert_string_middle(string, string_to_insert):
    middle_index = len(string) // 2
    new_string = string[:middle_index] + string_to_insert + string[middle_index:]
    return new_string
