# @filename: [m1builtins]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources: https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
# https://www.dummies.com/programming/python/how-to-use-lambda-functions-in-python/

builtInFuncs = dir(__builtins__)

#sorts the list using lambda expression:
# usage: 
#   lambda <arguments> : <expression or formula/conditions to met>
# 
# example: (lambda x: x.startswith("__") or x[0].islower())

builtInFuncs = sorted(builtInFuncs, key = (lambda x: x.startswith("__") or x[0].islower()), reverse=True)
#### question: why is the list reverted??

strBuiltIn = ""
for f in builtInFuncs:
    strSize = len(strBuiltIn)
    wordSize = len(f)
    
    if (strSize >= 40) or (strSize + wordSize + 1) >= 40:
        print(strBuiltIn[:40])
        strBuiltIn = ""
    else:
        strBuiltIn += f + " "