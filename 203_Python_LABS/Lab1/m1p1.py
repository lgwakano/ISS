# @filename: [m1p1]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources

import time  

localtime = time.asctime(time.localtime(time.time()))
email = "luizgustavo.wakano@edu.sait.ca" 
first = "Luiz"
last = "Who"

print("{} {} {} {}".format(localtime, email, first, last))