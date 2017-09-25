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
    options = {'in_file':'', 'out_file':'', 'help_req':False, 'key':None}

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
        elif sys.argv[i] == '-k':
            options['key'] = int(sys.argv[i+1])
            i += 1
        elif sys.argv[i] == '--help':
            options['help_req'] = True
        else:
            print "Unknown option '%s'" % sys.argv[i]
            sys.exit(1)

        i += 1

    return options

def runCaesarCipher( plain_text, key ):
    'Apply the caesar cipher method on the given text'

    # Create the alphabet container and output string
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cipher_text = ''
    
    # Loop over the input text
    for in_char in plain_text:
        
        # For each character find the corresponding position in the alphabet
        pos = alpha_list.index(in_char)
        
        # Apply the shift to the position, handling correctly potential wrap-around
        pos += key
        pos %= 26
        
        # Determine the new character and add it to the output string
        cipher_text += alpha_list[pos]
        
    # Finally (after the loop), return the output string
    return cipher_text
    
# -----------------------------------------------------

cmd_args = parseCommandLine()

if cmd_args['help_req']:
    print 'This program encrypts text with the caesar cipher method'
    print '   -i <file> - Input file to run on, stdin if none given'
    print '   -o <file> - Output file, stdout if none given'
    print '   --help - print this message'
    sys.exit(0)

# We need a key
if not cmd_args['key']:
    cmd_args['key'] = int(raw_input('Key: '))
    
# Take each letter from user input if no input file is given
if cmd_args['in_file'] != '':
    in_string = open(cmd_args['in_file']).read()
else:
    in_string = raw_input('Input: ')
    
out_string = ''
for in_char in in_string:
    #    - In each case, add result to a string variable
    out_string += transformChar( in_char )

# Apply the caesar cipher to this string
out_string = runCaesarCipher( out_string, cmd_args['key'])
    
# if there is no out file given, send to stdout
if cmd_args['out_file'] != '':
    open(cmd_args['out_file'], 'w').write(out_string)    
else:
    print out_string
