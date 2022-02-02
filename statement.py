"""In the shell or in a text editor, write a program that asks for the user to sign up for Programmer's Toolkit Monthly Subscription Box. They must select level of membership they want. Each month is something different, t-shirts, stickers, figurines, even programming books!
The levels are the following:
    Platinum
    Gold
    Silver
    Bronze
    Free Trial
Write an if statement that prints the cost for each of the level. Platinum is $60, each level below is 10 dollars cheaper, and the free trial is free.
Submit your .py file."""
# Input                            Expected Output         Actual Output
# if package == 'Platinum':      The cost is 60            Nothing
 #print('The cost is:',str(60))
#elif package =='Bronze':        The cost is 30            Free
 #print('The cost is:',str(30))   Free Trial is Free
#else:
#print('free')
x = "Programmer's Toolkit Monthly Subscription Box"
print(x)
y = "We have many package for you"
print(y)
print('Platinum')
print('Gold')
print('Silver')
print('Bronze')
print('Free Trial')
print('That inclued t-shirts,books,stickers, figurines')
first_name = input('Please enter your first name')
last_name = input('Please enter your last name')
age = input('Please enter your age')
package = input('Please choose your package')
if package == 'Platinum': print('The cost is $60 ')
if package == 'Gold':print('The cost is $50')
if package == 'Silver':print('The cost is 40')
if package == 'Bronze': print('The cost is $30')
if package == 'Free Trial':print('The cost is Free')

