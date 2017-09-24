# Take each letter from user input and in each case:
in_string = raw_input('Input: ')
out_string = ''
i = 0

while i < len(in_string):
    #    - Convert to upper case
    new_str = in_string[i].upper()
    i += 1
    
    #    - Change numbers to words
    if new_str == '0':
        new_str = 'ZERO'
    elif new_str == '1':
        new_str = 'ONE'
    elif new_str == '2':
        new_str = 'TWO'
    elif new_str == '3':
        new_str = 'THREE'
    elif new_str == '4':
        new_str = 'FOUR'
    elif new_str == '5':
        new_str = 'FIVE'
    elif new_str == '6':
        new_str = 'SIX'
    elif new_str == '7':
        new_str = 'SEVEN'
    elif new_str == '8':
        new_str = 'EIGHT'
    elif new_str == '9':
        new_str = 'NINE'
    
    #    - Ignore any other (non-alpha) characters
    if not new_str.isalpha():
        continue

    #    - In each case, add result to a string variable
    out_string += new_str

# print out the new string
print out_string
