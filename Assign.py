# 	NEW ASSIGNMENTDue 23 Aug
# Data Structures(list)
# 1. Join the items of this list to a string sentence. Print the result on the terminal. 
#     my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
# 2. Change the value of True in this list to False. Print the result on the terminal
#     new_list = ['this', "brown", 55, "oxen", True, 0.85]
# 3. Given the list below:
#      list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

#     Get 5000 and 500 out of the list and add them together.
#    Print the result on the terminal

# soln

my_list= ["The", "quick", "brown", "fox", "jump", "over", "the",
"lazy", "dog",]






# 1.

my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
print(len(my_list))







# 2

# Change the value of True in this list to False. Print the result on the terminal
new_list= ['this', "brown", 55, "oxen", True, 0.85]
# change of value
print(new_list[4])
new_list[4]="False"
print(new_list[4])



# 3.
list1 =[10, 20, [300, 400, [5000, 6000], 500], 30, 40]
first_num=list1[2][2][0]
print(first_num)
second_num= list1[2][3]
print(first_num + second_num)