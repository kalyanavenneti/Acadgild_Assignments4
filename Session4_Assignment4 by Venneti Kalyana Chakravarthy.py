
# coding: utf-8

# In[8]:


# Question 1.1-: Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
#area = (s(s-a)(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent class and 
#function to calculate the area should be defined in subclass.


#Parent class
class Triangle:
    def __init__(self):
        number_of_sides=['a','b','c']
        self.TriangleSides=number_of_sides
        
    def sides_Of_Triangle(self):
        self.sides_Of_Traingle=[input("Enter the Side "+i+" :") for i in self.TriangleSides]
        
#Sub class       
class Traingle_Area(Triangle):
    def __init__(self):
        Triangle.__init__(self)
        
    def area_Of_Triangle(self):
                
        # Iterator has been created to iterate sides of triangle from collection
        triangleSides=iter(self.sides_Of_Traingle)
        a=float(next(triangleSides))
        b=float(next(triangleSides))
        c=float(next(triangleSides))      
           
        # Half-perimeter (s) of Triangle         
        s= (a+b+c)*0.5        
        # Area of Triangle         
        Area = (s*(s-a)*(s-b)*(s-c))**0.5    
        print("The sides of triangle are a="+str(a)+", b="+str(b)+", c="+str(c))     
        Area = ('The Area of the triangle is %0.2f' %Area )
        #return Area
        print(Area)
        
# Create object of Sub class Traingle_Area()
Area_Of_Traingle = Traingle_Area()

#Ask User to Enter the sides of Triangle
Area_Of_Traingle.sides_Of_Triangle()

# Calculate the Area Of Triangle
Area_Of_Traingle.area_Of_Triangle()


# In[9]:


# Question 1.2-: Write a function filter_long_words() that takes a list of words and an integer n and 
#returns the list of words that are longer than n

#Function to Filter words based on length
def filter_long_words(WordList,n):
        
    #List Comprehensions
    Wordlist=[x.strip() for x in WordList if len(x.strip())>n]
    
    if(len(Wordlist)>0):
        print("\n Output:")
        print("\n The List of longest words , which  are longer than "+str(n)+" is :")
        return Wordlist
    else:
        return "No Words longer than specified number "+str(n)
    
#Ask user's Input
print("Input:")
string= input("Please enter your words: ")
number= int(input("Please enter your number: "))

# Split the words by "," comma and convert into list
list_Of_Words = list(string.split(","))
#Function Execution
filter_long_words(list_Of_Words,number)


# In[10]:


#Question 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the 
#lengths of the corresponding words . Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as 
# [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.

def map_Words_to_Length(List):
    ''' This function Map's the words with their corresponding length'''
    return list(map(len, List))

word_List=list(input("Input : Please enter Words : ").split(","))
#List Comprehension has been done to remove white trailing white spaces
List=[x.strip() for x in word_List]
#function Execution
Words_lengths=map_Words_to_Length(List)

print("Output: Length of Words are :",Words_lengths )


# In[16]:


# Question 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, 
# False otherwise.

def vowel_checker(inputChar):
    #docstring
    return_value=''
    if(len(inputChar)==1):
        vowel_list=['a','e','i','o','u']
        if (inputChar.lower() in vowel_list):
            return_value= True
        else:
            return_value= False
    else:
        return_value="Please enter single character only!"        
    return return_value


print("Enter character to check that it is Vowel or not")
input_value = input("Input Value: ")

output_value=vowel_checker(input_value) 

print("Output Value:",output_value)

print("Enter character to check that it is Vowel or not")
input_value = input("Input Value: ")


output_value=vowel_checker(input_value) 


print("Output Value:",output_value)

