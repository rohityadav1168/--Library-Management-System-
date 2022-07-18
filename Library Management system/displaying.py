# Originally, the dictionary book id was used as the key, and additional information were used as the value.
def book_dict():
    file = open("book.txt", "r")
    book_data = file.read()
    file.close()
    books_list = book_data.split("\n")
    books_list1 = []
    for each_item in books_list:
        books_list1.append(each_item.split(","))
    # Now, join the above list into a dictionary with the book id as the key and the rest of the book's data as the value.
    dictionary = {}
    for pre_list in books_list1:
        value = []
        for each_item in pre_list:
            if each_item == pre_list[0]:
                key = each_item
            else:
                value.append(each_item)
        dictionary[key] = value
    return dictionary
w = book_dict()
print(w)


# a component for displaying book details
#It shows the book's id, title, author, and other details.
def displaying_book():
    dictionary = book_dict()
    data1 = "| Book Id" + "\t" + "| Book Name" + "\t\t\t" + "| author name" + "\t\t\t" + "| quantity" + "\t\t" + "| price" + "\n"
    for key, value in dictionary.items():
        data1 += ("| "+key + "\t\t| " + value[0] + "\t\t\t| " + value[1] + "\t\t\t| " + value[2] + "\t\t\t| " + value[3] + "\n")
    return data1

# print(display_books())
#module for creating a list of all keys.
def total_all_keys():
    keys_list = []
    for key, value in book_dict().items():
        keys_list.append(key)
    return keys_list
