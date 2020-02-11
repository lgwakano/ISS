# @filename: [m1dir]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources 
# https://www.tutorialspoint.com/python/string_startswith.htm 
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# https://stackoverflow.com/questions/19103052/python-string-formatting-columns-in-line

index = 0
for x in dir(str):
    if not x.startswith("__"):
        if (index % 5) == 0:
            print("{0:<20}".format(""))
            
        #print("{0:<20}".format(x), end = " ")
        print("{0:<15}".format(x), end = " ")
        index = index + 1