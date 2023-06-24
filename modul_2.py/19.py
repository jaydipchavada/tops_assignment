def find_longest_word(words):
    # Initializing the longest length to be 0
    longest_length = 0
    
    # Looping through all the words in the list
    for word in words:
        # If the length of the current word is greater than the longest length so far, update the longest length
        if len(word) > longest_length:
            longest_length = len(word)
    
    # Return the longest length
    return longest_length

