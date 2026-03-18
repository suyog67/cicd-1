def subtract_letter(word):
    result = ""

    for char in word:
        if char.isalpha():  # Check if it's a letter
            # Convert to uppercase to keep it simple
            char = char.upper()
            
            # If letter is 'A', wrap around to 'Z'
            if char == 'A':
                result += 'Z'
            else:
                # Subtract 1 from ASCII value
                result += chr(ord(char) - 1)
        else:
            # If not a letter, keep it as it is
            result += char

    return result


# Example
word = input("Enter a word: ")
print("After subtraction:", subtract_letter(word))
print("done my sanSui")
print("done my sanSui")
