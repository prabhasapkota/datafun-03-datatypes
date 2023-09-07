"""
Created user_numeric_lists.py as Task for Module 3. Here, my domian is (Botany)leafnumbers in cucumber plabts.

"""

# import some standard modules
import math
import statistics


# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [3,5,8,9,2,12,14,19,2,8,8,10,9,9,7,11,15,19,7,7,7,11,3,3,1,16,11,4,4,8,10]

listx = [1,2,3,4,5,6,7,8,9,10]
listy = [1,2,2,3,5,4,4,6,4,5]

# TODO: define some custom functions
def measures_of_central_tendency():
    logger.info(f"Points scored: {list1}")
    logger.info(f"Range to 10: {listx}")

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"Leafnumbers mean is: {mean:.2f}")
    logger.info(f"Leafrnumbers median is: {median}")
    logger.info(f"Leafnumbers mode is : {mode}")

    logger.info(f"Leafnumbers standard deviation is: {stdev:.2f}")
    logger.info(f"Leafnumbers variance is: {variance:.2f}")


def correlation_function():
    logger.info(f"Listx:{listx}")
    logger.info(f"Listy:{listy}")
    
    correlationxy = statistics.correlation(listx, listy)
    slope, intercept = statistics.linear_regression(listx, listy)

    x_max = max(listx)
    newx = 15
    newy = slope * newx + intercept

    logger.info(f"correlation between x and y is: {correlationxy}")
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")
    logger.info(f"We predict that when x = {newx}, y will be about {newy}")


def list_info():
    logger.info(f"General information for the following list: {list1}")

    min_value = min(list1)
    max_value = max(list1)
    length = len(list1)
    total = sum(list1)
    average = (total/length)
    set_list1 = set(list1)
    sorted_values = sorted(list1)
    sorted_reversed = sorted(list1, reverse=True)

    logger.info(f"The min of list1 is {min_value}")
    logger.info(f"The msx of list1 is {max_value}")
    logger.info(f"The length of list1 is {length}")
    logger.info(f"The total of list1 is {total}")
    logger.info(f"The average of list 1 is {average:.2f}")
    logger.info(f"The set of list1 is {set_list1}")
    logger.info(f"List1 sorted is {sorted_values}")
    logger.info(f"List1 sorted and reversed is {sorted_reversed}")


def list_transformation():
    logger.info(f"General transformations of list1: {list1}")

    high_leafnumbers = list(filter(lambda x: x >=12, list1))
    leafnumbers_cubed = list(map(math.cbrt, list1))
    list_value = 5
    volume = (list_value**3)
    
    logger.info(f"The leafnumbers that are greater than or equal to 12 are: {high_leafnumbers}")
    logger.info(f"The leafnumbers cube rooted are: {leafnumbers_cubed}")
    logger.info(f"The volume of cube with side equal to 5 is {volume}") 


def list_transformation_comprehensions():
    logger.info(f"General list transformations using comprehensions of list1: {list1}")

    Leafnumbers_above10 = [x for x in list1 if x > 10]
    leafnumbers_trippled = [x*3 for x in list1]
    leafnumbers_sqrt = [math.sqrt(x) for x in list1]

    logger.info(f"The plants with leafnumbers that are greater than 10 are: {Leafnumbers_above10}")
    logger.info(f"The leafnumbers trippled are: {leafnumbers_trippled}")
    logger.info(f"leafnumbers square rooted are: {leafnumbers_sqrt}")

def show_log():
     with open(logname, "r") as file_wrapper:
         print(file_wrapper.read())






# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info("CALLING functions")
    logger.info("CALLING measures_of_central_tendency")
    measures_of_central_tendency()

    logger.info("***==============================================***")
    logger.info("CALLING correlation_function")
    correlation_function()

    logger.info("***==============================================***")
    logger.info("CALLING list_info")
    list_info()

    logger.info("***==============================================***")
    logger.info("CALLING list_transformation")
    list_transformation()

    logger.info("***==============================================***")
    logger.info("CALLING list_transformation_comprehensions")
    list_transformation_comprehensions()

    show_log()

   



