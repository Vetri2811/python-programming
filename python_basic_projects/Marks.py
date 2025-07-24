print("Enter Your Marks") #Print "Enter Your Makrs"
a=int(input("Tamil: "))   #print "Tamil:" After get integer input from user 
b=int(input("English: "))
c=int(input("Maths: "))
d=int(input("Science: "))
e=int(input("Social: "))
f=a+b+c+d+e                   #Add all given number and store "f"
g=f/500*100                   #calculate percentage and store "g"
if(f>500):
     print("Invaild Plase enter vaild Mark (Total Mark is: 100 Each sub)")      #if total grater then 500 the input is wrong 
elif(f>400):
    print("Grade A")                 #if grater then 400 print"Grade A"
elif(300<f):
    print("Grade B")                #if grater then 300 print"Grade B"
elif(175<f):
    print("Grade c")                     #if grater then 175 print"Grade C"
else:
    print("Fail")                       #else less then or equal 175 print "Fail"

print("Total: ",f,"/500")               #print total marks/500
print("Your Percentage: ",g,"%")        #print percentage 

