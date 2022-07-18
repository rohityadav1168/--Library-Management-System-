#It is the program's main module, from which all other modules are imported.
name = input("Enter your Full Name:")
while name == "":
     print(" Name cannot be left empty!!! Please, Enter the Full Name !! ")
     name = input("Enter your Full Name : ")
     
import displaying
import return_file
import borrow_file
print("\n")
print("\t\t\t\t\t" + "Hello", name + "!!")
print("\t\t\t" + "************ welcome to Library Mangement System*********************")
#displaying multiple options for the user
# If the select anything other than 1,2,3, and 4, the user's input will be recognized as invalid.
while True:
     print("Tap 1 to display the entire library's collection of books : ")
     print("Tap 2 to borrow book : ")
     print("Tap 3 to return book : ")
     print("Tap 4 to exit : ")
     answer = int(input("Enter your choice : "))

     if answer == 1:
        print(displaying.displaying_book())

     elif answer == 2:
        print(displaying.displaying_book())
        print("\n")
        borrow_file.borrow()

     elif answer == 3:
        print(displaying.displaying_book())
        return_file.returning()

     elif answer == 4:
         print("***************Thank you so much! For Using our Library Mangement System *************")
         exit()
     else:
         print("You've typed a number that was not in the acceptable range. \n please try again!!")
