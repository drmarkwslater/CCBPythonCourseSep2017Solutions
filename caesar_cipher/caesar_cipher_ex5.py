# Take each letter from user input and in each case:
in_string = raw_input('Input: ')
out_string = ''
num2word_dict = {'0':'ZERO', '1':'ONE', '2':'TWO', '3':'THREE', '4':'FOUR', '5':'FIVE', '6':'SIX', '7':'SEVEN', '8':'EIGHT', '9':'NINE' }

for in_char in in_string:
    #    - Convert to upper case
    new_str = in_char.upper()
    
    #    - Change numbers to words
    if new_str in num2word_dict.keys():
        new_str = num2word_dict[new_str]
    
    #    - Ignore any other (non-alpha) characters
    if not new_str.isalpha():
        continue

    #    - In each case, add result to a string variable
    out_string += new_str

# print out the new string
print out_string
