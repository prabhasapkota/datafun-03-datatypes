"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")
        
    # read from file and get a list of words

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    #logger.info(f"List of words from play 1: {wordlist1}")


    # read from file and get a list of words

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    #logger.info(f"List of words from play 2: {wordlist2}")


    wordset1 = set(wordlist1)  
    wordset2 = set(wordlist2)  

    # initialize a variable maxlen = 10
    maxlen = 10  

    # use a list comprension to get a list of words longer than 10
    # for word in wordset1
    # That is:
    # in a list (e.g. square brackets)
    # say "[Give me word (for each word in wordset1)
    #      if len(word) is greater than maxlen]"
    # then convert the list to a set to we can take the intersection
    # hint: use set()
    # name them longwordset1 and longwordset2

    longwordlist1 = [word for word in wordset1 if len(word) > maxlen]
    longwordlist2 = [word for word in wordset2 if len(word) > maxlen]

    longwordset1 = set(longwordlist1)
    longwordset2 = set(longwordlist2)
      
 

    # find the intersection of the two sets
    # that is, the words in both longwordset1 1 & longwordset2
    # name this variable longwords
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    # using logger instead of print


    logger.info(f"{len(longwordset1) = }")
    logger.info(f"{len(longwordset2) = }")
    logger.info(f"{len(longwords) = }")
    logger.info("=====================================================")
    logger.info("=====================================================")
    logger.info("doctest.testmod results")
    logger.info("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    logger.info("TESTING DONE")

    

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

if __name__ == "__main__":
    def compare():
        logger.info("Compare the text lists")

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    #logger.info(f"List of words from play 1: {wordlist1}")

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  

    wordset1 = set(wordlist1) 
    wordset2 = set(wordlist2)  

    maxlen = 10  

    longwordlist1 = [word for word in wordset1 if len(word) > maxlen]
    longwordlist2 = [word for word in wordset2 if len(word) > maxlen]

    longwordset1 = set(longwordlist1)  
    longwordset2 = set(longwordlist2)

    longwords = longwordset1 & longwordset2




    logger.info("Calling functions from main block")

    compare_two_plays()

    

    logger.info("Complete the code to compare two plays.")
    show_log()

