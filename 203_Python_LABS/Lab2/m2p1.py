# @filename: [m2p1]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources https://docs.python.org/2/howto/argparse.html

from random import randint, choice
from file_manager import FileManager
import argparse

ALPHA_OFFSET = None
non_repeating_seq = set()

"""
    Generates only alphanumeric basec on ASCII
    ASCII:
        Char => Dec
        0-9  => 48-57
        A-Z  => 65-90 (A-F => 65-70)
        a-z  => 97-122 (a-f => 97-102)
"""
def generate_random_alpha(size=12):
    alpha = ''
    for _ in range(size): #how many integers
        r = choice([(48,57),(65,70), (97, 102)]) #will select start and end included
        alpha += chr(randint(*r))
    return alpha


"""
    Define pattern for the offset
    Arguments:
        alpha: the 1st alphanumeric generated or given
"""
def define_pattern(alpha):
    global ALPHA_OFFSET
    if ALPHA_OFFSET != None:
        print("OFFSET already defined!")
    else:
        offset_size = get_offset_size(alpha)
        ALPHA_OFFSET = alpha[:offset_size]


def get_offset_size(alpha):
    offset_size = len(alpha) // 2 #pattern
    return offset_size


def get_first_alpha(user_input):
    alpha = user_input
    if alpha.isdigit():
        size = int(alpha)
        alpha = generate_random_alpha(size)
       
    return alpha


def write_currentbuffer(alpha):
    alpha += "\n"
    if not FileManager.file_exists():
        FileManager.write_on_file(alpha)
    else:
        FileManager.write_on_file(alpha, "a")


def generate_next_seq(pattern, alpha, alpha_length=None):
    global non_repeating_seq

    if alpha_length == None:
        alpha_length = len(alpha) - get_offset_size(alpha)
    
    next_alpha = generate_random_alpha(alpha_length)
    
    return next_alpha


def is_repeated(next_alpha):
    if len(non_repeating_seq) > 0:
        if next_alpha in non_repeating_seq:
            return True
    return False

def automate_search_pattern(user_input):
    alpha = get_first_alpha(user_input) #generate first alphanumeric based on user input
    alpha_size = len(alpha)

    define_pattern(alpha) #set OFFSET

    write_currentbuffer(ALPHA_OFFSET) #write the pattern on file

    pattern = FileManager.read_file()
    pattern = pattern.strip()

    keep_search = True
    while keep_search:
        next_seq = generate_next_seq(pattern, alpha, alpha_size) #does not include offset
        print("next seq: {} | {}".format(str(next_seq), pattern))

        if next_seq.startswith(pattern):
            keep_search = False
            print("\n--------- \nfound: " + next_seq)

    print("OFFSET: " + str(ALPHA_OFFSET)) #check offset
    FileManager.delete_file()


def set_random_alphanumeric():
    print("-" * 80)
    user_input = input("Let's generate an alphanumeric. " +
    "Please type either a string or a string length: \n>> ")

    alpha = get_first_alpha(user_input) #generate first alphanumeric based on user input
    write_currentbuffer(alpha) #write the alpha to the file
    print("\nAlphanumeric is: " + str(alpha)) #check offset
    print("please run the program again to check the offset pattern")

def check_pattern():
    print("-" * 40)
    user_input = input("Please provide the pattern to be checked:\n>> ")
    stored_string = FileManager.read_file()
    stored_string = stored_string.strip()

    print(f"\nThe stored string is: {stored_string}")
    print(f"You provided this pattern: {user_input}")

    if user_input in stored_string:
        splited = stored_string.split(user_input)

        offset_len = len(splited[0]) + 1

        print("*" * 40)
        print(f"The pattern match the stored string!")
        print(f"The offset position is: {offset_len}!")
        print("*" * 40)
        FileManager.delete_file()
    else:
        print("The pattern does not match!")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--auto", help="automate search. Usage: --auto 1")
        args = parser.parse_args()
        
        if args.auto:
            user_input = input("Please type either a string or a string length: \n")        
            automate_search_pattern(user_input)
        else:
            if not FileManager.file_exists():
                set_random_alphanumeric()
            else:
                check_pattern()

    except KeyboardInterrupt:
        print('Interrupted')
        if FileManager.file_exists():
            FileManager.delete_file()