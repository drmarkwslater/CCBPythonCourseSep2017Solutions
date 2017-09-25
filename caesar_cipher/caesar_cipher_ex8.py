# Import external modules
import sys

def transformChar( in_char ):
    'Take the input char, apply transliteration and return'
    
    num2word_dict = {'0':'ZERO', '1':'ONE', '2':'TWO', '3':'THREE', '4':'FOUR', '5':'FIVE', '6':'SIX', '7':'SEVEN', '8':'EIGHT', '9':'NINE' }
    
    #    - Convert to upper case
    new_str = in_char.upper()
    
    #    - Change numbers to words
    if new_str in num2word_dict.keys():
        new_str = num2word_dict[new_str]
    
    #    - Ignore any other (non-alpha) characters
    if not new_str.isalpha():
        return ''

    return new_str

def parseCommandLine():
    'Process any command line options'
    options = {'in_file':'', 'out_file':'', 'help_req':False}

    # loop over the command line arguments and process them
    i = 1
    while i < len(sys.argv):
    
        # Look for the various cmd line options
        if sys.argv[i] == '-i':
            options['in_file'] = sys.argv[i+1]
            i += 1
        elif sys.argv[i] == '-o':
            options['out_file'] = sys.argv[i+1]
            i += 1
        elif sys.argv[i] == '--help':
            options['help_req'] = True
        else:
            print "Unknown option '%s'" % sys.argv[i]
            sys.exit(1)

        i += 1

    return options


# -----------------------------------------------------

cmd_args = parseCommandLine()

if cmd_args['help_req']:
    print 'This program encrypts text with the caesar cipher method'
    print '   -i <file> - Input file to run on, stdin if none given'
    print '   -o <file> - Output file, stdout if none given'
    print '   --help - print this message'
    sys.exit(0)
        
# Take each letter from user input and in each case:
in_string = raw_input('Input: ')
out_string = ''

for in_char in in_string:
    #    - In each case, add result to a string variable
    out_string += transformChar( in_char )


# print out the new string
print out_string
