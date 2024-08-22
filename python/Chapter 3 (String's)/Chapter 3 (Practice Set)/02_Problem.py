# 16
# CHAPTER 3 – PRACTICE SET
# 1.
# Write a python program to display a user entered name followed by Good Afternoon using input () function.
# 2.
# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|Name|>, You are selected! <|Date|> '''

new_Letter = letter.replace("<|Name|>", "<|Majjbeen|>").replace("<|Date|>", "<|Bujjbeen Ko Pata Hai|>")


print(new_Letter)