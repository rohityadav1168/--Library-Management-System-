import displaying
#Method for returning book
#approaches for restoring books
def restoring_Info():
    books_Id = []
    keylist = displaying.total_all_keys()
    days = []
    name = input("please! Enter your Name: ")
    while name == "":
        print(" Name cannot be left empty!!! Please, Enter the returner's name. !! ")
        name = input("Enter your  Name : ")
     
    book_id1 = input("please! enter the book ID you'd want to return back: ")
    if book_id1 in keylist:
        books_Id.append(book_id1)
        selected = False
        while selected == False:
            #using try and except method to handle error
            try:
                total_borrowed_days = int(input("Number of days did you kept the books)?"))
                days.append(total_borrowed_days)
                selected = True
            except:
                print("invalid input!!. enter integer value")
    else:
        print("Sorry You have entered an invalid Book ID Please Enter Valid Book ID!!!!")
    selected = False
    while selected == False:
        answer = input("sorry! This book has already return by You Would you like to return a another book?? (y/n)")
        if answer == "y":
            book_id1 = input("plz! enter book id")
            if book_id1 in keylist:
                books_Id.append(book_id1)
                selected = False
                while selected == False:
                    try:
                        total_borrowed_days = int(input("number of days did you kept the books)?"))
                        days.append(total_borrowed_days)
                        selected = True
                    except:
                        print("Invalid input?? enter the integer value !! ")
            else:
                print("Invalid Book ID !!!!!!!")
        elif answer == "n" :
            selected = True
        else:
            print("error!the character you entered is not valid")
    print(books_Id)
    return books_Id, name, days
print("\n")
# For charging an extra fee if the book isn't returned on time module.
def fine_Calc():
    fine_box = []
    overall_fines = 0
    borrowed_days = []
    dictionary = displaying.book_dict()
    user_Info = restoring_Info()
    Books_Id = user_Info[0]
    name = user_Info[1]
    days1 = user_Info[2]
    chargeless_duration = 10
    for key, value in dictionary.items():
        cost = value[3]
        cost = cost.replace("$", "")
        cost = float(cost)
        if key in Books_Id:
            position = Books_Id.index(key)
            borrowed_tenure = days1[position]
            borrowed_days.append(borrowed_tenure)
            if borrowed_tenure > chargeless_duration:
                extra_days = borrowed_tenure - chargeless_duration
                fine = (20 / 100) * cost * extra_days
                fine = round(fine, 2)
                overall_fines += fine
                fine = "$" + str(fine)
                fine_box.append(fine)
            else:
                if key in Books_Id:
                    fine_box.append("$0")
                    overall_fines += cost

    overall_fines = "$" + str(overall_fines)
    return fine_box, overall_fines, Books_Id, name, borrowed_days


#in this returning module "trturningInfo.txt" is a new next file to generate return note
def returning():
    dictionary = displaying.book_dict()
    user_info = fine_Calc()
    fines = user_info[0]
    totalFine = user_info[1]
    booksId = user_info[2]
    name = user_info[3]
    borrowed_days = user_info[4]
    keylist = displaying.total_all_keys()
    file1 = open("returningInfo.txt","a")
    file2 = open("book.txt","w")
    info = ""
    i = 0
    for key,value in dictionary.items():
        if key in booksId:
            rate = value[3]
            quantities = int(value[2])+1
            info += (key +"\t\t\t" + value[0] + "\t\t\t" + value[3] + "\t\t" + str(borrowed_days[i]) + "\t\t" + fines[i] + "\n")
            i += 1
            if key == keylist[-1]:
                file2.write(key + "," + value[0] + "," + value[1] + "," + str(quantities) + "," + value[3])
            else:
                file2.write(key + "," + value[0] + "," + value[1] + "," + str(quantities) + "," + value[3] + "\n")
        else:
            if key == keylist[-1]:
                file2.write(key + "," + value[0] + "," + value[1] + "," + value[2] + "," + value[3])
            else:
                file2.write(key + "," + value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")

    file1.write(" ********************************************************************************** \n ")
    file1.write("\n")
    file1.write("name = " + name + "\n")
    file1.write("BOOK ID" + "\t\t\t" + "BOOk NAME" + "\t\t" + "PRICE" + "\t" + " BORROWED DURATION" + "\t" + "FINE" + "\n")
    file1.write(info+ "\n")
    file1.write("\n")
    file1.write("\t\t\t\t\t\t\t\t\t\t TOTAL FINES  :- " + totalFine + "\n")
    file1.write(" ==================================================================\n ")
    file1.close()
    file2.close()
