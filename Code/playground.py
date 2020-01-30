from __future__ import division, print_function
from random import randint, choice, seed
seed(1) #for different random nums
import re #for changing lines to words list

myDic = {1:["kobe", "mj"], 3:["wade", "lebron"]}
print(myDic[1])
values = myDic.keys()
print(values)
for count in values: #loop through each values in dic
    players = myDic[count]
    for player in players:
        if player == "wade":
            print(f"{player} has {count} count")
# myDic.pop(2)
print(f"my dic is {myDic}")

newDic = {"kobe": 24, "mj":23}
# print(newDic)
number = -1
# if "kobe" in newDic:
number = newDic.get("kk",0)
# else:
#     number = 0
print(number)
# for word in words:
#     word_count = words_histogram.get(word, 0) + 1  #if word is in words_histogram's keys, count will increment, else equal 1
#     words_histogram[word] = word_count