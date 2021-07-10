import pandas
import random

# a=0
# data=pandas.read_csv("E:/Python Tutorials/programs/app brewery/Flash Card App/data/french_words.csv")
# new_dict=data.to_dict()

# # print(list(new_dict.keys())[0])
# # # print(day.index)

# # length=data.count()
# num=random.randint(0,101)

# french_dict=new_dict["French"]
# english_dict=new_dict["English"]

# # print(french_dict)
# # print(english_dict)

# # # print(num)
# french_word=french_dict[num]
# english_word=english_dict[num]

# print(french_word)
# print(english_word)

# french_dict.pop(num)
# english_dict.pop(num)

# french_dict.update(english_dict)
# print(len(french_dict))


# # print(french_dict)
# # print(english_dict)

# # # print(english_dict)
# # print(f"{french_dict[num]} :- {english_dict[num]}")

# # day1=data[data[num]]
# # print(day1)

# # def Merge(dict1, dict2):
# #     return(dict2.update(dict1))

# # print(Merge(french_dict,english_dict))

# # print(french_dict)

       
# # Driver code 
# # dict1 = {'x': 10, 'y': 8} 
# # dict2 = {'a': 6, 'b': 4} 
# # dict1.update(dict2)
# # print(dict1)

data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")
print(to_learn)