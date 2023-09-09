"""
Task 5: Tuples and dictionaries

"""



# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)


# Create some tuples
tuple_flowertype = ("marigold", "sunflower", "lily", "rose", "lavender", "daisy")
tuple_field_location = ("North Carolina", "Missouri", "Texas", "New York", "Utah", "Maryland")
tuple_color = ("yellow", "red", "purple", "orange", "white", "brown")

logger.info(f"tuple_flowertype = {tuple_flowertype}")
logger.info(f"tuple_field_location = {tuple_field_location}")
logger.info(f"tuple_color = {tuple_color}")
logger.info("****=================================****")

    

# Create two sets
#presenting datasets : yield of flowers (lb) at diiferent time of the year.



yield_at_summer = {10, 8, 14, 16, 20, 11}
yield_at_winter = {5, 6, 7, 4, 8, 9}

logger.info(f"yield_at_summer = {yield_at_summer}")
logger.info(f"yield_at_winter = {yield_at_winter}")


#set union
total_yield =  yield_at_summer | yield_at_winter
logger.info(f"union of two sets: {total_yield}")

#set intersection
yield_set_intersection = yield_at_summer & yield_at_winter
logger.info(f"intersection of two sets: {yield_set_intersection}")
logger.info("****=================================****")

#Use a dictionary to create key-value pairs of each word and its count from a file.
# yield@1b 

rose_dict = {"fragnance_level": "high", "yield": 14 , "bloom_period": "4weeks"}
sunflower_dict = {"fragnance_level": "low", "result": 11 , "bloom_period": "3weeks"}

logger.info(f"rose_dict = {rose_dict}")
logger.info(f"sunflower_dict = {sunflower_dict}")
    
logger.info("") 


with open("text_names_in.txt") as file_object:
 word_list = file_object.read().split()
      

# loop to count words
word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

logger.info(f"Given text_names_in.txt, the word_count_dict {word_counts_dict}")
logger.info("****=================================****")

# comprehension to count words

word_count_dict2 = {word: word_list.count(word) for word in word_list}

logger.info(f"Word count comprehension result is {word_count_dict2}")

def show_log():
      with open(logname, "r") as file_wrapper:
          print(file_wrapper.read())

# -------------------------------------------------------------
# Call some functions and execute code!

if __name__=="__main__":
     
     logger.info("CALLING functions in user_tuple_etc.py")
     logger.info("****=================================****")
      



     show_log()

    
