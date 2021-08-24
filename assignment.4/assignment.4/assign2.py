# 1.  Write a Python program to clone a list. my_list = ['this', True, 'student', 45, 66.43]
# 2. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List =
# ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output = ['Green', 'White', 'Black']
# 3. Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


# /* ------soln----------*/

# /*--------1---------*/
my_list=[ 'This',True,'student',45,66.3]
list1=my_list.copy()
print(my_list)


# /*---------2------------*/
sample_list=['Red','Green','White','Black','Pink','Yellow']
alist=sample_list.remove('Red')
print(sample_list)
alist=sample_list.remove('Pink')
print(sample_list)
alist=sample_list.remove('Yellow')
print(sample_list)






# /*--------3-------*/
user_color=['Red','Green','White','Black','Pink','Yellow']
list=input('enter a color:\n')
user_color.append(list)
print(user_color)



