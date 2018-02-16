
# coding: utf-8

# # Data Boot Camp
# ## Code Practice 2
# ### Dillon Fournier
# Due: February 16th, 2018

# ### 1. Review. Does this code run without error? If so, what does it produce? If not, explain why.
# x = [1, 2, 3]
# y = 'bootcamp’
# z = x + y
# 
# No, this code does not run without error. It produces an error saying that it cannot concatenate a string to a list, only a list to a list.

# In[2]:


x = [1, 2, 3]
y = 'bootcamp'
z = x + y


# ### 2. Review. For the same x and y as the previous question: What function tells us what type
# they are? What function tells us how many elements they contain?
# the type function tells us the type of the function, while the len function tells us how many characters or elements they contain

# In[3]:


type(x)


# In[6]:


print(type(y))



# In[7]:


len(x)


# In[8]:


len(y)


# ### 3. What type is each expression? How can you tell?
# 2 is an int, its an integer without a decimal point
# 
# ’2’ is a str, you can tell because of the quotation marks around it
# 
# 2.0 is a float, you can tell because it has a decimal point
# 
# "2.0" is a string, you can tell because of the quotation marks around it
# 
# 2>1 is a boolean, or bool, you can tell because it is a verifiable statement
# 
# ’Itamar’ > ’Chase’ is a boolean, because its a verifiable statement ('itamar' is a higher unicode value than 'chase' because 
# 'I'' is a higher unicode than 'C')
# 
# [1, 2] is a list. You can tell by the [] brackets
# 
# (1, 2) is a tuple. You can tell by the () parentheses
# 
# {1: ’one’, 2: ’two’} Is a dictionary, you can tell by the {} and the format, with the colon followed by an entry.

# In[12]:


'Itamar' > 'Chase'


# In[14]:


x=[1,2]


# In[15]:


type(x)


# In[20]:


q= {1: 'one', 2: 'two'}
type(q)


# ### 4. What value does each of these comparisons have?
# 1>=0 is true
# 
# 1 >= 1 is true
# 
# 1 > 1 is false
# 
# 1==1 is true
# 
# 1 == 1.0 is true
# 
# ’Spencer’ == "Spencer" is true
# 
# 2**3 > 3**2 is false
# 
# 1 >= 0 or 1 <= 2 is true
# 
# 1 >= 0 and 1 <= 2 is true

# In[21]:


1>= 0


# In[22]:


1>= 1


# In[23]:


1 >1


# In[24]:


1==1


# In[25]:


1 == 1.0


# In[26]:


'spencer' == "spencer"


# In[27]:


2**3 > 3**2


# In[28]:


1 >= 0 or 1 <= 2


# In[29]:


1 >= 0 and 1 <= 2


# ### 5. Does this code run without error? If so, what does it produce? If not, how would you fix it?
# if 2>1
# print(’Yes, 2 is still greater than 1’)
# 
# No, it has an error. In order to fix it, you must add a colon after the 2>1 and include a space.

# In[13]:


if 2>1 :
    print('Yes, 2 is still greater than 1')


# ### 6. What is the result of running this code? Why?
# if True:
# print(’on the one hand’)
# else:
# print(’but on the other hand’)
# The Result is that it prints "on the one hand". This is because it found that the result is true.
# 
# #### What happens if we replace True with False in the first line? What happens if we insert the word not after if in the first line?
# If we replace true with false, then it prints "on the otherhand", while if we place not after "if" in the first line of the original code we also get it to print "on the otherhand"
# 

# In[10]:


if True:
    print("on the one hand")
else:
    print("but on the other hand")


# In[11]:


if False:
    print("on the one hand")
else:
    print("but on the other hand")


# In[12]:


if not True:
    print("on the one hand")
else:
    print("but on the other hand")


# ### 7. What is the result of running this code?
# cond = True
# if cond:
# x = "Chase"
# else:
# x = "Dave"
# print(x)
# The code prints the word Chase becaue cond was true

# In[48]:


cond = True
if cond:
    x = "Chase"
else:
    x = "Dave"
print(x)


# ### 8. Suppose we have two lists, x = [1, 2, 3, 4] and y = [’x’, ’y’, ’z’]. Adapt the code below to determine which has more elements:
# if <insert expression>:
# print(’x has more’)
# else:
# print("y has at least as many")
# See below for code: X has more 

# In[50]:


x=[1,2,3,4]
y=['x','y','z']
ans = len(x) > len(y) 
if ans:
    print('x has more')
else: 
    print('y has at least as many')


# ### 9. Explain in words what slicing does.
# Slicing pulls out a character, word, or entry from a particular object by selecting the numbered entry that you wanted to slice. See below, where x= "I can't believe it" and x[2] is "a"

# In[15]:



x= "I can't believe it"
x[3]


# ### 10. How would you extract (“slice”) the first element (the integer 1) from the list x below? The last element? All but the last element?
# x = [1, 2, 3, 4, 5]
# To extract the first element you would type x[0], the last element would be x[4], and all but the last would be x[0:4] 

# In[25]:


x = [1, 2, 3, 4, 5]
print(x[0], x[4], x[0:4])


