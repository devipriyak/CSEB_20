'''if-else
if condition:    #True
    statement(s)
else:            #False
    statements
'''
#Python program to read age of student and check whether
#student is eligible for vote or not
name=raw_input("Enter input")#String
age=int(raw_input("Enter age"))#int
#Check condition
if age>=18:
      print "Hello",name
      print("You are Eligible for Vote")
else:
      print "Sorry!",name
      print "Not elgible for vote due to",age

      
      
