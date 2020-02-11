# @filename: [m1p4]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# https://stackoverflow.com/questions/10037115/comparing-a-float-and-an-int-in-python

marks = [79,66,50,45,45,55,68,88,55,46,54,76,98,77,93,
45,87,42,58,81,48,94,52,62,84,79,74,80,80,90,
70,65,64,51,43,45,50,66,87,85,40,96,71,82,49,
50,56,53,66,79,84,48,79,84,90,60,55,58,65,65,
61,78,81,73,53,90,90,96,94,83,85,83,63,66,62,
80,68,40,97,40,74,42,50,80,81,63,55,69,57,64,
40,50,98,62,79,50,99,42,76,64,42,92,44,54,57,
74,44,55,44,44,75,47,57,95,72,92,86,52,80,54,
44,100,81,68,68,69,50,79,86,99,78,71,49,76,82,
67,51,46,88,87,90,45,89,78,56,41,89,80,46,98,
71,91,52,44,66,86,92,67,42,74,65,51,71,53,49,
71,75]

maxScore = 112

qtyMarks = len(marks)
sumMarks = sum(marks)

# To avoid excluding marks that are equal to the avrgScore we 
# will compare Decimal against Integer (avrgScore agaisnt list of marks)
# i.e.: if avrgScore is 67 the 67's marks would've been excluded from the above and below avrgScore,
# since they are exactly the same
avrgScore = round((sumMarks / qtyMarks), 2)
avrgPerc = (avrgScore/maxScore) * 100

print("avrg score: {0}\navrg in %: {1:0.1f}%".format(avrgScore, avrgPerc))

# list of comprehension give me a list of all marks above avrgScore
#
# Usage example:
# 
# result is a list = [ <expression> for <item> in <list> if <condition> ]
aboveAvrg = [x for x in marks if x > avrgScore]
aboveAvrgPerc = round(((len(aboveAvrg) / qtyMarks) * 100), 2)
aboveAvrg.sort()

print("\n{}% marks above avrg:\n{}".format(aboveAvrgPerc, aboveAvrg))

# return a list of all marks below avrgScore
belowAvrg = [x for x in marks if x < avrgScore]
belowAvrgPerc = round(((len(belowAvrg) / qtyMarks) * 100), 2)
belowAvrg.sort()

print("\n{}% marks below avrg:\n{}".format(belowAvrgPerc, belowAvrg))


 