# ### 11. Use slicing to extract each word from sentence = ’This is a sentence; please slice it.’
# I would use sentence.split() which would extract each word from the sentence as in below.
# 

# In[22]:


sentence = "This is a sentence; please slice it"
sentence.split()


# ### 12. Consider the list
# x = [1, 2, "a", ’b’, "fast", ’slow’, 3, "Raghu", ’Liuren’, 10]
# a. How would you slice out the first item? The last item?
# b. How would you slice out the items from ’b’ to 3 inclusive?
# 
# a. to slice the first item, you would input x[0], while to slice the last item you would input x[9]
# 
# b. To slice the first item, you would input x[3:7]

# In[4]:


x = [1, 2, "a", "b", "fast", "slow", 3, "Raghu", "Liuren", 10]
print(x[0], x[9], x[3:7])



# ### 13. Using the same list x, write a loop that prints every element on a new line.
# 
# To loop this, I would run the for loop below, which iterates through the items and prints them each on a new line

# In[5]:


for item in x:
    print(item)


# ### 14. *Challenging*. Using the same list x, write a loop that prints every element of type str.
# I would use an if function that tells it to print if the type(item) == str

# In[10]:


for item in x:
    if type(item) == str:
        print(item)

    


# In[8]:


type(x[1])


# In[49]:


get_ipython().magic('pinfo range')


# ### 15. Use Spyder’s help to find out what the range function does. How would you describe range(3,12,2)? Verify by converting to a list with list(range(3,12,2)).
# 
# The range function shows all the integers i to j-1 in a specified range between i and j. adding the third number specifies how many results minus 1 should be skipped, so range(3,12,2) compiles every other number between 2 (inclusive) and 12 (exclusive).

# In[52]:


list(range(3,12,2))


# ### 16. Challenging. Write a loop that sums the integers from zero to thirty that are multiples of three: 3, 6, etc.
# 
# As you can see below the loop sums the integers between 3 and 30 that are multiples of 3, finding a final value of 30

# In[11]:


sumo = 0
for number in range(3, 31, 3):
    sumo = sumo + number 
    print(sumo)
    


# In[12]:


type(sumo)


# ### 17. Define a function pocket_change() that takes four integers as inputs (numbers of pennies, nickels, dimes, and quarters in your pocket) and returns a floating point number (their dollar value). Run your program with the input (1, 2, 3, 4). Bonus (optional): Report the value with a dollar sign.
# 
# See below for answer

# In[22]:


def pocket_change(penny, nickel, dime, quarter):
    pennyvalue = penny*.01
    nickelvalue = nickel * .05
    dimevalue = dime * .1
    quartervalue = quarter * .25
    total = pennyvalue + nickelvalue + dimevalue + quartervalue
    return total
print('$', pocket_change(1, 2, 3, 4))


# ### Challenging. Write a function notsix() that takes a list of integers and returns a (shorter) list of only those that do not begin with a 6. Test it on the list [1234, 6783, 6, 4321, 9876]. Hints: You can create a blank list with x = []. You can append item to it with x.append(item)
# 
# See function run below

# In[41]:


def notsix(listy):
    x = []
    for item in listy:
        if str(item)[0] != '6':
            x.append(item)
    return x
test = [1234, 6783, 6, 4321, 9896]
print(notsix(test))
    


# ### 19. Challenging. Explain what this code does:
# old_list = [1234, 6783, 6, 4321, 9876]
# new_list = [x for x in old_list if str(x)[0] != "6"]
# This code creates a new_list that is defined as the old_list with only the entries that, when converted to strings, don't start with "6".

# In[24]:


old_list = [1234, 6783, 6, 4321, 9876]
new_list = [x for x in old_list if str(x)[0] != "6"]
print(new_list)


# ### 20. Consider the Python object
# z = {1: ’one’, 2: ’two’, 3: ’three’}
# a. What kind of object is z? What is its length?
# 
# b. Which components are keys? Which are values?
# 
# c. How would I get the value associated with the key 2?
# 
# d. Use Spyder’s help facilities to figure out what z.keys() does. Ditto z.values(). Try
# them to verify.
# 
# e. What does list(z.keys()) do?
# 
# f. What does list(z.values()) do?
# 
# a. z is a dictionary with length= 3
# b. 1, 2, 3 are the key components, while 'one', 'two' and 'three' are the values components
# c. to get the value associated with key 2 you'd type z[2] and it would pop out "two"
# d. z.keys() prints a dict_keys list of the keys in the dictionary z, while z.values() gives a dict_values list of the values in dictionary z
# e. list(z.keys()) prints a list of the keys in z
# f. list(z.values()) prints a list of the values in z.
# 

# In[25]:


z = {1: "one", 2: "two", 3: "three"}


# In[27]:


z[2]


# In[30]:


z.keys()


# In[31]:


z.values()


# In[32]:


list(z.keys())


# In[33]:


list(z.values())


# ### 21. Approximately how long did this assignment take you? Answer this by creating a .csv file and entering the time (in minutes) and posting it to your GitHub my_first_repository titled time_for_practice2.csv
# 
# It took me roughly 2 hours
