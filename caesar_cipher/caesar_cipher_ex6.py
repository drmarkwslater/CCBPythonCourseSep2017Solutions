# loop over the command line arguments and process them
import sys

input_file = ''
output_file = ''
i = 1
while i < len(sys.argv):
    
    # Look for the various cmd line options
    if sys.argv[i] == '-i':
        input_file = sys.argv[i+1]
        i += 1
    elif sys.argv[i] == '-o':
        output_file = sys.argv[i+1]
        i += 1
    elif sys.argv[i] == '--help':
        print 'This program encrypts text with the caesar cipher method'
        print '   -i <file> - Input file to run on, stdin if none given'
        print '   -o <file> - Output file, stdout if none given'
        print '   --help - print this message'
        sys.exit(0)
    else:
        print "Unknown option '%s'" % sys.argv[i]
        sys.exit(1)

    i += 1
    
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
