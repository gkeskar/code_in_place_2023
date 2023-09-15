import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    # your code here :)
    lines =  get_words_from_file()
    # for line in lines:
    #     print(line)
    while True:
        
        user_input = input("Press Enter to continue or type 'stop', 'exit', 'quit', 'end', 'terminate', or 'finish' to end the loop:...")
        
        if user_input.lower() in ['stop', 'exit', 'quit', 'end', 'terminate', 'finish']:
            break
        else:
            print(random.choice(lines))
        
    
    

if __name__ == '__main__':
    main()
