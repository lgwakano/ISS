# @filename: [m1p3]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources

import keyword

# for key in keyword.kwlist:
#     print(key)

keywordList = keyword.kwlist 
# print(sorted(keywordList))
# print(keywordList.sort())


# sort the list

keywordList.sort(key = str.lower)

# display the sorted keywordList
print("The sorted keywordList are:")
for word in keywordList:
   print(word)



