# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a parameter. 
# The constructor must assign  the integer value to  the age variable after confirming the argument passed is not negative; 
# if a negative argument is passed then the constructor should set  age to 0  and print “Age is not valid, setting age to 0”. 
#
# In addition, you must write the following instance methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:
# If age is between 0 and <13, print “You are young”.
# If  age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.
# Sample Input for amIOld():
#     -1
#     4
#     10
#     16
#     18
#     64
#     38
# Expected Output for amIOld():
#     Age is not valid, setting age to 0.  
#     You are young.   
#     You are young.   
#     You are a teenager.  
#     You are a teenager.   
#     You are old.   
#     You are old.
# Consider the age variable to be set to 38 then: 
#     Sample Input for yearPasses(): 4
#     Expected Output for yearPasses(): 42

class Person():
    def __init__(self,age):
        if age < 0:
           print ("Age is not valid, setting age to 0.")
           self.age = 0
        else:
            self.age = age
    def amIOld(self):
        if self.age < 13:
           print ("You are young.")
        elif(self.age>=13 and self.age<=19):
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def yearPasses(self,Sample_ip_for_yearpasses):
        self.age += Sample_ip_for_yearpasses
        print(self.age)


sample_ip_list = [-1,4,10,16,18,64,38]      
for x in sample_ip_list:
    ans1=Person(x)
    ans1.amIOld()
    print("")
ans1.yearPasses(4)





