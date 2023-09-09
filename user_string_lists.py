"""
Working on Task 4 

"""

# imports first
import random

#set up logging

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Creating lists. My domain is Biology (plants), so i am creating lists related to tomatoes farming.

tomatoes_varieties = ["cherry", "roma", "vine", "heirloom", "cocktail", "red beefsteak"]

total_outcomes = ["profit", "loss", "inbetween"]

field_location = ["NC", "MO", "NY", "KS", "IA", "KY", "TN", "TX", "UT"]

color_list = ["red", "pink", "yellow", "red", "red"]

tomatoes_size = ["large", "medium", "small", "large", "medium"]

# reusable functions next


# Task 4 ####################################################
# Use the built-in functions: len(), set(), and zip() 
# to combine 2 or more lists into tuples.



#Making new list with set
def new_list_set():
    lst_new = tuple(set(field_location))
    logger.info(f"new tuple using set(): {lst_new}")


#combine two lists using zip
def combine_twolists_zip():
    updated_tuple = tuple(zip(tomatoes_varieties, tomatoes_size))
    logger.info(f"combined list into tuple: {updated_tuple}")
    logger.info("-----------------------------------------------")#break for readability


# Use random.choice() to pick a random value from one of your lists.
# Customize the sentence generator to create random sentences about your domain. 

def random_choice():
    logger.info(f"Random value selected from variety: {tomatoes_varieties}")
    random_value = (random.choice(tomatoes_varieties))
    logger.info(f"Random variety is : {random_value}")


def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")
    sentence = (
        f"The {random.choice(tomatoes_varieties)} tomatoes is {random.choice(color_list)} while harvesting !!"
        f" There is {random.choice(total_outcomes)}  in {random.choice(tomatoes_varieties)} farming !")
    
    logger.info(f"Random sentence is {sentence}")


# Choose one of the text data files in the repo - or add another related your your domain.
# Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
# Sort the list. 
# Use len() to get the length display it to the console.
# How good is your list? 


def process_text_zen_of_python():
    logger.info(f"Calling process_text_zen_of_python")

    with open("text_zen_of_python.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        list_words_sorted = sorted(list_words)
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words and sort
        word_count = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"The sorted lis of words is: {list_words_sorted}")
        logger.info(f"There are {word_count} words in the file.")

        # Print the count and list of unique words
        unique_word_count = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_count} unique words in the file.")



def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())
   

# call functions and execute code
# use if __name__ == "__main__":


if __name__ == "__main__":
    logger.info("Calling functions from main block")
    
    new_list_set()
    combine_twolists_zip()
    random_choice()
    create_random_sentence()
    process_text_zen_of_python()
    show_log()
