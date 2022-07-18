import displaying
#Borrower information is kept on file.
def borrowerInfo():
    storing_section = []
    allkeys = displaying.total_all_keys()
    dictionary = displaying.book_dict()
    stu_name = input("Enter your  Name : ")
    while stu_name == "":
        print(" Name cannot be left empty!!! Please, Enter the Borrower's name. !! ")
        stu_name = input("Enter your  Name : ")
    
    book_ID = input("Enter the  book ID which you want to borrow")
    if book_ID in allkeys:
        for key, value in dictionary.items():
            if key == book_ID:
                if int(value[2]) > 0:
                    storing_section.append(book_ID)
                else:
                    print("sorry! The  book is  not available for . please ! try next one")
    else:
        print(" Sorry You have entered an invalid Book ID Please Enter Valid Book ID. !! ")

    selected = False
    while selected == False:
        answer = input(" Do you like to borrow another Book ? (y/n) ")
        if answer == "y" :
            book_ID = input("enter the book ID which you want to borrow")
            if book_ID in allkeys:
                for key, value in dictionary.items():
                    if key == book_ID:
                        if int(value[2]) > 0:
                            storing_section.append(book_ID)
                        else:
                            print("sorry! This book has suddenly been unavailable.. please ! try next time")
            else:
                print("Sorry You have entered an invalid Book ID Please Enter Valid Book ID!!")
           

        elif answer == "n":
            selected = True

        else:
            print("Invalid character. Please Enter a valid Character !! ")
    print(storing_section)
    return storing_section,stu_name
#function for Calculating of the total cost paid by the user during book borrowing:
def book_cost():
    userinfo = borrowerInfo()
    dictionary = displaying.book_dict()
    Id = userinfo[0]
    name_of_borrower = userinfo[1]
    total_cost = 0
    for key,value in dictionary.items():
        if key in Id:
            rate = value[3]
            rate = rate.replace("$","")
            rate = float(rate)
            total_cost += rate
    total1 = "$" + str(total_cost)
    return total1,Id,name_of_borrower
print("\n")
#Generating  borrower file in write mode in addition updating dictionary:
def borrow():
    dictionary1 = displaying.book_dict()
    list_of_keys = displaying.total_all_keys()
    full_info  = book_cost()
    total = full_info[0]
    book_Id = full_info[1]
    borrower_Name = full_info[2]
    info = ""
    file1 = open("borrower_data.txt","a")
    file2 = open("book.txt","w")
    for key,value in dictionary1.items():
        if key in book_Id:
            rate = value[3]
            quantities = int(value[2])-1
            info += (key + "\t\t" + value[0] + "\t\t" + value[3] + "\n")
            if key == list_of_keys[-1]:
                update_book = key + "," + value[0] + "," + value[1] + "," + str(quantities) + "," + value[3]
                file2.write(update_book)
            else:
                update_book = key + "," + value[0] + "," + value[1] + "," + str(quantities) + "," + value[3] + "\n"
                file2.write(update_book)
        else:
            if key == list_of_keys[-1]:
                update_book = key + "," + value[0] + "," + value[1] + "," + value[2] + "," + value[3]
                file2.write(update_book)
            else:
                update_book = key + "," + value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
                file2.write(update_book)
    print("\n")
    file1.write(" ======================================================\n")
    file1.write("\n")
    file1.write("\n")
    file1.write(" NAME OF BORROWER: " + borrower_Name + "\n")
    file1.write("BOOK ID" + "\t\t" + "BOOK NAME" + "\t\t" + "PRICE" + "\n")
    file1.write(info + "\n")
    file1.write("\n")
    file1.write("\n")
    file1.write(" \t\t\t\t\t TOTAL :" + total + "\n")
    file1.write("----------------------------------------\n")
    file1.close()
    file2.close()
    return file1
